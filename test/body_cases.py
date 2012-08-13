#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains test data to rst2slideshow in the form:
# case = {'rst': rst_text, 'out': expected_output, ...}

from __future__ import unicode_literals


# single_slide = {
#     'rst': '''
# Title 1
# =======

# * bullet''',
#     'out': '',
#     'indent_output': True,
# }


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

