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
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives.html import MetaBody as Meta
from genshi.builder import tag, Element
from rst2html5 import HTML5Writer, HTML5Translator

import re


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
        self.state = self.make_content
        self.contents = []
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
            contents = slide_contents()
            contents.extend(self.contents)
            self.contents = []
            self.section.append(contents)
        self.children.append(self.section)
        return

    def check_subsection(self, node):
        '''
        Make the header of the slide
        '''
        if isinstance(node, nodes.section):  # subsection
            # insert subsection in curr_children
            self.curr_children = node.children + self.curr_children
        else:
            self.state = self.make_content
            self.state(node)
        return

    def make_content(self, node):
        if isinstance(node, (nodes.transition, nodes.section)):
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
        elif isinstance(node, slide_contents) and node.children:
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

    tag_name_re = re.compile('^\w+')
    class_re = re.compile('\.([\w\-]+)')
    id_re = re.compile('#([\w|\-]+)')

    def __init__(self, *args):
        self.rst_terms['section'] = ['slide', 'visit_section', 'depart_section']  # [0] might be replaced later
        self.rst_terms['slide_contents'] = ('section', 'default_visit', 'default_departure')
        HTML5Translator.__init__(self, *args)
        self._reset()
        # self.metatags.append(tag.base(target="_blank"))
        return

    def _compacted_paragraph(self, node):
        '''
        a single node followed by a single field list should also be compacted
        '''
        parent_length = len([n for n in node.parent
                             if not isinstance(n, (nodes.field_list))])
        return HTML5Translator._compacted_paragraph(self, node) or parent_length == 1

    def visit_section(self, node):
        node['ids'] = ''
        node.attributes.update(self.slide_attributes)
        self.slide_attributes = {}
        self.heading_level += 1
        if self.heading_level == 1:
            self.default_visit(node)
        return

    def depart_section(self, node):
        self.heading_level -= 1
        if self.heading_level == 0:
            # here it is a less intrusive way to add any default class to a slide
            if 'class' in self.slide:
                node['classes'].extend([self.slide['class']])
            self.default_departure(node)
        return

    def depart_subtitle(self, node):
        HTML5Translator.depart_subtitle(self, node)
        self.heading_level += 1
        return

    def depart_document(self, node):
        self._distribute_slides()
        if len(self.context.stack[0]):
            deck = getattr(tag, self.container['tag'])(
                    *self.context.stack[0],
                    id=self.container.get('id', None),
                    class_=self.container.get('class', None)
            )
            self.context.stack = ['\n', deck, '\n']
        # _reset is necessary to run the several test cases
        self._reset()
        return

    def _reset(self):
        self.container = {'tag':'deck'}
        self.slide = {'tag':'slide'}
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

    def visit_field_container(self, value):
        tag_name = self.tag_name_re.findall(value)
        id = self.id_re.findall(value)
        class_ = self.class_re.findall(value)
        if tag_name:
            self.container['tag'] = tag_name[0]
        if id:
            self.container['id'] = id[0]
        if class_:
            self.container['class'] = class_[0]
        return

    def visit_field_slide(self, value):
        tag_name = self.tag_name_re.findall(value)
        class_ = self.class_re.findall(value)
        if tag_name:
            self.rst_terms['section'][0] = tag_name[0]
        if class_:
            self.slide['class'] = class_[0]
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
