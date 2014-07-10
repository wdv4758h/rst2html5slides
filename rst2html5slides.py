#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: André Felipe Dias <andref.dias@pronus.eng.br>

from __future__ import unicode_literals

"""
Translates a restructuredText document to a HTML5 slideshow
"""

__docformat__ = 'reStructuredText'

from collections import defaultdict
from docutils import nodes
from docutils.core import publish_from_doctree
from docutils.transforms import Transform
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives.html import MetaBody as Meta
from genshi.builder import tag, Element
from rst2html5 import HTML5Writer, HTML5Translator

import distribution


class slide_section(nodes.Element):
    '''
    nodes.section is not suited for this class because it must always
    have a title node as first child. However, a nodes.Element class does not
    have this restriction.
    '''
    pass


class slide_contents(nodes.Element):
    pass


class Slide(Directive):
    '''
    This directive creates a new slide_section node.
    The node doesn't need to be promoted to a document section because
    the SlideTransformer serializes all sections automatically.

    See test/cases.py for examples.

    All non-defined options that are defined in the declaration are automatically
    added as slide attributes such as :data-x:, :data-y: or :data-scale:
    '''
    final_argument_whitespace = True
    has_content = True
    option_spec = defaultdict(lambda: directives.unchanged, {
        'id': directives.unchanged,
        'class': directives.class_option,
        'title': directives.unchanged,
        'subtitle': directives.unchanged,
        'contents_class': directives.class_option,
    })

    def run(self):
        attrs = {key: value for key, value in self.options.iteritems()
                 if key not in ('class', 'title', 'subtitle', 'contents_class')}
        slide = slide_section(classes=self.options.get('class', []), **attrs)
        if 'title' in self.options:
            title = nodes.title(text=self.options.get('title', ''))
            slide.append(title)
            if 'subtitle' in self.options:
                subtitle = nodes.subtitle(text=self.options['subtitle'])
                slide.append(subtitle)
        content = slide_contents(classes=self.options.get('contents_class', []))
        self.state.nested_parse(self.content, self.content_offset, content)
        slide.append(content)
        return [slide]


class rst2html5slides_options(nodes.Element):
    '''
    node class that holds rst2html5slides options declared via rst2html5slides directive
    '''
    pass


class Rst2html5slides(Directive):
    '''
    Set rst2html5slides global options
    '''
    required_arguments = 0
    final_argument_whitespace = False
    has_content = False
    option_spec = {
        'container_id': directives.unchanged,
        'container_tag': directives.unchanged,
        'container_class': directives.class_option,
        'slide_tag': directives.unchanged,
        'slide_class': directives.class_option,
        'distribution': directives.unchanged,
        'incr_x': int,
        'incr_y': int,
        'distribution_parameter': int,
    }

    def run(self):
        return [rst2html5slides_options(**self.options)]


directives.register_directive('slide', Slide)
directives.register_directive('rst2html5slides', Rst2html5slides)


class SlideTransform(Transform):
    '''
    State Machine to transform default doctree to one with slideshow structure:
    section, header, contents.
    '''

    default_priority = 851

    # node classes that should be ignored to not form new slides
    skip_classes = (Meta.meta, rst2html5slides_options,)

    def apply(self):
        self.state = self.make_content
        self.contents = []
        self.contents_classes = []
        self.header = []
        self.children = []
        self.section = None
        self.curr_children = self.document.children
        self.document.clear()
        while self.curr_children:
            node = self.curr_children.pop(0)
            if isinstance(node, self.skip_classes):
                self.children.append(node)
                continue
            self.state(node)
        self.close_section()
        self.document.extend(self.children)

    def close_section(self):
        if not (self.contents or self.header):
            return
        if not self.section:
            self.section = nodes.section()
        if self.header:
            header = nodes.header()
            header.extend(self.header)
            self.section.append(header)
            self.header = []
        if self.contents:
            contents = slide_contents(classes=self.contents_classes)
            contents.extend(self.contents)
            self.contents = []
            self.contents_classes = []
            self.section.append(contents)
        self.children.append(self.section)
        return

    def check_subsection(self, node):
        '''
        Make the header of the slide
        '''
        if isinstance(node, nodes.section):  # subsection
            '''
            insert subsection in curr_children
            '''
            self.curr_children = node.children + self.curr_children
        else:
            self.state = self.make_content
            self.state(node)
        return

    def make_content(self, node):
        if isinstance(node, (nodes.transition, nodes.section, slide_section)):
            self.close_section()
            self.section = nodes.section()
            self.section.update_all_atts(node)
            self.curr_children = node.children + self.curr_children
        elif isinstance(node, (nodes.title, nodes.subtitle)):
            elem = nodes.subtitle() if len(self.header) else nodes.title()
            elem.update_all_atts(node)
            elem.extend(node.children)
            self.header.append(elem)
            self.state = self.check_subsection
        elif isinstance(node, slide_contents):
            self.contents_classes = node['classes']
            if node.children:
                self.contents = node.children
                self.close_section()
        else:
            self.contents.append(node)
        return


class SlideWriter(HTML5Writer):

    def __init__(self):
        HTML5Writer.__init__(self)
        self.translator_class = SlideTranslator

    def translate(self):
        self.parts['pseudoxml'] = self.document.pformat()  # get pseudoxml before HTML5.translate
        HTML5Writer.translate(self)

    def get_transforms(self):
        return HTML5Writer.get_transforms(self) + [SlideTransform]


class SlideTranslator(HTML5Translator):

    def __init__(self, *args):
        self.rst_terms['section'] = ('slide', 'visit_section', 'depart_section')
        self.rst_terms['slide_contents'] = ('section', 'default_visit', 'default_departure')
        self.rst_terms['slide_section'] = ('section', 'default_visit', 'default_departure')
        self.rst_terms['rst2html5slides_options'] = (None, 'visit_rst2html5slides_options', None)
        HTML5Translator.__init__(self, *args)
        self._reset()
        # self.metatags.append(tag.base(target="_blank"))
        return

    def _reset(self):
        self.container_id = None
        self.container_tag = 'deck'
        self.container_class = []
        self.slide_tag = 'slide'
        self.slide_class = []
        self.distribution = 'manual'
        self.incr_x = 1500
        self.incr_y = 800
        self.distribution_parameter = None
        return

    def parse(self, node):
        if node.__class__.__name__ == 'section':
            node['classes'].extend(self.slide_class)
        tag_name, indent, attrs = HTML5Translator.parse(self, node)
        if tag_name == 'slide':
            tag_name = self.slide_tag
        return tag_name, indent, attrs

    def visit_section(self, node):
        node['ids'] = ''
        self.heading_level += 1
        if self.heading_level == 1:
            self.default_visit(node)
        return

    def depart_section(self, node):
        self.heading_level -= 1
        if self.heading_level == 0:
            self.default_departure(node)
        return

    def depart_subtitle(self, node):
        HTML5Translator.depart_subtitle(self, node)
        self.heading_level += 1
        return

    def visit_rst2html5slides_options(self, node):
        self.container_id = node.get('container_id', self.container_id)
        self.container_tag = node.get('container_tag', self.container_tag)
        self.container_class = node.get('container_class', self.container_class)
        self.slide_tag = node.get('slide_tag', self.slide_tag)
        self.slide_class = node.get('slide_class', self.slide_class)
        self.distribution = node.get('distribution', self.distribution)
        self.incr_x = node.get('incr_x', self.incr_x)
        self.incr_y = node.get('incr_y', self.incr_y)
        self.distribution_parameter = node.get('distribution_parameter', self.distribution_parameter)
        raise nodes.SkipNode

    def _distribute_slides(self):
        '''
        Distribute slides spatially according to some predefined function.
        data-* attributes are used to keep the coordinates.
        '''
        if self.distribution == 'manual':
            return
        slides = [elem for item in self.context.stack[0] for elem in item if isinstance(elem, Element)]
        func = getattr(distribution, self.distribution)
        func(slides, self.incr_x, self.incr_y, self.distribution_parameter)
        return

    def depart_document(self, node):
        self._distribute_slides()
        if len(self.context.stack[0]):
            deck = getattr(tag, self.container_tag)(*self.context.stack[0], id=self.container_id)
            if self.container_class:
                deck(class_=' '.join(self.container_class))
            self.context.stack = ['\n', deck, '\n']
        # _reset is necessary to run the several test cases
        self._reset()
        return


def main():
    from docutils.core import publish_cmdline, default_description
    description = ('Translates a restructuredText document to a HTML5 slideshow.  ' +
                   default_description)
    publish_cmdline(writer=SlideWriter(), description=description)
    return


if __name__ == '__main__':
    main()
