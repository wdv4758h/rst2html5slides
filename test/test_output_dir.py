# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from io import open
from os import makedirs, urandom
from os.path import join, exists
from shutil import rmtree
from tempfile import mkdtemp
from rst2html5slides import SlideWriter
from docutils.core import publish_file, publish_string

presentation = '''.. presentation::
    :distribution: grid

.. role:: small

.. class:: capa

Presentation Title
==================

Agenda
======

* Topic 1
* Topic 2
* Topic 3

|logotipo|

.. class:: chapter

Chapter 1
=========

Schema
======

|tdd cycle|

----

|python logo|


.. include:: junit.rst


.. title:: Testes Automatizados de Software
.. meta::
    :generator: rst2html5slides https://bitbucket.org/andre_felipe_dias/rst2html5slides
    :author: André Felipe Dias

.. |logotipo| image:: imagens/logotipo.png
.. |tdd cycle| image:: imagens/tdd_cycle.png
.. |python logo| image:: https://www.python.org/static/community_logos/python-logo-master-v3-TM.png
'''

junit = '''JUnit
=====

JUnit is a testing framework'''

css = 'div {background-color: red}'
source_dir = mkdtemp()
source_path = join(source_dir, 'presentation.rst')


def setup():
    makedirs(join(source_dir, 'imagens'))
    makedirs(join(source_dir, 'css'))
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(presentation)
    with open(join(source_dir, 'junit.rst'), 'w', encoding='utf-8') as f:
        f.write(junit)
    with open(join(source_dir, 'css', 'style.css'), 'w', encoding='utf-8') as f:
        f.write(css)
    with open(join(source_dir, 'imagens', 'tdd_cycle.png'), 'wb') as f:
        f.write(urandom(2 ** 16))
    with open(join(source_dir, 'imagens', 'not_used.png'), 'wb') as f:
        f.write(urandom(2 ** 11))
    with open(join(source_dir, 'imagens', 'logotipo.png'), 'wb') as f:
        f.write(urandom(2 ** 15))


def teardown():
    rmtree(source_dir)


def test_destination_dir():
    dest_dir = mkdtemp()
    output = publish_file(
        writer=SlideWriter(), source_path=source_path,
        destination_path=dest_dir,
        settings_overrides={'stylesheet': [join('css', 'style.css')]}
    )
    assert exists(join(dest_dir, 'presentation.html'))
    assert exists(join(dest_dir, 'css', 'style.css'))
    assert exists(join(dest_dir, 'imagens', 'tdd_cycle.png'))
    assert exists(join(dest_dir, 'imagens', 'logotipo.png'))
    assert exists(join(dest_dir, 'css', 'slides.css'))
    assert exists(join(dest_dir, 'js'))
    assert not exists(join(dest_dir, 'imagens', 'not_used.png'))
    assert str('<link href="css/slides.css"') in output
    assert str('<script src="js/jquery.min.js">') in output
    assert str('<link href="css/style.css"') in output
    assert str('src="https://www.python.org') in output
    rmtree(dest_dir)


def test_destination_path():
    dest_dir = mkdtemp()
    output = publish_file(
        writer=SlideWriter(), source_path=source_path,
        destination_path=join(dest_dir, 'slides.html'),
        settings_overrides={'stylesheet': [join('css', 'style.css')]}
    )
    assert exists(join(dest_dir, 'slides.html'))
    assert not exists(join(dest_dir, 'presentation.html'))
    assert exists(join(dest_dir, 'css', 'style.css'))
    assert exists(join(dest_dir, 'imagens', 'tdd_cycle.png'))
    assert exists(join(dest_dir, 'imagens', 'logotipo.png'))
    assert not exists(join(dest_dir, 'imagens', 'not_used.png'))
    assert exists(join(dest_dir, 'css', 'slides.css'))
    assert exists(join(dest_dir, 'js'))
    assert str('<link href="css/slides.css"') in output
    assert str('<script src="js/jquery.min.js">') in output
    assert str('<link href="css/style.css"') in output
    assert str('src="https://www.python.org') in output
    rmtree(dest_dir)


def test_no_destination():
    dest_dir = mkdtemp()
    os.chdir(dest_dir)
    output = publish_string(
        writer=SlideWriter(), source=presentation, source_path=source_path,
        settings_overrides={'stylesheet': [join('css', 'style.css')],
                            'output_encoding': 'unicode'}
    )
    assert not exists(join(dest_dir, 'presentation.html'))
    assert not exists(join(dest_dir, 'css', 'style.css'))
    assert not exists(join(dest_dir, 'imagens', 'tdd_cycle.png'))
    assert not exists(join(dest_dir, 'imagens', 'logotipo.png'))
    assert not exists(join(dest_dir, 'imagens', 'not_used.png'))
    assert not exists(join(dest_dir, 'css', 'slides.css'))
    assert not exists(join(dest_dir, 'js'))
    assert str('<link href="css/slides.css"') in output
    assert str('<script src="js/jquery.min.js">') in output
    assert '<link href="css/style.css"' in output
    assert 'src="https://www.python.org' in output
    rmtree(dest_dir)
