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
    'indent_output': True,
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
    'indent_output': True,
}


hgroup = {
    'rst': '''
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
<slides class="layout-widescreen">
    <slide>
        <header>
            <hgroup>
                <h1>Title 1</h1>
                <h2>Subtitle</h2>
            </hgroup>
        </header>
        <section>
            <ul>
                <li>bullet</li>
            </ul>
        </section>
    </slide>
    <slide>
        <header>
            <hgroup>
                <h1>Title 2</h1>
                <h2>Subtitle 2</h2>
            </hgroup>
        </header>
        <section>
            <ul>
                <li>bullet 2</li>
            </ul>
        </section>
    </slide>
</slides>
''',
    'indent_output': True,
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
    'indent_output': True
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
    'indent_output': True,
}