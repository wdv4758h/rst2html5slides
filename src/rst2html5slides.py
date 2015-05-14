#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: André Felipe Dias <andref.dias@pronus.eng.br>

from __future__ import unicode_literals

import re
import shutil
from os import makedirs
from os.path import join, dirname, basename, isfile, exists, curdir, split, splitext, abspath

from docutils import nodes
from docutils.io import FileOutput
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives.html import MetaBody as Meta
from docutils.transforms import Transform
from genshi.builder import Element, tag
from rst2html5 import HTML5Translator, HTML5Writer

try:
    from urllib.parse import urlparse
except ImportError:  # Python 2
    from urlparse import urlparse


"""
Translates a restructuredText document to a HTML5 slideshow
"""

__docformat__ = 'reStructuredText'


class presentation(nodes.Element):
    pass


class Presentation(Directive):

    '''
    This directive handles attributes global to the presentation.
    Usually, it is placed at the top of the document
    but it is possible to change presentation attributes in the middle.

    See test/cases.py for examples.
    '''

    option_spec = {
        'distribution': directives.unchanged,
        'deck-selector': directives.unchanged,
        'slide-selector': directives.unchanged,
        'increment': directives.unchanged,
    }

    def run(self):
        return [presentation(**self.options)]


directives.register_directive('presentation', Presentation)


class slide_contents(nodes.Element):
    pass


class SlideTransform(Transform):

    '''
    State Machine to transform default doctree to one with slideshow structure:
    section, header, contents.
    '''

    default_priority = 851

    # node classes that should be ignored to not form new slides
    force_new_slide = (presentation, nodes.field_list)
    skip_classes = (Meta.meta, nodes.docinfo) + force_new_slide

    def apply(self):
        self.contents = []
        self.header = []
        self.slides = []
        self.slide = nodes.section()
        self.inner_level = 0
        self.visit(self.document.children)
        self.document.extend(self.slides)
        return

    def visit(self, children):
        self.inner_level += 1
        while children:
            node = children.pop(0)
            if isinstance(node, self.skip_classes):
                if isinstance(node, self.force_new_slide):
                    # meta and docinfo doesn't close slide
                    # see meta_tag_and_slides in test/cases.py
                    self.close_slide()
                self.slides.append(node)
                continue
            self.parse(node)
        self.inner_level -= 1
        if self.inner_level <= 1:
            self.close_slide()
        return

    def parse(self, node):
        if isinstance(node, nodes.transition):
            self.close_slide()
            self.slide.update_all_atts(node)
        elif isinstance(node, nodes.section):
            # All subsections are flattened to the same level.
            if self.inner_level == 1:
                self.close_slide()
                self.slide.update_all_atts(node)
            self.visit(node.children)
        elif isinstance(node, (nodes.title, nodes.subtitle)):
            # Titles and subtitles are converted to nodes.title and
            # their heading levels are defined later during translation
            self.header.append(node)
        else:
            self.contents.append(node)
        return

    def close_slide(self):
        if not (self.contents or self.header):
            return
        if self.header:
            header = nodes.header()
            header.extend(self.header)
            self.slide.append(header)
            self.header = []
        if self.contents:
            contents = slide_contents()
            contents.extend(self.contents)
            self.contents = []
            self.slide.append(contents)
        self.slides.append(self.slide)
        self.slide = nodes.section()
        return


class SlideWriter(HTML5Writer):

    choices = ['impress.js', 'jmpress.js', 'deck.js', 'None']

    settings_spec = HTML5Writer.settings_spec + (
        'rst2html5slides Specific Options',
        None,
        (
            (
                'Choose a web presentation framework for the output. '
                'Possible values are %s. '
                'Default is %s.' % (', '.join(choices), choices[0]),
                ['--presentation'],
                {
                    'choices': choices,
                    'default': choices[0],
                    'metavar': '<framework>'
                }
            ),
            (
                'Specify the name of the slide distribution function. '
                'Options are "linear", "grid" or "grid-rotate". '
                'An additional parameter can be specified along with the name such as in '
                '"grid_rotate  3".',
                ['--distribution'],
                {
                    'metavar': '<function_name>',
                }
            ),
            (
                'Specify the value of the increment used by the distribution functions. '
                'To specify different values for X and Y increments, '
                'separate them by space. Example "1000 500". '
                'Default value is 1600 for X and Y increments.',
                ['--increment'],
                {
                    'metavar': '<increment>',
                }
            ),
            (
                'Disable slide automatic identification based on title.',
                ['--manual-slide-id'],
                {
                    'action': 'store_true',
                    'dest': 'manual_slide_identification',
                }
            ),
            (
                'Specify the tag, id and/or class to replace the default (and non-standard) '
                '<deck> tag used to surround the slides. '
                'Follow the pattern tag#id.class (such as a CSS selector). '
                'Examples: div, div#impress, div.deck-container, article#impress.impress-not-supported',
                ['--deck-selector'],
                {
                    'dest': 'deck_selector',
                    'metavar': '<deck_selector>',
                },
            ),
            (
                'Specify the tag, id and/or class to replace the default (and non-standard) '
                '<slide> tag used to surround each slide.'
                'Follow the pattern tag#id.class (such as a CSS selector)'
                'Examples: div.slide, section, div.step',
                ['--slide-selector'],
                {
                    'dest': 'slide_selector',
                    'metavar': '<slide_selector>',
                },
            ),
        )
    )

    def __init__(self):
        HTML5Writer.__init__(self)
        self.translator_class = SlideTranslator

    def rebuild_output(self):

        def copy_file(origin, destination):
            dest_dir = dirname(destination)
            if not exists(dest_dir):
                makedirs(dest_dir)
            shutil.copy(origin, destination)

        def roundrobin(*iterables):
            """
            roundrobin('ABC', 'D', 'EF') --> A D E B F C

            see: https://docs.python.org/3.4/library/itertools.html#itertools-recipes
            """
            from itertools import cycle, islice
            pending = len(iterables)
            # small modification to run under both Python 3 and 2
            next_attr = '__next__' if hasattr(iter(iterables[0]), '__next__') else 'next'
            nexts = cycle(getattr(iter(it), next_attr) for it in iterables)
            while pending:
                try:
                    for next in nexts:
                        yield next()
                except StopIteration:
                    pending -= 1
                    nexts = cycle(islice(nexts, pending))

        output = self.output
        href_pattern = re.compile('href=".*?"|src=".*?"')
        path_pattern = re.compile('"(.*?)"')
        hrefs = re.findall(href_pattern, output)
        save_to_destination = self.destination.destination_path not in ('<stdout>', '<string>')
        dest_dir = dirname(self.destination.destination_path)
        if save_to_destination:
            source_dir = dirname(self.document.settings._source)
        for i, href in enumerate(hrefs):
            path = re.findall(path_pattern, href)[0]
            if urlparse(path).netloc:  # scheme is not always present, but netloc is
                continue
            href_path = re.findall('^(?:\.+/)*(.*)', path)[0]
            hrefs[i] = re.sub(path_pattern, '"%s"' % href_path, href)
            if save_to_destination:
                source_path = join(source_dir, path)
                if not isfile(source_path):
                    # try css, js files relative to the template path
                    if isfile(self.document.settings.template):
                        template_dir = dirname(self.document.settings.template)
                    else:
                        template_dir = curdir
                    rel_template_path = abspath(join(template_dir, path))
                    if not isfile(rel_template_path):
                        self.document.reporter.error('file not found: %s' % source_path)
                        continue
                    source_path = rel_template_path
                copy_file(source_path, join(dest_dir, href_path))
        # rebuild output references
        splitted = re.split(href_pattern, output)
        self.output = ''.join(roundrobin(splitted, hrefs))
        return

    def translate(self):
        destination_path = self.destination.destination_path
        if destination_path not in ('<stdout>', '<string>'):  # there is a specified destination
            dest_dir, extension = splitext(destination_path)
            if extension:  # there is a filename in the destination
                dest_dir, dest_filename = split(destination_path)
            else:  # The specified destination is a directory. A new filename is necessary
                dest_filename = splitext(basename(self.document.settings._source))[0] + '.html'
            self.destination = FileOutput(destination_path=join(dest_dir, dest_filename),
                                          encoding='utf-8')
        HTML5Writer.translate(self)
        self.rebuild_output()
        return

    def get_transforms(self):
        return HTML5Writer.get_transforms(self) + [SlideTransform]


class SlideTranslator(HTML5Translator):

    tag_name_re = re.compile('^\w+')
    class_re = re.compile('\.([\w\-]+)')
    id_re = re.compile('#([\w|\-]+)')

    def __init__(self, *args):
        self.rst_terms['section'] = ['slide', 'visit_section', 'depart_section']  # [0] might be replaced later
        self.rst_terms['slide_contents'] = ('section', 'default_visit', 'default_departure')
        self.rst_terms['title'] = (None, 'visit_title', 'depart_title')  # flatten titles
        self.rst_terms['presentation'] = (None, 'visit_presentation', None)
        HTML5Translator.__init__(self, *args)
        self.metatags.append(tag.meta(generator='rst2html5slides'))
        self.metatags.append(tag.meta(generator_homepage='https://pypi.python.org/pypi/rst2html5slides'))
        self._reset_settings()
        return

    def _compacted_paragraph(self, node):
        '''
        a single node followed by a single field list should also be compacted
        '''
        field_list_sibling = len([n for n in node.parent
                                  if not isinstance(n, (nodes.field_list))]) == 1
        return not node['classes'] and \
            (HTML5Translator._compacted_paragraph(self, node) or field_list_sibling)

    def visit_section(self, node):
        if self.document.settings.manual_slide_identification:
            node['ids'] = []
        elif 'id' in self.slide_attributes:
            node['ids'] = [self.slide_attributes['id']]
        node.attributes.update(self.slide_attributes)
        if not self.distribution.get('func'):
            # (Only) slide data-* attributes are cumulative
            # otherwise impress.js defaults data-x,y,z to 0, data-scale to 1 etc.
            keys = list(self.slide_attributes.keys())
            for key in keys:
                if not key.startswith('data-'):
                    del self.slide_attributes[key]
        else:  # do not accumulate any slide attributes
            self.slide_attributes = {}
        self.default_visit(node)
        return

    def depart_section(self, node):
        self.heading_level = 0  # a new section reset title level
        if 'class' in self.slide_selector:
            node['classes'].extend([self.slide_selector['class']])
        self.default_departure(node)
        return

    def visit_title(self, node):
        '''
        In rst2html5slides, subsections are flattened and every title node is grouped
        inside the same header as a nodes.title.
        According to their position, the title node should become h1, h2, h3 etc.

        Example:

        <header>
            <title 1>
            <title 2>
            <title 3>

        becomes:

        <header>
            <h1>Title 1</h1>
            <h2>Subtitle</h2>
            <h3>Subsubtitle</h3>

        see test/cases.py  h2 and h3
        '''
        self.default_visit(node)
        self.heading_level += 1
        return

    def depart_document(self, node):
        self._distribute_slides()
        if len(self.context.stack[0]):
            deck = getattr(tag, self.deck_selector['tag'])(
                *self.context.stack[0],
                id=self.deck_selector.get('id', None),
                class_=self.deck_selector.get('class', None)
            )
            self.context.stack = ['\n', deck, '\n']
        # _reset is necessary to run the several test cases
        self._reset_settings()
        return

    def visit_field(self, node):
        field_name = node.children[0].astext()
        field_value = self._strip_spaces(node.children[1].astext())
        visit_field_func = getattr(self, 'visit_field_' + field_name.replace('-', '_'), None)
        if visit_field_func:
            visit_field_func(field_value)
        else:
            self.slide_attributes[field_name] = field_value
        raise nodes.SkipNode

    def visit_field_class(self, value):
        self.slide_attributes['classes'] = value.split()
        return

    def visit_field_classes(self, value):
        self.visit_field_class(value)
        return

    def visit_presentation(self, node):
        if 'distribution' in node:
            self._get_distribution(node['distribution'])
        if 'deck-selector' in node:
            self._get_deck_selector(node['deck-selector'])
        if 'slide-selector' in node:
            self._get_slide_selector(node['slide-selector'])
        if 'increment' in node:
            self._get_increment(node['increment'])
        raise nodes.SkipNode

    def _reset_settings(self):
        config = {
            'impress.js': ('impress.html', 'div#impress', 'div.step', 'linear'),
            'jmpress.js': ('jmpress.html', 'div#jmpress', 'div.step', 'linear'),
            'deck.js': ('deck.html', 'div#deck', 'div.step', 'none'),
            'None': ('default.html', 'deck', 'slide', 'none'),
        }
        self.distribution = {
            'incr_x': 1600,
            'incr_y': 1600,
            'data-*': {},
            'visited': 0,
        }
        self.deck_selector = {}
        self.slide_selector = {}
        self.slide_attributes = {}
        settings = self.document.settings
        template, deck_selector, slide_selector, distribution = config[settings.presentation]
        settings.template = settings.template or abspath(join(dirname(__file__), curdir, 'template', template))
        self._get_distribution(settings.distribution or distribution)
        self._get_deck_selector(settings.deck_selector or deck_selector)
        self._get_slide_selector(settings.slide_selector or slide_selector)
        self._get_increment(settings.increment)
        return

    def _get_deck_selector(self, value):
        tag_name = self.tag_name_re.findall(value)
        id = self.id_re.findall(value)
        class_ = self.class_re.findall(value)
        if tag_name:
            self.deck_selector['tag'] = tag_name[0]
        if id:
            self.deck_selector['id'] = id[0]
        if class_:
            self.deck_selector['class'] = class_[0]
        return

    def _get_slide_selector(self, value):
        tag_name = self.tag_name_re.findall(value)
        class_ = self.class_re.findall(value)
        if tag_name:
            self.rst_terms['section'][0] = tag_name[0]
        if class_:
            self.slide_selector['class'] = class_[0]
        return

    def _get_increment(self, value):
        if not value:
            return
        value = value.split()
        self.distribution['incr_x'] = int(value[0])
        self.distribution['incr_y'] = int(value[1]) if len(value) > 1 else self.distribution['incr_x']
        return

    def _get_distribution(self, field_value):
        # distribute all slides so far with current distribution function
        self._distribute_slides()
        if not field_value:
            return
        values = field_value.split()
        # distribution function names must end with '_distribution'
        self.distribution['func'] = getattr(self, values[0] + '_distribution', None)
        if len(values) > 1:
            self.distribution['parameter'] = int(values[1])
        elif 'parameter' in self.distribution:
            del self.distribution['parameter']
        return

    def _distribute_slides(self):
        '''
        Distribute slides spatially according to some predefined function.
        data-* attributes are used to keep the coordinates.
        '''
        if not (self.distribution.get('func') and self.context.stack):
            return
        initial_pos = self.distribution['visited']
        slides = (elem for item in self.context.stack[0][initial_pos::] for elem in item if isinstance(elem, Element))
        self.distribution['visited'] = len(self.context.stack[0])

        def enumerate_slides(slides):
            index = 0
            for slide in slides:
                slide_data = self._get_data(slide)
                if slide_data:
                    index = 0
                    self.distribution['data-*'].update(slide_data)
                yield index, slide
                index += 1

        self.distribution['func'](enumerate_slides(slides))
        return

    def _get_data(self, slide):

        def convert(value):
            if isinstance(value, (int, float)):
                return value
            try:
                if '.' in value:
                    return float(value)
                else:
                    return int(value)
            except ValueError:
                return value

        return {q[0].localname: convert(q[1]) for q in slide.attrib
                if q[0].localname.startswith('data-')}

    def none_distribution(self, enumerated_slides):
        '''
        Makes no positioning, but keep slide's data-* attributes
        '''
        data_attributes = self.distribution['data-*']
        for index, slide in enumerated_slides:
            slide(**data_attributes)

    def linear_distribution(self, enumerated_slides):
        '''
        Linear distribution
        '''
        data_attributes = self.distribution['data-*']
        data_attributes.setdefault('data-x', 0)
        incr_x = self.distribution['incr_x']
        for index, slide in enumerated_slides:
            slide(**data_attributes)
            data_attributes['data-x'] += incr_x
        return

    def grid_distribution(self, enumerated_slides):
        '''
        change line after certain number of slides
        It might receive one parameter to indicate the length of the line

        [ ] [ ] [ ] [ ]
        [ ] [ ] [ ] [ ]
        ...
        '''
        data_attributes = self.distribution['data-*']
        line_length = self.distribution.get('parameter', 4)
        incr_x = self.distribution['incr_x']
        incr_y = self.distribution['incr_y']
        for index, slide in enumerated_slides:
            if index == 0:
                x_ref = data_attributes.setdefault('data-x', 0)
            elif index % line_length == 0:  # break line
                data_attributes['data-x'] = x_ref
                data_attributes['data-y'] = data_attributes.setdefault('data-y', 0) + incr_y
            slide(**data_attributes)
            data_attributes['data-x'] += incr_x
        return

    def grid_rotate_distribution(self, enumerated_slides):
        '''
        Similar to grid, but slides are rotated when line changes
        '''
        data_attributes = self.distribution['data-*']
        line_length = self.distribution.get('parameter', 4)
        incr_x = self.distribution['incr_x']
        incr_y = self.distribution['incr_y']
        for index, slide in enumerated_slides:
            if index == 0:
                data_attributes.setdefault('data-x', 0)
                # jmpress doesn't rotate clockwise when it is 180
                rotate_z_ref = data_attributes.setdefault('data-rotate-z', 0) + 179.9
            elif index % line_length == 0:
                data_attributes['data-x'] -= incr_x  # keep same data-x reverting last += incr_x
                data_attributes['data-y'] = data_attributes.setdefault('data-y', 0) + incr_y
                incr_x = -incr_x
                data_attributes['data-rotate-z'] = rotate_z_ref \
                    if data_attributes['data-rotate-z'] != rotate_z_ref else (rotate_z_ref - 179.9)
            slide(**data_attributes)
            data_attributes['data-x'] += incr_x


def main():
    from docutils.core import publish_cmdline, default_description
    description = ('Translates a restructuredText document to a HTML5 slideshow.  ' +
                   default_description)
    publish_cmdline(writer=SlideWriter(), description=description)
    return


if __name__ == '__main__':
    main()
