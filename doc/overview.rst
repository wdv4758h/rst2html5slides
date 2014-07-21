
A presentation starts with a rst file:

.. include:: doc/example1.rst
    :code: rst

Without any additional parameters,
the HTML5 code produced is:

.. code-block:: bash

    $ rst2html5slides example.rst

.. include:: doc/example1.html
    :code: html

It won't work as it is because
rst2html5slides does not provide or attach any presentation framework files by default.
They should be specified as parameters or in a template file.
Besides,
the structure of HTML of the deck of slides certainly will not fit directly any presentation framework.
Some small adjustments have to be done.


Presentation Frameworks
=======================

impress.js
----------



.. code-block:: html

    <div id="impress">
        <div class="step">
            ...
        </div>
        ...
    </div>


jmpress.js
----------

Permite


Using a Template File
=====================

The easiest way to suit the rst2html5slides result to a specific presentation framework
is using a template with all necessary surrounds.
The role of rst2html5slides is to fill in the blanks with the deck of slides.

Below there is an example of a template to use rst2html5slides with the `jmpress.js` framework:

.. include:: doc/jmpress_template.html
    :code: html

.. tip::

    You must always double curly braces in template's javascripts.
    To avoid this, keep all scripts in external files.
    In the previous template,
    the jmpress initialization could be a external file included by a
    :literal:`<script defer="defer" src="jmpress_init.js"></script>`.

The command to generate a presentation from example.rst using the previous template
is show below:

.. code-block:: bash

    $ rst2html5slides --template jmpress_template.html example.rst

.. include:: doc/example1-jmpress.html
    :code: html


Using Parameters
================

It is possible to get an equivalent result using parameters.
However:

#. All meta tags must be defined in the rst file through a :literal:`meta` directive
   usually placed at the beginning of the rst file:

    .. code-block:: rst

        .. meta::
            :author: André Felipe Dias
            :viewport: width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes
            :http-equiv=X-UA-Compatible: chrome=1

#. All stylesheets and scripts should be passed as parameters
#. The framework initialization must be in an external file specified via a :literal:`--script-defer` option

    .. include:: doc/jmpress_init.js
        :code: javascript

The command to produce an equivalent `jmpress.js`_ presentation from the previous section would be:

.. code-block:: bash

    $ rst2html5slides \
        --stylesheet impress.css \
        --script http://code.jquery.com/jquery-latest.min.js \
        --script jmpress.js \
        --script-defer jmpress_init.js \
        example-with-meta-tag.rst

.. include:: doc/example2.html
    :code: html



A slide is delimited by three different ways:

#. Title. A new title automatically starts a new section that corresponds to a new slide
#. Horizontal line :literal:`----`
#. :literal:`slide` directive



Slides Delimitados por Title
-----------------------------

O restrucutedText automaticamente gera seções para cada título encontrado.
Como exemplo, considere o trecho a seguir:






O pseudoxml gerado é o seguinte:

.. code-block:: xml

    <document source="trecho.rst">
        <section ids="titulo-1" names="título\ 1">
            <title>
                Title 1
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        item 1
                <list_item>
                    <paragraph>
                        item 2
        <section ids="titulo-2" names="título\ 2">
            <title>
                Title 2
            <bullet_list bullet="*">
                <list_item>
                    <paragraph>
                        item 1
                <list_item>
                    <paragraph>
                        item 2

Essa característica foi aproveitada para traduzir nós do tipo ``section``
diretamante para o marcador ``<slide>`` em html5 no resultado final.
O título será agrupado em um ``<header>`` e o conteúdo do slide em uma ``<section>``,
conforme planejado inicialmente para a estrutura do slide.

O slide pode ter um subtítulo:

.. code-block:: rst

    Title
    ======

    Subtítulo
    ---------

    parágrafo 1

    parágrafo 2

Resultando em HTML5:

.. code-block:: html

    <slide>
        <header>
            <h1>Title</h1>
            <h2>Subtítulo</h2>
        </header>
        <section>
            <p>parágrafo 1</p>
            <p>parágrafo 2</p>
        </section>
    </slide>

.. note::

    A ideia inicial era usar um agrupamento em torno de ``<hgroup>``
    mas essa tag foi excluída do padrão HTML5.


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

A linha horizontal é indicada para os casos de slides que não têm Title.


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




Directives
==========

There