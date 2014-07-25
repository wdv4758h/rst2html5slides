#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains test data to rst2html5slides in the form:
# case = {'rst': rst_text, 'out': expected_output, ...}

from __future__ import unicode_literals

simple_slides = {
    'rst': '''
Title 1
=======

* bullet

Title 2
=======

* bullet 2''',
    'out': '''
<deck>
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
</deck>
''',
    'part': 'body',
    'manual_slide_identification': True,
}


simple_slides_doctree = {
    'rst': simple_slides['rst'],
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


deck_slide_selector_parameters = {
    'rst': simple_slides['rst'],
    'deck_selector': 'div#impress.impress-not-supported',
    'slide_selector': 'div.step',
    'manual_slide_identification': True,
    'part': 'body',
    'out': '''
<div class="impress-not-supported" id="impress">
    <div class="step">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>bullet</li>
            </ul>
        </section>
    </div>
    <div class="step">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>bullet 2</li>
            </ul>
        </section>
    </div>
</div>
''',
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
<deck>
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
</deck>
''',
    'part': 'body',
    'manual_slide_identification': True,
}


slide_with_no_title = {
    'rst': '''
A slide with no title

----

slide 2. No title either.
The next one is an empty slide

----

..''',
    'part': 'body',
    'out': '''
<deck>
    <slide>
        <section>A slide with no title</section>
    </slide>
    <slide>
        <section>slide 2. No title either. The next one is an empty slide</section>
    </slide>
    <slide>
        <section></section>
    </slide>
</deck>
''',
}

slide_with_no_title_in_the_middle = {
    'rst': '''
Title 1
=======

paragraph

----

This should be a new slide

.. class:: special

----

This should also be a new slide

Title 2
=======
''',
    'part': 'body',
    'out': '''
<deck>
    <slide id="title-1">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>paragraph</section>
    </slide>
    <slide>
        <section>This should be a new slide</section>
    </slide>
    <slide class="special">
        <section>This should also be a new slide</section>
    </slide>
    <slide id="title-2">
        <header>
            <h1>Title 2</h1>
        </header>
    </slide>
</deck>
''',
}


slide_with_no_title_class = {
    'rst': '''
:slide_selector: .step
:class: test

first slide, no title.
The class directive doesn't work here.
You must use :literal:`:class:` or :literal:`:classes:` to set up the class of this slide.
Those are workarounds. No other solution at the time being.

.. class:: hint

----

the class directive works from the second slide onward

:classes: special

----

:literal:`classes` could also be used instead of :literal:`:class:`
''',
    'part': 'body',
    'out': '''
<deck>
    <slide class="test step">
        <section>first slide, no title. The class directive doesn't work here. You must use <code>:class:</code> or <code>:classes:</code> to set up the class of this slide. Those are workarounds. No other solution at the time being.</section>
    </slide>
    <slide class="hint step">
        <section>the class directive works from the second slide onward</section>
    </slide>
    <slide class="special step">
        <section><code>classes</code> could also be used instead of <code>:class:</code></section>
    </slide>
</deck>
''',
}


slide_without_content_1 = {
    'rst': '''
Title 1
=======

Title 2
=======''',
    'part': 'body',
    'out': '''
<deck>
    <slide id="title-1">
        <header>
            <h1>Title 1</h1>
        </header>
    </slide>
    <slide id="title-2">
        <header>
            <h1>Title 2</h1>
        </header>
    </slide>
</deck>
''',
}


slide_without_content_1_doctree = {
    'rst': slide_without_content_1['rst'],
    'part': 'pseudoxml',
    'out': '''<document source="<string>">
    <section ids="title-1" names="title\ 1">
        <header>
            <title>
                Title 1
    <section ids="title-2" names="title\ 2">
        <header>
            <title>
                Title 2
''',
}


slide_without_content_2 = {
    'rst': '''
Title 1
=======

Subtitle 1
----------

Title 2
=======

Subtitle 2
----------

Subsubtitle
^^^^^^^^^^^
''',
    'part': 'body',
    'out': '''
<deck>
    <slide id="title-1">
        <header>
            <h1>Title 1</h1>
            <h2>Subtitle 1</h2>
        </header>
    </slide>
    <slide id="title-2">
        <header>
            <h1>Title 2</h1>
            <h2>Subtitle 2</h2>
            <h3>Subsubtitle</h3>
        </header>
    </slide>
</deck>
''',
}


slide_without_content_2_doctree = {
    'rst': slide_without_content_2['rst'],
    'part': 'pseudoxml',
    'out': '''<document source="<string>">
    <section ids="title-1" names="title\ 1">
        <header>
            <title>
                Title 1
            <title>
                Subtitle 1
    <section ids="title-2" names="title\ 2">
        <header>
            <title>
                Title 2
            <title>
                Subtitle 2
            <title>
                Subsubtitle
''',
}


slide_contents_class = {
    'rst': '''
single paragraph. No <p> tag wrapping it.

----

.. class:: special

This paragraph won't be compacted because of its "special" class

----

.. container:: special

    This construction becomes a <div> section.

----

.. class:: hint

     * This also works
     * Substructure here''',
    'part': 'body',
    'manual_slide_identification': True,
    'out': '''
<deck>
    <slide>
        <section>single paragraph. No &lt;p&gt; tag wrapping it.</section>
    </slide>
    <slide>
        <section>
            <p class="special">This paragraph won't be compacted because of its "special" class</p>
        </section>
    </slide>
    <slide>
        <section>
            <div class="special">This construction becomes a &lt;div&gt; section.</div>
        </section>
    </slide>
    <slide>
        <section>
            <ul class="hint">
                <li>This also works</li>
                <li>Substructure here</li>
            </ul>
        </section>
    </slide>
</deck>
''',
}


single_slide_no_title = {
    'rst': '''paragraph

* bullet 1
* bullet 2''',
    'out': '''
<deck>
    <slide>
        <section>
            <p>paragraph</p>
            <ul>
                <li>bullet 1</li>
                <li>bullet 2</li>
            </ul>
        </section>
    </slide>
</deck>
''',
    'part': 'body',
}

single_slide_no_title_doctree = {
    'rst': single_slide_no_title['rst'],
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
<deck>
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
</deck>
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

h2 = {
    'rst': '''.. class:: segue dark nobackground

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
    'out': '''
<deck>
    <slide class="segue dark nobackground" id="title-1">
        <header>
            <h1>Title 1</h1>
            <h2>Subtitle</h2>
        </header>
        <section>
            <ul>
                <li>bullet</li>
            </ul>
        </section>
    </slide>
    <slide id="title-2">
        <header>
            <h1>Title 2</h1>
            <h2>Subtitle 2</h2>
        </header>
        <section>
            <ul>
                <li>bullet 2</li>
            </ul>
        </section>
    </slide>
</deck>
''',
    'part': 'body',
}

h2_doctree = {
    'rst': h2['rst'],
    'out': '''<document source="<string>">
    <section classes="segue dark nobackground" ids="title-1" names="title\ 1">
        <header>
            <title>
                Title 1
            <title>
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
            <title>
                Subtitle 2
        <slide_contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet 2
''',
    'part': 'pseudoxml',
}

# rst2html5slides doesn't allow three different heading levels at the same slide
h3 =  {
    'rst': '''There can't be three title levels at the first slide
because the first two are interpreted as document title / subtitle.
See http://docutils.sourceforge.net/docs/user/rst/quickstart.html#document-title-subtitle

----

Title 1
=======

Subtitle
--------

Subsubtitle
+++++++++++

* bullet
''',
    'out': '''
<deck>
    <slide>
        <section>There can't be three title levels at the first slide because the first two are \
interpreted as document title / subtitle. \
See <a href="http://docutils.sourceforge.net/docs/user/rst/quickstart.html#document-title-subtitle">\
http://docutils.sourceforge.net/docs/user/rst/quickstart.html#document-title-subtitle</a></section>
    </slide>
    <slide id="title-1">
        <header>
            <h1>Title 1</h1>
            <h2>Subtitle</h2>
            <h3>Subsubtitle</h3>
        </header>
        <section>
            <ul>
                <li>bullet</li>
            </ul>
        </section>
    </slide>
</deck>
''',
    'part': 'body',
}


h3_doctree =  {
    'rst': h3['rst'],
    'out': '''<document source="<string>">
    <section>
        <slide_contents>
            <paragraph>
                There can't be three title levels at the first slide
                because the first two are interpreted as document title / subtitle.
                See \n                \
<reference refuri="http://docutils.sourceforge.net/docs/user/rst/quickstart.html#document-title-subtitle">
                    http://docutils.sourceforge.net/docs/user/rst/quickstart.html#document-title-subtitle
    <section ids="title-1" names="title\ 1">
        <header>
            <title>
                Title 1
            <title>
                Subtitle
            <title>
                Subsubtitle
        <slide_contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet
''',
    'part': 'pseudoxml',
}


transition_to_section = {
    'rst': '''paragraph

----

* bullet''',
    'out': '''
<deck>
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
</deck>
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

transition_2_doctree = {
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

# it is not possible to have an initial empty slide
empty_slide = {
    'rst': '''Title
=====

paragraph

----

..''',
    'out': '''
<deck>
    <slide>
        <header>
            <h1>Title</h1>
        </header>
        <section>paragraph</section>
    </slide>
    <slide>
        <section></section>
    </slide>
</deck>
''',
    'part': 'body',
}


empty_slide_pseudoxml = {
    'rst': empty_slide['rst'],
    'out': '''<document ids="title" names="title" source="<string>" title="Title">
    <section>
        <header>
            <title>
                Title
        <slide_contents>
            <paragraph>
                paragraph
    <section>
        <slide_contents>
            <comment xml:space="preserve">
''',
    'part': 'pseudoxml',
}

meta_tag = {
    'rst': '''.. meta::
    :author: André Felipe Dias
    :http-equiv=X-UA-Compatible: chrome=1
''',
    'out': '''
    <meta charset="utf-8" />
    <meta content="André Felipe Dias" name="author" />
    <meta content="chrome=1" http-equiv="X-UA-Compatible" />
    <link href="impress.css" rel="stylesheet" />
    <script src="http://code.jquery.com/jquery-latest.min.js"></script>
    <script src="impress.css"></script>
''',
    'part': 'head',
    'script': [
        ('http://code.jquery.com/jquery-latest.min.js', None),
        ('impress.css', None),
    ],
    'stylesheet': ('impress.css',),
}

meta_tag2 = {
    'rst': meta_tag['rst'],
    'out': '',
    'part': 'body',
}

meta_tag_and_slides = {
    'rst': '''.. meta::
    :viewport: width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes

Title 1
=======

* item''',
    'part': 'pseudoxml',
    'out': '''<document ids="title-1" names="title\ 1" source="<string>" title="Title 1">
    <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport">
    <section>
        <header>
            <title>
                Title 1
        <slide_contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        item
''',
}

_five_slides = '''Title 1
=======

* Bullet

Title 2
=======

* Bullet

Title 3
=======

* Bullet

Title 4
=======

* Bullet

Title 5
=======

* Bullet
'''

linear = {
    'rst': ''':distribution: linear

''' + _five_slides,
    'part': 'body',
    'manual_slide_identification': True,
    'out': '''
<deck>
    <slide data-x="0">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-x="1600">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-x="3200">
        <header>
            <h1>Title 3</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-x="4800">
        <header>
            <h1>Title 4</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-x="6400">
        <header>
            <h1>Title 5</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
</deck>
''',
}


linear_parameter = {
    'rst': _five_slides,
    'part': 'body',
    'manual_slide_identification': True,
    'distribution': 'linear',
    'out': linear['out'],
}


square = {
    'rst': ''':distribution: square 2

''' + _five_slides,
    'part': 'body',
    'manual_slide_identification': True,
    'out': '''
<deck>
    <slide data-x="0">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-x="1600">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-y="1600" data-x="0">
        <header>
            <h1>Title 3</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-y="1600" data-x="1600">
        <header>
            <h1>Title 4</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-y="3200" data-x="0">
        <header>
            <h1>Title 5</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
</deck>
''',
}


square_parameter = {
    'rst': _five_slides,
    'part': 'body',
    'manual_slide_identification': True,
    'distribution': 'square 2',
    'out': square['out']
}


square_rotate = {
    'rst': ''':distribution: square_rotate 2

''' + _five_slides,
    'part': 'body',
    'manual_slide_identification': True,
    'out': '''
<deck>
    <slide data-x="0" data-rotate-z="0">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-x="1600" data-rotate-z="0">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-y="1600" data-x="1600" data-rotate-z="179.9">
        <header>
            <h1>Title 3</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-y="1600" data-x="0" data-rotate-z="179.9">
        <header>
            <h1>Title 4</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-y="3200" data-x="0" data-rotate-z="0.0">
        <header>
            <h1>Title 5</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
</deck>
''',
}

change_distribution_linear = {
    'rst': ''':distribution: linear

slide 1

:data-x: -2000
:data-y: -1000
:data-scale: -3
:data-rotate-z: 45

----

slide 2

----

slide 3

''',
    'part': 'body',
    'out': '''
<deck>
    <slide data-x="0">
        <section>slide 1</section>
    </slide>
    <slide data-y="-1000" data-x="-2000" data-rotate-z="45" data-scale="-3">
        <section>slide 2</section>
    </slide>
    <slide data-y="-1000" data-x="-400" data-rotate-z="45" data-scale="-3">
        <section>slide 3</section>
    </slide>
</deck>
''',
}


change_distribution_square = {
    'rst': ''':distribution: square 2

slide 1

:data-x: -2000
:data-y: -1000
:data-scale: -3
:data-rotate-z: 45

----

slide 2

----

slide 3

----

slide 4
''',
    'part': 'body',
    'out': '''
<deck>
    <slide data-x="0">
        <section>slide 1</section>
    </slide>
    <slide data-y="-1000" data-x="-2000" data-rotate-z="45" data-scale="-3">
        <section>slide 2</section>
    </slide>
    <slide data-y="-1000" data-x="-400" data-rotate-z="45" data-scale="-3">
        <section>slide 3</section>
    </slide>
    <slide data-y="600" data-x="-2000" data-rotate-z="45" data-scale="-3">
        <section>slide 4</section>
    </slide>
</deck>
''',
}

change_distribution_func = {
    'rst': ''':distribution: linear

slide 1

----

slide 2

----

slide 3

:distribution: square 1

----

slide 4

----

slide 5
''',
    'part': 'body',
    'out': '''
<deck>
    <slide data-x="0">
        <section>slide 1</section>
    </slide>
    <slide data-x="1600">
        <section>slide 2</section>
    </slide>
    <slide data-x="3200">
        <section>slide 3</section>
    </slide>
    <slide data-y="1600" data-x="3200">
        <section>slide 4</section>
    </slide>
    <slide data-y="3200" data-x="3200">
        <section>slide 5</section>
    </slide>
</deck>
''',
}

deck_slide_selectors  = {
    'rst': ''':deck_selector: div.deck_container
:slide_selector: article.slide

Welcome

Title 1
=======

* Bullet

:deck_selector: deck#impress
:slide_selector: div.step

Title 2
=======

* Bullet''',
    'part': 'body',
    'out': '''
<deck class="deck_container" id="impress">
    <article class="slide">
        <section>Welcome</section>
    </article>
    <div class="step" id="title-1">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </div>
    <div class="step" id="title-2">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </div>
</deck>
''',
}

deck_slide_selectors_2  = {
    'rst': ''':deck_selector: div.deck-container
:slide_selector: article.slide

:id: opening
:class: cover
:data-x: -1000
:data-y: -500
:data-scale: 5

Welcome


:data-rotate-x: 180

Title 1
=======

* Bullet

:data-y: -1500
:data-rotate-z: 180
:data-scale: 7

----

* Bullet

:data-rotate-x: 0
:data-x: 0

Title 3
=======

* Bullet
''',
    'part': 'body',
    'out': '''
<div class="deck-container">
    <article data-y="-500" data-x="-1000" class="cover slide" id="opening" data-scale="5">
        <section>Welcome</section>
    </article>
    <article class="slide" data-y="-500" data-x="-1000" data-rotate-x="180" data-scale="5" \
id="title-1">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </article>
    <article data-scale="7" data-y="-1500" data-x="-1000" data-rotate-z="180" data-rotate-x="180" \
class="slide">
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </article>
    <article data-scale="7" data-y="-1500" data-x="0" data-rotate-z="180" data-rotate-x="0" \
id="title-3" class="slide">
        <header>
            <h1>Title 3</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </article>
</div>
''',
}


manual_slide_identification = {
    'rst': '''
:id: benvindo

Welcome

:id: introducao

Title 1
=======

Title 2
=======

paragraph

----

About
''',
    'part': 'body',
    'manual_slide_identification': True,
    'out': '''
<deck>
    <slide id="benvindo">
        <section>Welcome</section>
    </slide>
    <slide id="introducao">
        <header>
            <h1>Title 1</h1>
        </header>
    </slide>
    <slide>
        <header>
            <h1>Title 2</h1>
        </header>
        <section>paragraph</section>
    </slide>
    <slide>
        <section>About</section>
    </slide>
</deck>
''',
}


automatic_slide_identification = {
    'rst': manual_slide_identification['rst'],
    'part': 'body',
    'out': '''
<deck>
    <slide id="benvindo">
        <section>Welcome</section>
    </slide>
    <slide id="introducao">
        <header>
            <h1>Title 1</h1>
        </header>
    </slide>
    <slide id="title-2">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>paragraph</section>
    </slide>
    <slide>
        <section>About</section>
    </slide>
</deck>
''',
}


case_1 = {
    'rst': '''.. meta::
    :http-equiv=X-UA-Compatible: chrome=1:
    :viewport: width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes

:deck_selector: div#impress
:slide_selector: div.step

Title
=====

Text

.. class:: special

Title 2
=======

Another line''',
    'part': 'whole',
    'out': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta content="chrome=1:" http-equiv="X-UA-Compatible" />
    <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport" />
</head>
<body>
<div id="impress">
    <div class="step" id="title">
        <header>
            <h1>Title</h1>
        </header>
        <section>Text</section>
    </div>
    <div class="special step" id="title-2">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>Another line</section>
    </div>
</div>
</body>
</html>''',
}

case_1_pseudoxml = {
    'rst': case_1['rst'],
    'part': 'pseudoxml',
    'out': '''<document source="<string>">
    <docinfo>
        <field>
            <field_name>
                deck_selector
            <field_body>
                <paragraph>
                    div#impress
        <field>
            <field_name>
                slide_selector
            <field_body>
                <paragraph>
                    div.step
    <meta content="chrome=1:" http-equiv="X-UA-Compatible">
    <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport">
    <section ids="title" names="title">
        <header>
            <title>
                Title
        <slide_contents>
            <paragraph>
                Text
    <section classes="special" ids="title-2" names="title\ 2">
        <header>
            <title>
                Title 2
        <slide_contents>
            <paragraph>
                Another line
''',
}

# do use this way
data_before_transition = {
    'rst': ''':data-x: 100

slide 1

:data-x: 200

----

slide 2''',
    'part': 'body',
    'out': '''
<deck>
    <slide data-x="100">
        <section>slide 1</section>
    </slide>
    <slide data-x="200">
        <section>slide 2</section>
    </slide>
</deck>
''',
}


# slide attributes within the slide
# will be used in the next slide
data_after_transition = {
    'rst': ''':data-x: 100

slide 1

----

:data-x: 200

slide 2''',
    'part': 'body',
    'out': '''
<deck>
    <slide data-x="100">
        <section>slide 1</section>
    </slide>
    <slide data-x="100">
        <section>slide 2</section>
    </slide>
</deck>
''',
}


data_title = {
    'rst': ''':data-x: 100

Title 1
=======

slide 1

:data-x: 200

Title 2
=======

slide 2''',
    'part': 'body',
    'out': '''
<deck>
    <slide data-x="100" id="title-1">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>slide 1</section>
    </slide>
    <slide data-x="200" id="title-2">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>slide 2</section>
    </slide>
</deck>
''',
}

data_title_doctree = {
    'rst': ''':data-x: 100

Title 1
=======

slide 1

:data-x: 200

Title 2
=======

slide 2''',
    'part': 'pseudoxml',
    'out': '''<document source="<string>">
    <docinfo>
        <field>
            <field_name>
                data-x
            <field_body>
                <paragraph>
                    100
    <section ids="title-1" names="title\ 1">
        <header>
            <title>
                Title 1
        <slide_contents>
            <paragraph>
                slide 1
            <field_list>
                <field>
                    <field_name>
                        data-x
                    <field_body>
                        <paragraph>
                            200
    <section ids="title-2" names="title\ 2">
        <header>
            <title>
                Title 2
        <slide_contents>
            <paragraph>
                slide 2
''',
}


internal_link = {
    'rst': '''

.. warning::

    :literal:`id` fields mess up with internal links.

:id: another-id

Title 1
=======

paragraph

Title 2
=======

link to `Title 1`_
''',
    'part': 'body',
    'out': '''
<deck>
    <slide>
        <section>
            <aside class="warning"><code>id</code> fields mess up with internal links.</aside>
        </section>
    </slide>
    <slide id="another-id">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>paragraph</section>
    </slide>
    <slide id="title-2">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>link to <a href="#title-1">Title 1</a></section>
    </slide>
</deck>
''',
}

