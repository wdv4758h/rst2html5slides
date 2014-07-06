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


class AnyOptionsDict(dict):
    '''
    This dict subclass is supposed to be used as a option_spec attribute
    to allow the directive to receive any number of options,
    with some of them defined previously
    '''
    def __getitem__(self, key):
        try:
            item = dict.__getitem__(self, key)
        except KeyError:
            item = directives.unchanged
        return item


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
    option_spec = AnyOptionsDict({
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


directives.register_directive('slide', Slide)
directives.register_directive('slides_distribution', distribution.Distribution)


class SlideTransform(Transform):
    '''
    State Machine to transform default doctree to one with slideshow structure:
    section, header, contents.
    '''

    default_priority = 851

    skip_classes = (Meta.meta,)

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

    slide_script_init = '''\n<script>
$(function() {
    $('deck').jmpress({
        stepSelector: 'slide'
    });
});
</script>\n'''

    default_template = '<!DOCTYPE html>\n<html{html_attr}>\n' \
                       '<head>{head}</head>\n<body>{body}{script}</body>\n</html>'

    def __init__(self, *args):
        self.rst_terms['section'] = ('slide', 'visit_section', 'depart_section')
        self.rst_terms['slide_contents'] = ('section', 'default_visit', 'default_departure')
        self.rst_terms['slide_section'] = ('section', 'default_visit', 'default_departure')
        HTML5Translator.__init__(self, *args)
        self.metatags.append(tag.base(target="_blank"))
        return

    def _get_template_values(self):
        result = HTML5Translator._get_template_values(self)
        result['script'] = self.slide_script_init
        return result

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

    def _distribute_slides_jmpress(self):
        slides = [elem for item in self.context.stack[0] for elem in item if isinstance(elem, Element)]
        func_name = distribution.Distribution.slides_distribution
        parameter = distribution.Distribution.opts.get('parameter', None)
        func = getattr(distribution, func_name)
        func(slides, parameter)
        distribution.Distribution.reset()

    def depart_document(self, node):
        self._distribute_slides_jmpress()
        if len(self.context.stack[0]):
            deck = tag.deck(*self.context.stack[0])
            self.context.stack = ['\n', deck, '\n']
        return


def main():
    from docutils.core import publish_cmdline, default_description
    description = ('Translates a restructuredText document to a HTML5 slideshow.  ' +
                   default_description)
    publish_cmdline(writer=SlideWriter(), description=description)
    return


if __name__ == '__main__':
    main()
