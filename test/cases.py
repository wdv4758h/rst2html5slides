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
<deck>
    <slide>
        <section>paragraph</section>
    </slide>
</deck>
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
<deck>
    <slide class="special">
        <header>
            <h1>Teste 1</h1>
            <h2>Subtitle</h2>
        </header>
        <section>paragraph</section>
    </slide>
</deck>
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
<deck>
    <slide class="special">
        <header>
            <h1>Teste 1</h1>
            <h2>Subtitle</h2>
        </header>
        <section class="flexbox vcenter">paragraph</section>
    </slide>
</deck>
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
<deck>
    <slide class="segue dark quote nobackground">
        <section class="flexbox vleft auto-fadein">
            <blockquote class="epigraph">
                <p>This is an example of quote text.</p>
            </blockquote>
        </section>
    </slide>
</deck>
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
<deck>
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
</deck>
''',
    'part': 'body',
}

slide_impress_1 = {
    'rst': '''.. slide::
    :id: paragraph
    :class: special
    :data-x: 1000
    :data-y: -200
    :data-scale: 4
    :no-sense-attr: xyz

    paragraph
''',
    'part': 'pseudoxml',
    'out': '''<document source="<string>">
    <section classes="special" data-scale="4" data-x="1000" data-y="-200" id="paragraph" no-sense-attr="xyz">
        <slide_contents>
            <paragraph>
                paragraph
''',
}

slide_impress_1_slideshow = {
    'rst': slide_impress_1['rst'],
    'part': 'body',
    'out': '''
<deck>
    <slide no-sense-attr="xyz" class="special" data-y="-200" data-x="1000" data-scale="4" id="paragraph">
        <section>paragraph</section>
    </slide>
</deck>
''',
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
<deck>
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
</deck>
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

_rst_example = '''Title 1
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
    'rst': '''.. rst2html5slides::
    :distribution: linear

''' + _rst_example,
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
    <slide data-x="1500">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-x="3000">
        <header>
            <h1>Title 3</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-x="4500">
        <header>
            <h1>Title 4</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-x="6000">
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
    'rst': '''.. rst2html5slides::
    :distribution: square
    :distribution_parameter: 2

''' + _rst_example,
    'part': 'body',
    'out': '''
<deck>
    <slide data-y="0" data-x="0">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-y="0" data-x="1500">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-y="800" data-x="0">
        <header>
            <h1>Title 3</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-y="800" data-x="1500">
        <header>
            <h1>Title 4</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-y="1600" data-x="0">
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

square2 = {
    'rst': '''.. rst2html5slides::
    :distribution: square2
    :distribution_parameter: 2

''' + _rst_example,
    'part': 'body',
    'out': '''
<deck>
    <slide data-rotate-z="0" data-y="0" data-x="0">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-rotate-z="0" data-y="0" data-x="1500">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-rotate-z="179.9" data-y="800" data-x="1500">
        <header>
            <h1>Title 3</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-rotate-z="179.9" data-y="800" data-x="0">
        <header>
            <h1>Title 4</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </slide>
    <slide data-rotate-z="0" data-y="1600" data-x="0">
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

# spiral = {
#     'rst': '''.. slides_distribution::
#     :distribution: spiral

# ''' + _rst_example,
#     'part': 'body',
#     'out': '''
# ''',
# }


distribution_slide_with_data = {
    'rst': '''.. rst2html5slides::
    :distribution: square
    :distribution_parameter: 2
    :container_tag: div
    :container_class: deck-container
    :slide_tag: article
    :slide_class: slide

.. slide::
    :id: opening
    :class: cover
    :data-x: -1000
    :data-y: -500
    :data-scale: 5

    Welcome

Title 1
=======

* Bullet

Title 2
=======

* Bullet

Title 3
=======

* Bullet

.. slide::
    :data-y: -1500
    :data-rotate: 180
    :data-scale: 7
    :contents_class: special

    * Bullet

Title 5
=======

* Bullet
''',
    'part': 'body',
    'out': '''
<div class="deck-container">
    <article data-y="-500" data-x="-1000" data-scale="5" id="opening" class="cover slide">
        <section>Welcome</section>
    </article>
    <article class="slide" data-y="0" data-x="1500">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </article>
    <article class="slide" data-y="800" data-x="0">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </article>
    <article class="slide" data-y="800" data-x="1500">
        <header>
            <h1>Title 3</h1>
        </header>
        <section>
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </article>
    <article data-y="-1500" data-scale="7" class="slide" data-rotate="180">
        <section class="special">
            <ul>
                <li>Bullet</li>
            </ul>
        </section>
    </article>
    <article class="slide" data-y="1600" data-x="1500">
        <header>
            <h1>Title 5</h1>
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

rst2html5slides_directive = {
    'rst': '''.. rst2html5slides::
    :distribution: linear
    :distribution_parameter: 3
    :incr_x: 1200
    :container_tag: div
    :container_class: deck-container
    :slide_tag: article
    :slide_class: slide
''',
    'part': 'pseudoxml',
    'out': '''<document source="<string>">
    <rst2html5slides_options container_class="deck-container" container_tag="div" \
distribution="linear" distribution_parameter="3" incr_x="1200" slide_class="slide" \
slide_tag="article">
''',
}

rst2html5slides_directive_2 = {
    'rst': rst2html5slides_directive['rst'],
    'part': 'body',
    'out': '',
}

rst2html5slides_directive_3 = {
    'rst': rst2html5slides_directive['rst'] + '''

Title 1
=======

* item

Title 2
=======

* item
''',
    'part': 'body',
    'out': '''
<div class="deck-container">
    <article class="slide" data-x="0">
        <header>
            <h1>Title 1</h1>
        </header>
        <section>
            <ul>
                <li>item</li>
            </ul>
        </section>
    </article>
    <article class="slide" data-x="1200">
        <header>
            <h1>Title 2</h1>
        </header>
        <section>
            <ul>
                <li>item</li>
            </ul>
        </section>
    </article>
</div>
''',
}