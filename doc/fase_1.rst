======================
Fase 1 - rst2slideshow
======================

Transformar o restructuredText em slideshow

.. _estrutura do slide:

Estrutura de um Slide
=====================

::

    Slide
    +----------------------------------------------+
    |                                              |
    |   +--------------------------------------+   |
    |   | header/hgroup                        |   |
    |   +--------------------------------------+   |
    |                                              |
    |   +--------------------------------------+   |
    |   | section/article                      |   |
    |   |                                      |   |
    |   |                                      |   |
    |   |                                      |   |
    |   |                                      |   |
    |   |                                      |   |
    |   +--------------------------------------+   |
    |                                              |
    |   +--------------------------------------+   |
    |   | footer: inserido via javascript      |   |
    |   +--------------------------------------+   |
    |                                              |
    +----------------------------------------------+

Será necessário manipular a *doctree* para ajustá-la a uma estrutura mais adequada.

Caso 1: Seção Única correspondente a um slide
---------------------------------------------

::

    document
        section
            title
            content


para::

    document
        slide
            header
                title
            article
                content


Caso 2: Slide com subseção
-------

::

    document
        section
            title h1
            section
                title h2
                content
        ...

para::

    document
        slide
            header
                hgroup
                    title h1
                    title h2
            section
                content
        ...

Caso 3
------

::

    document
        title
        content


para::

    document
        slide
            header
                title
            section
                content

Veja :file:`../test/cases.py` para outros casos previstos.


Separadores de Slides
=====================

Um slide é delimitado de três maneiras diferentes:

#. Título. Um novo título começa uma nova seção, que corresponde a um novo slide
#. Linha horizontal ``----``
#. Diretiva ``slide``

Slides Delimitados por Título
-----------------------------

O restrucutedText automaticamente gera seções para cada título encontrado.
Como exemplo, considere o trecho a seguir:

.. code-block:: rst

    Título 1
    ========

    * item 1
    * item 2

    Título 2
    ========

    * item 1
    * item 2

O pseudoxml gerado é o seguinte:

.. code-block:: xml

    <document source="trecho.rst">
        <section ids="titulo-1" names="título\ 1">
            <title>
                Título 1
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        item 1
                <list_item>
                    <paragraph>
                        item 2
        <section ids="titulo-2" names="título\ 2">
            <title>
                Título 2
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        item 1
                <list_item>
                    <paragraph>
                        item 2

Essa característica foi aproveitada para traduzir nós do tipo ``section``
diretemante para o marcador ``<slide>`` em html5 no resultado final.
O título será agrupado em um ``<header>`` e o conteúdo do slide em uma ``<section>``,
conforme planejado inicialmente para a `estrutura do slide`_.

O slide pode ter um subtítulo.
Nesse caso, o título e o subtítulo são agrupados em um elemento ``<hgroup>``:

.. code-block:: rst

    Título
    ======

    Subtítulo
    ---------

    parágrafo 1

    parágrafo 2

Resultando em HTML5:

.. code-block:: html

    <slide>
        <header>
            <hgroup>
                <h1>Título</h1>
                <h2>Subtítulo</h2>
            </hgroup>
        </header>
        <section>
            <p>parágrafo 1</p>
            <p>parágrafo 2</p>
        </section>
    </slide>


Slides Delimitados por uma Linha Horizontal
-------------------------------------------

Uma linha horizontal é uma sequência formada por 4 ou mais caracteres de pontuação
(`ref <http://docutils.sourceforge.net/docs/user/rst/quickref.html#transitions>`_),
que corresponde a um nó do tipo ``transition``.

Originalmente, a linha horizontal corresponde em HTML5 ao elemento ``<hr />``,
mas foi aproveitado para indicar o limite entre um slide e outro:

.. code-block:: rst

    Slide 1

    -----------

    slide 2

    .. class:: segue contexto

    -----------

    slide 3 com atributo class="segue contexto"

A linha horizontal é indicado para os casos de slides que não têm Título.


Slides Delimmitados pela Diretiva ``slide``
-------------------------------------------

A diretiva ``slide`` é o modo mais flexível de delimitar um slide.
Serve tanto para slides que têm título e subtítulo,
quanto para slides que não têm.
Além disso, pode receber diretamente o parâmetro correspondente ao atributo ``class``:


.. code-block:: rst

    .. slide::
        :class: special black-background
        :title: Slide 1
        :subtitle: Subtítulo do slide

        conteúdo do slide

    .. slide::

        conteúdo do outro slide 2, que não tem título