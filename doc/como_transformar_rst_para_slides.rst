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







