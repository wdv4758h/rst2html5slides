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
        <contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet
    <section ids="title-2" names="title\ 2">
        <header>
            <title>
                Title 2
        <contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet 2
''',
    'debug': True,
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
        <contents>
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
        <contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet 2
''',
    'debug': True,
}


lose_nodes = {
    'rst': '''paragraph

* bullet 1
* bullet 2''',
    'out': '''<document source="<string>">
    <section>
        <contents>
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
    'debug': True
}


single_slide = {
    'rst': '''
Title 1
=======

* bullet''',
    'out': '''<document ids="title-1" names="title\ 1" source="<string>" title="Title 1">
    <section>
        <header>
            <title>
                Title 1
        <contents>
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        bullet
''',
    'debug': True,
}
