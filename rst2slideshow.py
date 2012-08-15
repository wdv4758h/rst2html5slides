#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: André Felipe Dias <andref.dias@pronus.eng.br>

from __future__ import unicode_literals

"""
Translates a restructuredText document to a HTML5 slideshow
"""

__docformat__ = 'reStructuredText'

from docutils import nodes, frontend
from docutils.core import publish_from_doctree
from genshi.builder import tag
from rst2html5 import HTML5Writer, HTML5Translator


class slide_contents(nodes.section): pass


class SlideShowTransformer(object):
    '''
    State Machine to transform default doctree to one with slideshow structure:
    section, header, hgroup, contents.
    '''

    def transform(self, document):
        self.state = self.make_content
        self.contents = []
        self.header = []
        self.children = []
        self.section = None
        self.curr_children = document.children
        document.clear()

        # import pdb
        # pdb.set_trace()

        while self.curr_children:
            node = self.curr_children.pop(0)
            self.state(node)
        self.close_section()
        document.extend(self.children)
        return document

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
        Make the header of the slide. If more than one title is found, there will be a hgroup
        '''
        if isinstance(node, nodes.section): # subsection
            '''
            insert subsection in curr_children
            '''
            self.curr_children = node.children + self.curr_children
        else:
            self.state = self.make_content
            self.state(node)
        return

    def make_content(self, node):
        if isinstance(node, (nodes.transition, nodes.section)):
            self.close_section()
            self.section = nodes.section()
            self.section.update_basic_atts(node)
            self.curr_children = node.children + self.curr_children
        elif isinstance(node, (nodes.title, nodes.subtitle)):
            elem = nodes.subtitle() if len(self.header) else nodes.title()
            elem.update_basic_atts(node)
            elem.extend(node.children)
            self.header.append(elem)
            self.state = self.check_subsection
        else:
            self.contents.append(node)
        return



class SlideShowWriter(HTML5Writer):

    def __init__(self):
        HTML5Writer.__init__(self)
        self.translator_class = SlideShowTranslator

    def translate(self):
        self.transform_doctree(self.document)
        if not self.document.settings.debug:
            HTML5Writer.translate(self)
            self.pseudoxml = ''
        else:
            self.pseudoxml = self.output = publish_from_doctree(self.document)
            self.head = self.body = ''
        return

    def assemble_parts(self):
        HTML5Writer.assemble_parts(self)
        self.parts['pseudoxml'] = self.pseudoxml
        return

    @classmethod
    def transform_doctree(cls, document):
        transformer = SlideShowTransformer()
        return transformer.transform(document)

class SlideShowTranslator(HTML5Translator):

    def __init__(self, *args):
        self.rst_terms['section'] = ('slide', 'visit_section', 'depart_section')
        self.rst_terms['slide_contents'] = ('section', 'default_visit', 'default_departure')
        self.rst_terms['hgroup'] = (None, 'default_visit', 'default_departure')
        HTML5Translator.__init__(self, *args)
        self.head.append(tag.meta(**{'http-equiv':"X-UA-Compatible", 'content':"chrome=1"}))
        self.head.append(tag.base(target="_blank"))
        # incluir links para stylesheets
        # incluir scripts

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

    def depart_document(self, node):
        slides = tag.slides(*self.context.stack[0], class_="layout-widescreen")
        self.context.stack = ['\n', slides, '\n']
        return

def main():
    from docutils.core import publish_cmdline, default_description

    description = ('Translates a restructuredText document to a HTML5 slideshow.  ' +
                    default_description)
    publish_cmdline(writer=SlideShowWriter(), description=description)
    return


if __name__ == '__main__':
    main()