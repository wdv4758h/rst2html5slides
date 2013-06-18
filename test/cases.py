#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains test data to rst2slideshow in the form:
# case = {'rst': rst_text, 'out': expected_output, ...}

from __future__ import unicode_literals


slides = {
    'rst': '''
Title 1
=======

* bullet

Title 2
=======

* bullet 2''',
    'out': '''
<slides class="layout-widescreen">
    <slide>
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>bullet</li>
            </ul>
        </section>
    </slide>
    <slide>
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>bullet 2</li>
            </ul>
        </section>
    </slide>
</slides>
''',
    'part': 'body',
}

slide_class = {
    'rst': '''
.. class:: segue dark nobackground

Title 1
=======

* bullet

Title 2
=======

.. class:: build fade

    * bullet 2
''',
    'out': '''
<slides class="layout-widescreen">
    <slide class="segue dark nobackground">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>bullet</li>
            </ul>
        </section>
    </slide>
    <slide>
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul class="build fade">
                <li>bullet 2</li>
            </ul>
        </section>
    </slide>
</slides>
''',
    'part': 'body',
}


lose_nodes = {
    'rst': '''paragraph

* bullet 1
* bullet 2''',
    'out': '''
<slides class="layout-widescreen">
    <slide>
        <section>
            <p>paragraph</p>
            <ul>
                <li>bullet 1</li>
                <li>bullet 2</li>
            </ul>
        </section>
    </slide>
</slides>
''',
    'part': 'body',
}


lose_nodes_doctree = {
    'rst': lose_nodes['rst'],
    'out': '''<document source="<string>">
    <section>
        <slide_contents>
            <paragraph>
                paragraph
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet 1
                <list_item>
                    <paragraph>
                        bullet 2
''',
    'part': 'pseudoxml',
}


single_slide = {
    'rst': '''
Title 1
=======

* bullet''',
    'out': '''
<slides class="layout-widescreen">
    <slide>
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>bullet</li>
            </ul>
        </section>
    </slide>
</slides>
''',
    'part': 'body',
}


single_slide_doctree = {
    'rst': single_slide['rst'],
    'out': '''<document ids="title-1" names="title\ 1" source="<string>" \
title="Title 1">
    <section>
        <header>
            <title>
                Title 1
        <slide_contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet
''',
    'part': 'pseudoxml',
}


simple_case = {
    'rst': '''
Title 1
=======

* bullet

Title 2
=======

* bullet 2''',
    'out': '''<document source="<string>">
    <section ids="title-1" names="title\ 1">
        <header>
            <title>
                Title 1
        <slide_contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet
    <section ids="title-2" names="title\ 2">
        <header>
            <title>
                Title 2
        <slide_contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet 2
''',
    'part': 'pseudoxml',
}


subsection = {
    'rst': '''
.. class:: segue dark nobackground

Title 1
=======

Subtitle
--------

* bullet

Title 2
=======

Subtitle 2
----------

* bullet 2
''',
    'out': '''<document source="<string>">
    <section classes="segue dark nobackground" ids="title-1" names="title\ 1">
        <header>
            <title>
                Title 1
            <subtitle>
                Subtitle
        <slide_contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet
    <section ids="title-2" names="title\ 2">
        <header>
            <title>
                Title 2
            <subtitle>
                Subtitle 2
        <slide_contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet 2
''',
    'part': 'pseudoxml',
}


transition_to_section = {
    'rst': '''paragraph

----

* bullet''',
    'out': '''
<slides class="layout-widescreen">
    <slide>
        <section>paragraph</section>
    </slide>
    <slide>
        <section>
            <ul>
                <li>bullet</li>
            </ul>
        </section>
    </slide>
</slides>
''',
    'part': 'body',
}


transition_to_section_doctree = {
    'rst': transition_to_section['rst'],
    'out': '''<document source="<string>">
    <section>
        <slide_contents>
            <paragraph>
                paragraph
    <section>
        <slide_contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet
''',
    'part': 'pseudoxml',
}


transition_2 = {
    'rst': '''Title
=====

paragraph

----

another slide''',
    'out': '''<document ids="title" names="title" source="<string>" \
title="Title">
    <section>
        <header>
            <title>
                Title
        <slide_contents>
            <paragraph>
                paragraph
    <section>
        <slide_contents>
            <paragraph>
                another slide
''',
    'part': 'pseudoxml',
}

transition_3 = {
    'rst': '''Title
=====

paragraph

----

another slide

Title 2
=======

slide 3''',
    'out': '''<document source="<string>">
    <section ids="title" names="title">
        <header>
            <title>
                Title
        <slide_contents>
            <paragraph>
                paragraph
    <section>
        <slide_contents>
            <paragraph>
                another slide
    <section ids="title-2" names="title\ 2">
        <header>
            <title>
                Title 2
        <slide_contents>
            <paragraph>
                slide 3
''',
    'part': 'pseudoxml',
}

transition_with_class = {
    'rst': '''Title
=====

paragraph

.. class:: special

----

another slide

Title 2
=======

slide 3''',
    'out': '''<document source="<string>">
    <section ids="title" names="title">
        <header>
            <title>
                Title
        <slide_contents>
            <paragraph>
                paragraph
    <section classes="special">
        <slide_contents>
            <paragraph>
                another slide
    <section ids="title-2" names="title\ 2">
        <header>
            <title>
                Title 2
        <slide_contents>
            <paragraph>
                slide 3
''',
    'part': 'pseudoxml',
}

slide_directive_1 = {
    'rst': '''.. slide::

    paragraph''',
    'out': '''<document source="<string>">
    <section>
        <slide_contents>
            <paragraph>
                paragraph
''',
    'part': 'pseudoxml',
}


slide_directive_1_slideshow = {
    'rst': slide_directive_1['rst'],
    'out': '''
<slides class="layout-widescreen">
    <slide>
        <section>paragraph</section>
    </slide>
</slides>
''',
    'part': 'body',
}

slide_directive_2 = {
    'rst': '''.. slide::
    :class: special
    :title: Teste 1
    :subtitle: Subtitle

    paragraph''',
    'out': '''<document source="<string>">
    <section classes="special">
        <header>
            <title>
                Teste 1
            <subtitle>
                Subtitle
        <slide_contents>
            <paragraph>
                paragraph
''',
    'part': 'pseudoxml',
}


slide_directive_2_slideshow = {
    'rst': slide_directive_2['rst'],
    'out': '''
<slides class="layout-widescreen">
    <slide class="special">
        <header>
            <h1>Teste 1</h1>
            <h2>Subtitle</h2>
        </header>
        <section>paragraph</section>
    </slide>
</slides>
''',
    'part': 'body',
}


slide_directive_3 = {
    'rst': '''.. slide::
    :class: special
    :title: Teste 1
    :subtitle: Subtitle
    :contents_class: flexbox vcenter

    paragraph''',
    'out': '''<document source="<string>">
    <section classes="special">
        <header>
            <title>
                Teste 1
            <subtitle>
                Subtitle
        <slide_contents classes="flexbox vcenter">
            <paragraph>
                paragraph
''',
    'part': 'pseudoxml',
}

slide_directive_3_slideshow = {
    'rst': slide_directive_3['rst'],
    'out': '''
<slides class="layout-widescreen">
    <slide class="special">
        <header>
            <h1>Teste 1</h1>
            <h2>Subtitle</h2>
        </header>
        <section class="flexbox vcenter">paragraph</section>
    </slide>
</slides>
''',
    'part': 'body',
}

slide_directive_4 = {
    'rst': '''.. slide::
    :class: segue dark quote nobackground
    :contents_class: flexbox vleft auto-fadein

.. epigraph::

    This is an
    example of quote text.''',
    'out': '''<document source="<string>">
    <section classes="segue dark quote nobackground">
        <slide_contents classes="flexbox vleft auto-fadein">
            <block_quote classes="epigraph">
                <paragraph>
                    This is an
                    example of quote text.
''',
    'part': 'pseudoxml',
}

slide_directive_4_slideshow = {
    'rst': slide_directive_4['rst'],
    'out': '''
<slides class="layout-widescreen">
    <slide class="segue dark quote nobackground">
        <section class="flexbox vleft auto-fadein">
            <blockquote class="epigraph">
                <p>This is an example of quote text.</p>
            </blockquote>
        </section>
    </slide>
</slides>
''',
    'part': 'body',
}

slide_directive_5 = {
    'rst': '''.. slide::
    :class: special
    :title: Code Slide (Smaller Font)
    :contents_class: smaller

.. code-block:: javascript

    function helloWorld(world) {
        alert('Hello ' + String(world));
    }''',
    'out': '''
<slides class="layout-widescreen">
    <slide class="special">
        <header>
            <h1>Code Slide (Smaller Font)</h1>
        </header>
        <section class="smaller">
            <pre><code class="javascript"><span class="kd">function</span> \
<span class="nx">helloWorld</span><span class="p">(</span><span class="nx">\
world</span><span class="p">)</span> <span class="p">{</span>
    <span class="nx">alert</span><span class="p">(</span>\
<span class="s1">'Hello '</span> <span class="o">+</span> \
<span class="nb">String</span><span class="p">(</span><span class="nx">\
world</span><span class="p">));</span>
<span class="p">}</span></code></pre>
        </section>
    </slide>
</slides>
''',
    'part': 'body',
}

slide_directive_in_the_middle = {
    'rst': '''Title
=====

paragraph 1

.. slide::
    :class: special
    :title: Teste 1
    :subtitle: Subtitle

    paragraph''',
    'out': '''<document ids="title" names="title" source="<string>" \
title="Title">
    <section>
        <header>
            <title>
                Title
        <slide_contents>
            <paragraph>
                paragraph 1
    <section classes="special">
        <header>
            <title>
                Teste 1
            <subtitle>
                Subtitle
        <slide_contents>
            <paragraph>
                paragraph
''',
    'part': 'pseudoxml',
}

everything_together = {
    'rst': '''
Title
=====

some test

-----

slide without title

.. slide::
    :title: Slide
    :subtitle: Directive

    slide_contents
''',
    'out': '''<document ids="title" names="title" source="<string>" title="Title">
    <section>
        <header>
            <title>
                Title
        <slide_contents>
            <paragraph>
                some test
    <section>
        <slide_contents>
            <paragraph>
                slide without title
    <section>
        <header>
            <title>
                Slide
            <subtitle>
                Directive
        <slide_contents>
            <paragraph>
                slide_contents
''',
    'part': 'pseudoxml',
}

empty_slides = {
    'rst': '''.. slide::
    :class: special

..

----

..

Title
=====

paragraph''',
    'out': '''
<slides class="layout-widescreen">
    <slide class="special">
        <section></section>
    </slide>
    <slide>
        <section></section>
    </slide>
    <slide>
        <header>
            <h1>Title</h1>
        </header>
        <section>paragraph</section>
    </slide>
</slides>
''',
    'part': 'body',
}


empty_slides_pseudoxml = {
    'rst': empty_slides['rst'],
    'out': '''<document source="<string>">
    <section classes="special">
        <slide_contents>
            <comment xml:space="preserve">
    <section>
        <slide_contents>
            <comment xml:space="preserve">
    <section ids="title" names="title">
        <header>
            <title>
                Title
        <slide_contents>
            <paragraph>
                paragraph
''',
    'part': 'pseudoxml',
}
