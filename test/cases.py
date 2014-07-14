#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains test data to rst2html5slides in the form:
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
}


slide_doctree = {
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
}


lose_nodes = {
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
    'out': '''
<deck>
    <slide class="segue dark nobackground">
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
    <slide>
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

# rst2html5slides doesn't allow three different heading levels at the same slide
h3 =  {
    'rst': '''Title 1
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
        <header>
            <h1>Title 1</h1>
            <h2>Subtitle</h2>
            <h2>Subsubtitle</h2>
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
    'out': '''<document ids="title-1" names="title\ 1" source="<string>" title="Title 1">
    <section>
        <header>
            <title>
                Title 1
            <subtitle ids="subtitle" names="subtitle">
                Subtitle
            <subtitle>
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

square = {
    'rst': ''':distribution: square 2

''' + _five_slides,
    'part': 'body',
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

square_rotate = {
    'rst': ''':distribution: square_rotate 2

''' + _five_slides,
    'part': 'body',
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

container_slide_options  = {
    'rst': ''':container: div.deck_container
:slide: article.slide

Welcome

Title 1
=======

* Bullet

:container: deck#impress
:slide: div.step

Title 2
=======

* Bullet''',
    'part': 'body',
    'out': '''
<deck class="deck_container" id="impress">
    <article class="slide">
        <section>Welcome</section>
    </article>
    <div class="step">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </div>
    <div class="step">
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

container_slide_options_2  = {
    'rst': ''':container: div.deck-container
:slide: article.slide

:id: opening
:class: cover
:data-x: -1000
:data-y: -500
:data-scale: 5

Welcome

Title 1
=======

* Bullet

:data-y: -1500
:data-rotate: 180
:data-scale: 7

----

* Bullet

Title 3
=======

* Bullet
''',
    'part': 'body',
    'out': '''
<div class="deck-container">
    <article data-y="-500" data-x="-1000" data-scale="5" id="opening" class="slide">
        <section>Welcome</section>
    </article>
    <article class="slide">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </article>
    <article data-y="-1500" data-rotate="180" class="slide" data-scale="7">
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </article>
    <article class="slide">
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

case_1 = {
    'rst': '''.. meta::
    :http-equiv=X-UA-Compatible: chrome=1:
    :viewport: width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes

:container: div#impress
:slide: div.step
:data-x: 1000
:data-y: 2000

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
    <div data-y="2000" data-x="1000" class="step">
        <header>
            <h1>Title</h1>
        </header>
        <section>Text</section>
    </div>
    <div class="special step">
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
                container
            <field_body>
                <paragraph>
                    div#impress
        <field>
            <field_name>
                slide
            <field_body>
                <paragraph>
                    div.step
        <field>
            <field_name>
                data-x
            <field_body>
                <paragraph>
                    1000
        <field>
            <field_name>
                data-y
            <field_body>
                <paragraph>
                    2000
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
    <slide>
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
    <slide data-x="100">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>slide 1</section>
    </slide>
    <slide data-x="200">
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

