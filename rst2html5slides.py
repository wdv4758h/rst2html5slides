#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: André Felipe Dias <andref.dias@pronus.eng.br>

from __future__ import unicode_literals

"""
Translates a restructuredText document to a HTML5 slideshow
"""

__docformat__ = 'reStructuredText'

from docutils import nodes
from docutils.core import publish_from_doctree
from docutils.transforms import Transform
from docutils.parsers.rst.directives.html import MetaBody as Meta
from genshi.builder import tag, Element
from rst2html5 import HTML5Writer, HTML5Translator

import re
import media


class slide_contents(nodes.Element):
    pass


class SlideTransform(Transform):
    '''
    State Machine to transform default doctree to one with slideshow structure:
    section, header, contents.
    '''

    default_priority = 851

    # node classes that should be ignored to not form new slides
    skip_classes = (Meta.meta, nodes.docinfo)

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

    settings_spec = HTML5Writer.settings_spec + (
        'rst2html5slides Specific Options',
        None,
        (
            (
                'Specify the name of the slide distribution function. '
                'Options are "linear", "square" or "square-rotate". '
                'An additional parameter can be specified along with the name such as in '
                '"square_rotate  3".',
                ['--distribution'],
                {
                    'dest': 'distribution',
                    'metavar': '<function_name>'
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
                    'metavar': '<slide_selector>'
                },
            ),
        )
    )

    def __init__(self):
        HTML5Writer.__init__(self)
        self.translator_class = SlideTranslator

    def translate(self):
        self.parts['pseudoxml'] = self.document.pformat()  # get pseudoxml before HTML5.translate
        HTML5Writer.translate(self)

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
        HTML5Translator.__init__(self, *args)
        self._reset()
        settings = self.document.settings
        if settings.distribution:
            self.visit_field_distribution(settings.distribution)
        if settings.deck_selector:
            self.visit_field_deck_selector(settings.deck_selector)
        if settings.slide_selector:
            self.visit_field_slide_selector(settings.slide_selector)
        return

    def _compacted_paragraph(self, node):
        '''
        a single node followed by a single field list should also be compacted
        '''
        parent_length = len([n for n in node.parent
                             if not isinstance(n, (nodes.field_list))])
        return HTML5Translator._compacted_paragraph(self, node) or parent_length == 1

    def visit_section(self, node):
        if self.document.settings.manual_slide_identification:
            node['ids'] = []
        elif 'id' in self.slide_attributes:
            node['ids'] = [self.slide_attributes['id']]
        node.attributes.update(self.slide_attributes)
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
        self._reset()
        return

    def _reset(self):
        self.deck_selector = {'tag':'deck'}
        self.slide_selector = {'tag':'slide'}
        self.slide_attributes = {}
        self.distribution = {
            'func': None,
            'incr_x': 1600,
            'incr_y': 1600,
            'data-*': {},
            'visited': 0,
        }
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

    def visit_field_deck_selector(self, value):
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

    def visit_field_slide_selector(self, value):
        tag_name = self.tag_name_re.findall(value)
        class_ = self.class_re.findall(value)
        if tag_name:
            self.rst_terms['section'][0] = tag_name[0]
        if class_:
            self.slide_selector['class'] = class_[0]
        return

    def visit_field_incr_x(self, value):
        self.incr_x = int(value)
        return

    def visit_field_incr_y(self, value):
        self.incr_y = int(value)
        return

    def visit_field_distribution(self, field_value):
        self._distribute_slides()
        values = field_value.split()
        # distribution function names must end with '_distribution'
        self.distribution['func'] = getattr(self, values[0] + '_distribution')
        if len(values) > 1:
            self.distribution['parameter'] = int(values[1])
        return

    def _distribute_slides(self):
        '''
        Distribute slides spatially according to some predefined function.
        data-* attributes are used to keep the coordinates.
        '''
        if not self.distribution['func']:
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

        return {q[0].localname: convert(q[1]) for q in slide.attrib \
                if q[0].localname.startswith('data-')}

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

    def square_distribution(self, enumerated_slides):
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

    def square_rotate_distribution(self, enumerated_slides):
        '''
        Similar to square, but slides are rotated when line changes
        '''
        data_attributes = self.distribution['data-*']
        line_length = self.distribution.get('parameter', 4)
        incr_x = self.distribution['incr_x']
        incr_y = self.distribution['incr_y']
        for index, slide in enumerated_slides:
            if index == 0:
                x_ref = data_attributes.setdefault('data-x', 0)
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
