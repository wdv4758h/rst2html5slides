======================
Fase 1 - rst2slideshow
======================

-------------------------------------------
Transformar o restructuredText em slideshow
-------------------------------------------


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

Veja :file:`../test/cases.py` para outros casos previstos.



Separadores de Slides
=====================

Um slide é delimitado por três maneiras diferentes:

#. Título. Um novo título começa uma nova seção, que corresponde a um novo slide.
#. Transição. ``----`` é um nó ``transition`` que corresponde à barra horizontal em html5 ``<hr />``.
#. Diretiva ``slide``. Ainda falta...