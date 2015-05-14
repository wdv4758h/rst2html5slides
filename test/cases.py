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
    'distribution': None,
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
.. presentation::
    :slide-selector: .step

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
        <section>first slide, no title. The class directive doesn't work here. You must use \
<code>:class:</code> or <code>:classes:</code> to set up the class of this slide. \
Those are workarounds. No other solution at the time being.</section>
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
    'distribution': None,
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
h3 = {
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


h3_doctree = {
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
    'distribution': 'linear',
    'out': '''
<deck>
    <slide data-x="0">
        <header>
            <h1>Title</h1>
        </header>
        <section>paragraph</section>
    </slide>
    <slide data-x="1600">
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
    <meta generator="rst2html5slides" />
    <meta generator-homepage="https://pypi.python.org/pypi/rst2html5slides" />
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
    'rst': '''
.. presentation::
    :distribution: linear

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


presentation_attributes_via_command_parameters = {
    'rst': _five_slides,
    'part': 'body',
    'manual_slide_identification': True,
    'distribution': 'grid_rotate 2',
    'deck_selector': 'div#impress.impress-not-supported',
    'slide_selector': 'div.step',
    'increment': '1000 800',
    'out': '''
<div class="impress-not-supported" id="impress">
    <div class="step" data-rotate-z="0" data-x="0">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </div>
    <div class="step" data-rotate-z="0" data-x="1000">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </div>
    <div class="step" data-rotate-z="179.9" data-x="1000" data-y="800">
        <header>
            <h1>Title 3</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </div>
    <div class="step" data-rotate-z="179.9" data-x="0" data-y="800">
        <header>
            <h1>Title 4</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </div>
    <div class="step" data-rotate-z="0.0" data-x="0" data-y="1600">
        <header>
            <h1>Title 5</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </div>
</div>
''',
}


grid = {
    'rst': '''
.. presentation::
    :distribution: grid 2

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
    <slide data-x="0" data-y="1600">
        <header>
            <h1>Title 3</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-x="1600" data-y="1600">
        <header>
            <h1>Title 4</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-x="0" data-y="3200">
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


grid_parameter = {
    'rst': _five_slides,
    'part': 'body',
    'manual_slide_identification': True,
    'distribution': 'grid 2',
    'out': grid['out']
}


grid_rotate = {
    'rst': '''
.. presentation::
    :distribution: grid_rotate 2

''' + _five_slides,
    'part': 'body',
    'manual_slide_identification': True,
    'out': '''
<deck>
    <slide data-rotate-z="0" data-x="0">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-rotate-z="0" data-x="1600">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-rotate-z="179.9" data-x="1600" data-y="1600">
        <header>
            <h1>Title 3</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-rotate-z="179.9" data-x="0" data-y="1600">
        <header>
            <h1>Title 4</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-rotate-z="0.0" data-x="0" data-y="3200">
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

_change_distribution = '''

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

slide 4'''


change_distribution_linear = {
    'rst': '''
.. presentation::
    :distribution: linear''' + _change_distribution,
    'part': 'body',
    'out': '''
<deck>
    <slide data-x="0">
        <section>slide 1</section>
    </slide>
    <slide data-rotate-z="45" data-scale="-3" data-x="-2000" data-y="-1000">
        <section>slide 2</section>
    </slide>
    <slide data-rotate-z="45" data-scale="-3" data-x="-400" data-y="-1000">
        <section>slide 3</section>
    </slide>
    <slide data-rotate-z="45" data-scale="-3" data-x="1200" data-y="-1000">
        <section>slide 4</section>
    </slide>
</deck>
''',
}


change_distribution_grid = {
    'rst': '''
.. presentation::
    :distribution: grid 2''' + _change_distribution,
    'part': 'body',
    'out': '''
<deck>
    <slide data-x="0">
        <section>slide 1</section>
    </slide>
    <slide data-rotate-z="45" data-scale="-3" data-x="-2000" data-y="-1000">
        <section>slide 2</section>
    </slide>
    <slide data-rotate-z="45" data-scale="-3" data-x="-400" data-y="-1000">
        <section>slide 3</section>
    </slide>
    <slide data-rotate-z="45" data-scale="-3" data-x="-2000" data-y="600">
        <section>slide 4</section>
    </slide>
</deck>
''',
}


change_distribution_grid_rotate = {
    'rst': '''
.. presentation::
    :distribution: grid_rotate 2
    :increment: -800 -750''' + _change_distribution,
    'part': 'body',
    'out': '''
<deck>
    <slide data-rotate-z="0" data-x="0">
        <section>slide 1</section>
    </slide>
    <slide data-rotate-z="45" data-scale="-3" data-x="-2000" data-y="-1000">
        <section>slide 2</section>
    </slide>
    <slide data-rotate-z="45" data-scale="-3" data-x="-2800" data-y="-1000">
        <section>slide 3</section>
    </slide>
    <slide data-rotate-z="224.9" data-scale="-3" data-x="-2800" data-y="-1750">
        <section>slide 4</section>
    </slide>
</deck>
''',
}


change_distribution_func = {
    'rst': '''
.. presentation::
    :distribution: linear

slide 1

----

slide 2

.. presentation::
    :distribution: grid 1

----

slide 3

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
    <slide data-x="3200" data-y="1600">
        <section>slide 4</section>
    </slide>
    <slide data-x="3200" data-y="3200">
        <section>slide 5</section>
    </slide>
</deck>
''',
}

change_deck_slide_selectors_in_the_middle = {
    'rst': '''
.. presentation::
    :deck-selector: div.deck_container
    :slide-selector: article.slide

the tag of this slide is <article class="slide">

----

idem

.. presentation::
    :deck-selector: deck#impress
    :slide-selector: div.step

----

The tag here is supposed to be <div class="step">''',
    'part': 'body',
    'out': '''
<deck class="deck_container" id="impress">
    <article class="slide">
        <section>the tag of this slide is &lt;article class="slide"&gt;</section>
    </article>
    <article class="slide">
        <section>idem</section>
    </article>
    <div class="step">
        <section>The tag here is supposed to be &lt;div class="step"&gt;</section>
    </div>
</deck>
''',
}

deck_slide_selectors = {
    'rst': '''
.. presentation::
    :deck-selector: div.deck-container
    :slide-selector: article.slide

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
    <article class="cover slide" data-scale="5" data-x="-1000" data-y="-500" id="opening">
        <section>Welcome</section>
    </article>
    <article class="slide" data-rotate-x="180" data-scale="5" data-x="-1000" data-y="-500" \
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
    <article class="slide" data-rotate-x="180" data-rotate-z="180" data-scale="7" data-x="-1000" \
data-y="-1500">
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </article>
    <article class="slide" data-rotate-x="0" data-rotate-z="180" data-scale="7" data-x="0" \
data-y="-1500" id="title-3">
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
    'distribution': None,
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


field_list_transition = {
    'rst': ''':data-x: 100

slide 1

:data-x: 200

field list creates a new slide.
A transition '----' isn't mandatory
''',
    'part': 'body',
    'out': '''
<deck>
    <slide data-x="100">
        <section>slide 1</section>
    </slide>
    <slide data-x="200">
        <section>field list creates a new slide. \
A transition '----' isn't mandatory</section>
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


presentation_directive_1 = {
    'rst': '''
.. presentation::
    :distribution: grid_rotate 2
    :deck-selector: div#impress
    :slide-selector: div.slide
    :increment: 1000 800

slide 1

----

slide 2

----

slide 3
''',
    'part': 'body',
    'manual_slide_identification': True,
    'out': '''
<div id="impress">
    <div class="slide" data-rotate-z="0" data-x="0">
        <section>slide 1</section>
    </div>
    <div class="slide" data-rotate-z="0" data-x="1000">
        <section>slide 2</section>
    </div>
    <div class="slide" data-rotate-z="179.9" data-x="1000" data-y="800">
        <section>slide 3</section>
    </div>
</div>
''',
}


presentation_directive_1_doctree = {
    'rst': presentation_directive_1['rst'],
    'part': 'pseudoxml',
    'manual_slide_identification': True,
    'out': '''<document source="<string>">
    <presentation deck-selector="div#impress" distribution="grid_rotate 2" \
increment="1000 800" slide-selector="div.slide">
    <section>
        <slide_contents>
            <paragraph>
                slide 1
    <section>
        <slide_contents>
            <paragraph>
                slide 2
    <section>
        <slide_contents>
            <paragraph>
                slide 3
''',
}


presentation_directive_single_slide = {
    'rst': '''
.. presentation::
    :distribution: linear
    :deck-selector: div#impress

single slide
''',
    'part': 'body',
    'manual_slide_identification': True,
    'out': '''
<div id="impress">
    <slide data-x="0">
        <section>single slide</section>
    </slide>
</div>
''',
}


presentation_directive_single_slide_pseudoxml = {
    'rst': presentation_directive_single_slide['rst'],
    'part': 'pseudoxml',
    'manual_slide_identification': True,
    'out': '''<document source="<string>">
    <presentation deck-selector="div#impress" distribution="linear">
    <section>
        <slide_contents>
            <paragraph>
                single slide
''',
}

invalid_distribution_function_name = {
    'rst': '''
.. presentation::
    :distribution: linear

slide

.. presentation::
    :distribution: manual

----

An invalid distribution function name is simply ignored.
Not even a warning is raised
''',
    'part': 'pseudoxml',
    'manual_slide_identification': True,
    'out': '''<document source="<string>">
    <presentation distribution="linear">
    <section>
        <slide_contents>
            <paragraph>
                slide
    <presentation distribution="manual">
    <section>
        <slide_contents>
            <paragraph>
                An invalid distribution function name is simply ignored.
                Not even a warning is raised
''',
}


_simple_presentation = '''
.. meta::
    :http-equiv=X-UA-Compatible: chrome=1:
    :viewport: width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes

Title
=====

Text

.. class:: special

Title 2
=======

Another line'''


presentation_None = {
    'rst': _simple_presentation,
    'part': 'whole',
    'out': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta generator="rst2html5slides" />
    <meta generator-homepage="https://pypi.python.org/pypi/rst2html5slides" />
    <meta content="chrome=1:" http-equiv="X-UA-Compatible" />
    <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport" />

</head>
<body>
<deck>
    <slide id="title">
        <header>
            <h1>Title</h1>
        </header>
        <section>Text</section>
    </slide>
    <slide class="special" id="title-2">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>Another line</section>
    </slide>
</deck>
</body>
</html>''',
}

presentation_None_pseudoxml = {
    'rst': _simple_presentation,
    'part': 'pseudoxml',
    'out': '''<document source="<string>">
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

presentation_impress = {
    'rst': _simple_presentation,
    'presentation': 'impress.js',
    'part': 'whole',
    'out': '''<!DOCTYPE html>
<html>
<head>
    <link href="css/impress.css" rel="stylesheet" />
    <script src="js/impress.js"></script>

    <meta charset="utf-8" />
    <meta generator="rst2html5slides" />
    <meta generator-homepage="https://pypi.python.org/pypi/rst2html5slides" />
    <meta content="chrome=1:" http-equiv="X-UA-Compatible" />
    <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport" />

</head>
<body>
<div id="impress">
    <div id="title" class="step" data-x="0">
        <header>
            <h1>Title</h1>
        </header>
        <section>Text</section>
    </div>
    <div id="title-2" class="special step" data-x="1600">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>Another line</section>
    </div>
</div>
</body>
</html>
''',
}

presentation_jmpress = {
    'rst': _simple_presentation,
    'presentation': 'jmpress.js',
    'part': 'whole',
    'out': '''<!DOCTYPE html>
<html>
<head>
    <link href="css/slides.css" rel="stylesheet" />
    <script src="js/jquery.min.js"></script>
    <script src="js/jmpress/jmpress.js"></script>
    <script src="js/jmpress/jmpress_init.js" defer="defer"></script>
    <script src="js/adjust_slides.js" defer="defer"></script>

    <meta charset="utf-8" />
    <meta generator="rst2html5slides" />
    <meta generator-homepage="https://pypi.python.org/pypi/rst2html5slides" />
    <meta content="chrome=1:" http-equiv="X-UA-Compatible" />
    <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport" />

</head>
<body>
<div id="jmpress">
    <div id="title" class="step" data-x="0">
        <header>
            <h1>Title</h1>
        </header>
        <section>Text</section>
    </div>
    <div id="title-2" class="special step" data-x="1600">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>Another line</section>
    </div>
</div>
</body>
</html>
''',
}

presentation_deck = {
    'rst': _simple_presentation,
    'presentation': 'deck.js',
    'part': 'whole',
    'out': '''<!DOCTYPE html>
<!--[if lt IE 7]> <html class="no-js ie6" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js ie7" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js ie8" lang="en"> <![endif]-->
<!--[if gt IE 8]><!-->  <html class="no-js" lang="en"> <!--<![endif]-->
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=1024, user-scalable=no">

    <!-- Core and extension CSS files -->
    <link rel="stylesheet" media="screen" href="css/deck.js/deck.core.css">
    <link rel="stylesheet" media="screen" href="css/deck.js/deck.goto.css">
    <link rel="stylesheet" media="screen" href="css/deck.js/deck.menu.css">
    <link rel="stylesheet" media="screen" href="css/deck.js/deck.navigation.css">
    <link rel="stylesheet" media="screen" href="css/deck.js/deck.status.css">
    <link rel="stylesheet" media="screen" href="css/deck.js/deck.scale.css">

    <!-- Style theme. More available in /themes/style/ or create your own. -->
    <link id="style-theme-link" rel="stylesheet" media="screen" href="css/deck.js/web-2.0.css">

    <!-- Transition theme. More available in /themes/transition/ or create your own. -->
    <link id="transition-theme-link" rel="stylesheet" media="screen" href="css/deck.js/horizontal-slide.css">

    <!-- Basic black and white print styles -->
    <link rel="stylesheet" media="print" href="css/deck.js/print.css">

    <script src="js/modernizr.custom.js"></script>

    <meta charset="utf-8" />
    <meta generator="rst2html5slides" />
    <meta generator-homepage="https://pypi.python.org/pypi/rst2html5slides" />
    <meta content="chrome=1:" http-equiv="X-UA-Compatible" />
    <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport" />

</head>
<body>
<div id="deck">
    <div id="title" class="step">
        <header>
            <h1>Title</h1>
        </header>
        <section>Text</section>
    </div>
    <div id="title-2" class="special step">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>Another line</section>
    </div>
</div>


<!-- deck.navigation snippet -->
<div aria-role="navigation">
    <a href="#" class="deck-prev-link" title="Previous">&#8592;</a>
    <a href="#" class="deck-next-link" title="Next">&#8594;</a>
</div>

<!-- deck.status snippet -->
<p class="deck-status" aria-role="status">
    <span class="deck-status-current"></span>
    /
    <span class="deck-status-total"></span>
</p>

<!-- deck.goto snippet -->
<form action="." method="get" class="goto-form">
    <label for="goto-slide">Go to slide:</label>
    <input type="text" name="slidenum" id="goto-slide" list="goto-datalist">
    <datalist id="goto-datalist"></datalist>
    <input type="submit" value="Go">
</form>

<script src="js/jquery.min.js"></script>

<!-- Deck Core and extensions -->
<script src="js/deck.js/deck.core.js"></script>
<script src="js/deck.js/deck.menu.js"></script>
<script src="js/deck.js/deck.goto.js"></script>
<script src="js/deck.js/deck.status.js"></script>
<script src="js/deck.js/deck.navigation.js"></script>
<script src="js/deck.js/deck.scale.js"></script>

<!-- Initialize the deck -->
<script>
$(function() {
    $.deck('slide');
});
</script>

</body>
</html>
''',
}
