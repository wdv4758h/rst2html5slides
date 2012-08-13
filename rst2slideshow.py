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


class contents(nodes.container): pass

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

        def adjust_section(section):
            terms = section.children
            section.clear()
            headings = []
            if isinstance(terms[0], nodes.title):
                headings.append(terms.pop(0))
                if len(terms) and isinstance(terms[0], nodes.section):
                    '''
                    Title             title
                    =====             section
                                         title
                    Subtitle                ...
                    --------             contents...

                    contents
                    '''
                    subsection = terms.pop()[0].traverse(descend=0, siblings=1)
                    subsection_title = subsection.pop(0)
                    subtitle = nodes.subtitle()
                    subtitle.update_basic_atts(subsection_title)
                    subtitle.extend(subsection_title.children)
                    headings.append(subtitle)
                    terms.extend(subsection)
                header = nodes.header()
                header.extend(headings)
                section.append(header)
            _contents = contents()
            _contents.extend(terms)
            section.append(_contents)
            return

        children = document.children
        document.clear()
        group = []
        while children or group:
            child = children.pop(0) if children else None
            if child and not isinstance(child, nodes.section):
                group.append(child)
            elif group:
                forced_section = nodes.section()
                forced_section.extend(group)
                group = []
                children.insert(0, forced_section)
            else:
                adjust_section(child)
                document.append(child)

        return document

class SlideShowTranslator(HTML5Translator):

    def __init__(self, *args):
        self.rst_terms['section'] = ('slide', 'visit_section', 'depart_section')
        self.rst_terms['contents'] = ('section', 'default_visit', 'default_departure')
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