# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from io import open
from os import makedirs, urandom
from os.path import join, exists
from shutil import rmtree
from tempfile import mkdtemp
from rst2html5slides import SlideWriter
from docutils.core import publish_file

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


.. include:: junit.rst


.. title:: Testes Automatizados de Software
.. meta::
    :generator: rst2html5slides https://bitbucket.org/andre_felipe_dias/rst2html5slides
    :author: André Felipe Dias

.. |logotipo| image:: imagens/logotipo.png
.. |tdd cycle| image:: imagens/tdd_cycle.png
'''

junit = '''JUnit
=====

JUnit is a testing framework'''

css = 'div {background-color: red}'


def test_output_dir():
    temp_dirname = mkdtemp()
    dest_dirname = mkdtemp()
    makedirs(join(temp_dirname, 'imagens'))
    makedirs(join(temp_dirname, 'css'))
    source_path = join(temp_dirname, 'presentation.rst')
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(presentation)
    with open(join(temp_dirname, 'junit.rst'), 'w', encoding='utf-8') as f:
        f.write(junit)
    with open(join(temp_dirname, 'css', 'style.css'), 'w', encoding='utf-8') as f:
        f.write(css)
    with open(join(temp_dirname, 'imagens', 'tdd_cycle.png'), 'wb') as f:
        f.write(urandom(2 ** 16))
    with open(join(temp_dirname, 'imagens', 'not_used.png'), 'wb') as f:
        f.write(urandom(2 ** 11))
    with open(join(temp_dirname, 'imagens', 'logotipo.png'), 'wb') as f:
        f.write(urandom(2 ** 15))
    publish_file(
        writer=SlideWriter(), source_path=source_path,
        destination_path=join(dest_dirname, 'presentation.html1'),
        settings_overrides={'output_dir': dest_dirname, 'stylesheet': [join('css', 'style.css')]}
    )
    assert exists(join(dest_dirname, 'presentation.html'))
    assert not exists(join(dest_dirname, 'presentation.html1'))
    assert exists(join(dest_dirname, 'css', 'style.css'))
    assert exists(join(dest_dirname, 'imagens', 'tdd_cycle.png'))
    assert exists(join(dest_dirname, 'imagens', 'logotipo.png'))
    assert not exists(join(dest_dirname, 'imagens', 'not_used.png'))
    rmtree(temp_dirname)
    rmtree(dest_dirname)
