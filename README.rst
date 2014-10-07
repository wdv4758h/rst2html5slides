===============
rst2html5slides
===============

rst2html5slides extends rst2html5_ to generate a deck of slides from a reStructuredText file
that can be used with any web presentation framework
such as `impress.js`_, `jmpress.js`_ or `deck.js`_.


Usage
=====

.. code-block:: bash

    $ rst2html5slides [options] SOURCE DEST

Options:

--distribution=<function_name>
                        Specify the name of the slide distribution function.
                        Options are "linear", "grid" or "grid-rotate". An
                        additional parameter can be specified along with the
                        name such as in "grid_rotate  3".
--increment=<increment>
                        Specify the value of the increment used by the
                        distribution functions. To specify different values
                        for X and Y increments, separate them by space.
                        Example "1000 500". Default value is 1600 for X and Y
                        increments.
--manual-slide-id       Disable slide automatic identification based on title.
--deck-selector=<deck_selector>
                        Specify the tag, id and/or class to replace the
                        default (and non-standard) <deck> tag used to surround
                        the slides. Follow the pattern tag#id.class (such as a
                        CSS selector). Examples: div, div#impress, div.deck-
                        container, article#impress.impress-not-supported
--slide-selector=<slide_selector>
                        Specify the tag, id and/or class to replace the
                        default (and non-standard) <slide> tag used to surround
                        each slide.Follow the pattern tag#id.class (such as a
                        CSS selector)Examples: div.slide, section, div.step

.. tip::

    Other options inherited from rst2html5_ like :literal:`--stylesheet`, :literal:`--script`,
    :literal:`--script-defer` and :literal:`--template`
    are particularly important to make the rst presentation fit the chosen presentation framework.


Features
========

* Agnostic to any specific presentation framework.
  rst2html5slides generates suitable content to any presentation framework,
  but does not provide any of the other necessary stylesheet or javascript files.
* Presentations are easy to read and write as a plain text file
* Slides can be manually or automatically positioned through pre-defined functions
* Separation between content and design details


Example
=======

:literal:`presentation.rst`:

.. code-block:: rst

    .. title:: Simple Presentation | rst2html5slides
    .. meta::
      :author: André Felipe Dias

    .. class:: context

    Presentation
    ============

    Author
    ------

    Topic 1
    =======

    * item A
    * item B

    Topic 2
    =======

    * item C
    * item D


rst2html5slides doesn't provide any specific web presentation framework files.
You must already have them in place and use rst2html5slides to fill in presentation contents.
The simplest way is passing a template as parameter.
:literal:`jmpress_template.html`:

.. code-block:: html

    <!DOCTYPE html>
    <html{html_attr}>
    <head>{head}
        <!-- styles and scripts for a jmpress.js presentation -->
        <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport" />
        <link href="css/default.css" rel="stylesheet" />
        <link href="css/pygments.css" rel="stylesheet" />
        <link href="css/impress.css" rel="stylesheet" />
        <script src="http://code.jquery.com/jquery-latest.min.js"></script>
        <script src="js/jmpress.js"></script>
    <body>{body}
    <script>
    $(function() {{
        $('deck').jmpress({{
            stepSelector: 'slide'
        }});
    }});
    </script>
    </body>
    </html>

.. note::

    You must double curly braces when coding javascript directly in templates.
    To avoid this, keep all scripts in external files.
    In the previous template,
    the jmpress initialization could be placed in an external file included via
    :literal:`<script defer="defer" src="jmpress_init.js"></script>`.

rst2html5slides command:

.. code-block:: bash

    rst2html5slides --template jmpress_template.html \
                    --distribution linear \
                    presentation.rst presentation.html

:literal:`presentation.html`:

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Presentation | rst2html5slides</title>
        <meta charset="utf-8" />
        <meta content="André Felipe Dias" name="author" />

        <!-- styles and scripts for a jmpress.js presentation -->
        <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport" />
        <link href="css/default.css" rel="stylesheet" />
        <link href="css/pygments.css" rel="stylesheet" />
        <link href="css/impress.css" rel="stylesheet" />
        <script src="http://code.jquery.com/jquery-latest.min.js"></script>
        <script src="js/jmpress.js"></script>
    <body>
    <deck>
        <slide class="context" id="presentation" data-x="0">
            <header>
                <h1>Presentation</h1>
                <h2>Author</h2>
            </header>
        </slide>
        <slide id="topic-1" data-x="1600">
            <header>
                <h1>Topic 1</h1>
            </header>
            <section>
                <ul>
                    <li>item A</li>
                    <li>item B</li>
                </ul>
            </section>
        </slide>
        <slide id="topic-2" data-x="3200">
            <header>
                <h1>Topic 2</h1>
            </header>
            <section>
                <ul>
                    <li>item C</li>
                    <li>item D</li>
                </ul>
            </section>
        </slide>
    </deck>

    <script>
    $(function() {
        $('deck').jmpress({
            stepSelector: 'slide'
        });
    });
    </script>
    </body>
    </html>


Documentation
=============

Full documentation is available at readthedocs.org and also in the :literal:`doc` subdirectory.


Source
======

rst2html5slides source is located at http://bitbucket.org/andre_felipe_dias/rst2html5slides


Installing rst2html5slides
==========================

.. code-block:: bash

    pip install rst2html5slides


License
=======

rst2html5slides is made available under a MIT license.

Included slide CSS and JavaScript are based on JQuery_, `impress.js`, `jmpress.js`_
and `deck.js`_ projects also licensed under MIT License.


.. _rst2html5: https://pypi.python.org/pypi/rst2html5
.. _impress.js: http://github.com/bartaz/impress.js
.. _jmpress.js: http://jmpressjs.github.io/jmpress.js/
.. _deck.js: http://imakewebthings.com/deck.js/