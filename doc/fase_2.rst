======
Fase 2
======

------------------
Javascript e Temas
------------------


Dada uma estrutura com o padrão::

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

qual o javascript adequado para mainpulá-lo em slides?


Manipulação de HTML5 em Slides
==============================

Existem várias bibliotecas para transformar o html em slides S5:

* `S6 <https://github.com/geraldb/s6>`_
* Apresentações do Google IO têm versões diferentes.

    * `io 2012 slides <http://io-2012-slides.googlecode.com>`_ | Google IO 2012
    * `html5wow <http://www.htmlfivewow.com>`_ | Google IO 2011
    * `The Web Can Do That <http://www.htmlfivecan.com>`_ | Google IO 2012
    * `html5slides <http://code.google.com/p/html5slides/>`_ | Modelo 2011

* `reveal.js <http://lab.hakim.se/reveal-js>`_ https://github.com/hakimel/reveal.js
* `DZSlides <http://paulrouget.com/dzslides/>`_
* `ShowOff <https://github.com/schacon/showoff>`_ is a Sinatra web app that reads simple configuration files for a presentation.
   It is sort of like a Keynote web app engine - think S5 + `Slidedown <https://github.com/nakajima/slidedown>`_.

É necessário analisar cada uma das alternativas e ver os pontos positivos e negativos
para poder escolher as melhores características disponíveis.

s6
==

S6 is a rewrite of Eric Meyer's S5 using the jQuery JavaScript library.

* Os exemplos apresentados não são bonitos. Usam muitos gradientes de gosto duvidoso.
* Parte de uma marcação baseada em textile ou markdown.

A estrutura dos slides em HTML5 baseia-se em uma seção contendo ``articles``:

.. code-block:: html

    <body>
    <section class="slides">
        <article class='cover'>
            <h1>
                Title Goes Here Up
                <br>
                To Two Lines
            </h1>
            <p>Carlos Ruby<br>November 11, 2011</p>
        </article>

        <article class='nobackground'>
            <h3>A slide with an embed + title</h3>
            <iframe src='http://slideshow.rubyforge.org'></iframe>
        </article>

        <article class='slide nobackground'>
            <iframe src='http://slideshow.rubyforge.org'></iframe>
        </article
    </section>
    </body>

* Os scripts estão divididos em várias partes pequenas.
  O que realmente manipula os slides é o `jquery.slideshow.js <https://github.com/geraldb/s6/blob/master/js/jquery.slideshow.js>`_

Avaliação Geral
---------------

Apesar de usar JQuery para realizar algumas seleções de elementos e até transições de slides,
o resultado não parece muito bom no geral.
Algumas melhorias e simplificações no código poderiam ter sido feitas na conversão para JQuery.

Não há muito o que aproveitar.


Google IOSlides
===============

* Usa transformações 3D e outros recursos avançados de CSS3.
* Várias ideias interessantes a serem aproveitadas, a começar pela estrutura dos slides.
* Todos slides começam escondidos devido a uma definição do CSS.
  O slide que é apresentado é que recebe uma propriedade para ser visível
* Usa a biblioteca requirejs_ para carregar os scripts mais rápido e na ordem correta.

Ideias Interessantes
--------------------

#. Destaque no código fonte
#. Miniaturas dos slides para navegação
#. Transição dos slides

Pontos Negativos
----------------

* Algumas operações não ficaram muito claras tais como o "overview".
* Algumas configurações estão definidas no código e não podem ser mudadas externamente,
  tais como a referência ao IO GoogleCode 2012.

Reveal.js
=========

* Uma implementação moderna, que usa recursos avançados de CSS3.
* O código javascript está bem documentado.
* Usa headjs_ para carregar os scripts na ordem correta.

Ideias Interessantes
--------------------

#. Impressão dos Slides
#. Miniaturas dos slides para navegação

Negativos
---------

* Permite que slides tenham outros slides internamente,
  resultando em uma navegação bidimensional.
  Isso torna a navegação mais confusa e menos linear.


DZSlides
========

Código simples e enxuto.

Ideias Interessantes
--------------------

* Navegação remota dos slides através do postMessage embedder.html
* Uma tela para o apresentador e outra para o público.
  A tela do apresentador contém um relógio, as notas, o slide atual e o próximo. onstage.html
* Resize através da transformação *scale*


Pontos Negativos
----------------

* Segue um padrão muito peculiar de HTML5.
  Não usa a seção <body> e mistura <style>, <script> e conteúdo no mesmo nível.



Implementação
=============

Comparação entre javascript loaders
-----------------------------------

requirejs_ e headjs_ são javascript loaders famosos, mas outros existem.
Particularmente, o yepnopejs_ parece ser bem interessante.

* http://www.netmagazine.com/features/essential-javascript-top-five-script-loaders
* http://www.peterbe.com/plog/requirejs-vs-headjs
* http://webification.com/12-javascript-loaders-to-speed-up-your-web-applications



Passos
======

#. Funcionalidade Básica
#. Temas
#. Aprimoramentos

    * Transições
    * Painel de controle
    * Impressão
    * Miniaturas
    * Novo estilo para o Pygments

#. Otimização e Portabilidade

    * Javascript Loaders
    * Modernizr
    * Touch Screen
    * Celulares, Tablets etc.
    * Fonts

#. Testes Automatizados??







Ainda Falta
===========

1. Pra que serve o :code:`<slide class="backdrop"></slide>` ao final do :ref:`gabarito <io-2012-template>`?
#. como disponibilizar vários temas para o mesmo conjunto de slides?

.. _requirejs : http://requirejs.org
.. _headjs: http://headjs.com/
.. _yepnopejs: http://yepnopejs.com/