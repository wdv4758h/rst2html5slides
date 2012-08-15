===================================
Como transformar de rst para Slides
===================================

* `rst2slides <http://packages.python.org/rst2slides>`_
* `pandoc <http://johnmacfarlane.net/pandoc/index.html>`_
* `Sphinx S6 <https://bitbucket.org/shimizukawa/sphinxjp.themes.s6>`_

Sphinx ou rst
=============

Tem diferença entre usar o sphinx ou o rst diretamente?

rst2slides trabalha diretamente sobre o rst, sem precisar do Sphinx.
Contudo, parece não possuir todas as funcionalidades adicionais que o Sphinx traz.

O trecho abaixo é um texto em rst que é processado corretamente pelo comando ``rst2html``::

	this is colourful Python code:

	.. code:: python

	   def hello():
	       print "hello world"


	.. math::

	   C_{base,p1} & = diff(R_{base}, R_{p1}) = R_{p1} - R_{base}\\
	   C_{base,p2} & = diff(R_{base}, R_{p2}) = R_{p2} - R_{base}\\
	   C_{merge} & = C_{base,p1} + C_{base,p2}\\
	   R_{merge} & = patch(R_{base}, C_{merge})

Tanto o processamento do trecho de código quanto o de matemática são reconhecidos.
Contudo, a cor das partes do código não são aplicadas
pois o CSS com o padrão de cores não é incluído automaticamente pelo comando ``rst2html``.

Portanto, parece que o Sphinx não é um pré-requisito de instalação para gerar os slides a partir do rst.

rst2slides
==========

Já existe um projeto com esse nome: `rst2slides <http://packages.python.org/rst2slides>`_

* `PEP 258 <http://www.python.org/dev/peps/pep-0258/>`_ fornece algumas informações sobre o docutils.

Criando um Writer
=================

* http://www.arnebrodowski.de/blog/write-your-own-restructuredtext-writer.html

É necessário decidir que seções usar.
http://edward.oconnor.cx/2009/08/marking-up-a-slideshow-in-html5


Criando uma Diretiva de reStructuredText
========================================


* `Docutils Hacker's Guide <http://docutils.sourceforge.net/docs/dev/hacking.html>`_. Não foi muito
  útil. Apresentou as etapas do processamento de um texto rst, mas não entrou em detalhes.
  Uma informação interessante é que a extensão pode ser feita em uma das três partes: Parser,
  Transformer ou Writer.
* http://docutils.sourceforge.net/docs/howto/rst-directives.html

Como em muitos projetos open source, a documentação é escassa.
O jeito é estudar diretamente o código fonte e os testes unitários.


Exemplo de declaração de diretiva de vídeo:
https://github.com/astraw/burst_s5/blob/master/burst_s5/video_directive.py

docutils com HTML5: https://github.com/eegg/docutils-html5-writer


Estrutura dos Slides
====================

Existem várias bibliotecas para transformar o html em slides S5:

* `S6 <https://github.com/geraldb/s6>`_
* Apresentações do Google IO têm versões diferentes.

	* `io 2012 slides <http://io-2012-slides.googlecode.com>`_ | Google IO 2012
	* `html5wow <http://www.htmlfivewow.com>`_ | Google IO 2011
	* `The Web Can Do That <http://www.htmlfivecan.com>`_ | Google IO 2012
	* `html5slides <http://code.google.com/p/html5slides/>`_ | Modelo 2011
    * `reveal.js <http://lab.hakim.se/reveal-js>`_ https://github.com/hakimel/reveal.js

* `DZSlides <http://paulrouget.com/dzslides/>`_

Entretanto, a estrutura do HTML5 sobre as quais operam é relativamente independente,
com cada slide em uma seção.
Atributos de classe da seção mudam as transições e outras características do slide.

.. code-block:: html
    :linenos:

    <slides class="layout-widescreen">

        <slide class="estilos">
            <header>
                Título
            </header>
            <section>
                texto
            </section>
        </slide>

        <slide class="lista de estilos">
            <header>
                Título
            </header>
            <section class="estilos">
                texto
            </section>
        </slide>

    </slides>


Estrutura do Slide em reStructuredText
======================================

O título pode definir automaticamente o começo de uma seção. O Pandoc trabalha assim.

Mas e se for um slide que não tem título?
O primeiro slide, por exemplo, não tem título, só uma figura (logotipo).

Cada slide pode ter uma classe diferente. Se o novo slide for definido por um título,
como atribuir essas classes ao slide?

Um título pode continuar começando um novo slide
e também pode haver um comando específico para gerar um novo slide.

Uma diretiva ``slide`` pode ser usada para definir a classe dos próximos slides,
até outra diretiva ser encontrada, tal como a diretiva ``default-role``.


::

    slide 1
    =======

    * item 1
    * item 2
    * item 3

    slide 2
    =======

    * item 1
    * item 2
    * item 3

    .. slide-style: segue transparent

    slide 3
    =======

    * etc.

    .. new-slide::

    * sem título



Projeto IO-2012-slides
======================

O script de conversão está no diretório ``scripts/md``.
O padrão usado é o ``markdown``, que realmente é mais simples que o rst e suficiente para páginas web.

Um documento em ``markdown`` é analisado e inserido em um template em ``jinja``:

.. _io-2012-template:

.. code-block:: html
    :linenos:

    <!--
    Google IO 2012 HTML5 Slide Template

    Authors: Eric Bidelman <ebidel@gmail.com>
             Luke Mahe <lukem@google.com>

    URL: https://code.google.com/p/io-2012-slides
    -->
    <!DOCTYPE html>
    <html>
    <head>
      <title>Google IO 2012</title>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="chrome=1">
      <!--<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">-->
      <!--<meta name="viewport" content="width=device-width, initial-scale=1.0">-->
      <!--This one seems to work all the time, but really small on ipad-->
      <!--<meta name="viewport" content="initial-scale=0.4">-->
      <meta name="apple-mobile-web-app-capable" content="yes">
      <link rel="stylesheet" media="all" href="theme/css/default.css">
      <link rel="stylesheet" media="only screen and (max-device-width: 480px)" href="theme/css/phone.css">
      <base target="_blank"> <!-- This amazingness opens all links in a new tab. -->
      <script data-main="js/slides" src="js/require-1.0.8.min.js"></script>
    </head>
    <body style="opacity: 0">

    <slides class="layout-widescreen">

    <slide class="logoslide nobackground">
      <article class="flexbox vcenter">
        <span><img src="images/google_developers_logo.png"></span>
      </article>
    </slide>

    <slide class="title-slide segue nobackground">
      <aside class="gdbar"><img src="images/google_developers_icon_128.png"></aside>
      <!-- The content of this hgroup is replaced programmatically through the slide_config.json. -->
      <hgroup class="auto-fadein">
        <h1 data-config-title><!-- populated from slide_config.json --></h1>
        <h2 data-config-subtitle><!-- populated from slide_config.json --></h2>
        <p data-config-presenter><!-- populated from slide_config.json --></p>
      </hgroup>
    </slide>

    {% for slide in slides %}
    <slide class="{{ slide.class }}">
      <hgroup>
        <h1>{{ slide.h1 }}</h1>
        <h2>{{ slide.title }}</h2>
      </hgroup>
      <article>
      {{ slide.content }}
      </article>
    </slide>
    {% endfor %}

    <slide class="backdrop"></slide>

    </slides>

    <!--[if IE]>
      <script src="http://ajax.googleapis.com/ajax/libs/chrome-frame/1/CFInstall.min.js"></script>
      <script>CFInstall.check({mode: 'overlay'});</script>
    <![endif]-->
    </body>
    </html>

Em princípio, parece que a transformação não será tão complexa.

1. A especialização de ``rst2html5`` deve mudar o gabarito inicial do html5 gerado tal como o exemplo acima,
   preenchendo a seção ``<head>``.
#. o elemento ``document`` corresponde à seção ``slides``
#. ``section`` --> ``slide``

A transição ``----`` *não* poderá ser usada para indicar um novo slide.
Isto requereria uma mudança no *parser* que seria muito complicada.
Melhor criar uma *nova* diretiva ``slide`` para isso.


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

Caso 1
-------

::

    document
        section
            title
            content


para::

    document
        section
            header
                title
            article
                content


Caso 2
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
        section
            header
                hgroup
                    title h1
                    title h2
            article
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
        section
            header
                title
            article
                content

Ainda Falta
===========

1. Pra que serve o :code:`<slide class="backdrop"></slide>` ao final do :ref:`gabarito <io-2012-template>`?
#. como disponibilizar vários temas para o mesmo conjunto de slides?
