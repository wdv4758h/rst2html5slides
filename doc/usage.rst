=====
Usage
=====

rst2html5slides extends rst2html5_ to generate a deck of slides from a reStructuredText file
that can be used with any web presentation framework
such as `impress.js`_, `jmpress.js`_ or `deck.js`_.

rst2html5slides source is located at http://bitbucket.org/andre_felipe_dias/rst2html5slides
but you can install it with pip:

.. code-block:: bash

    $ pip install rst2html5slides

Later,
you will also need to install or download the chosen web presentation framework.
For now,
let's concentrate on making presentations.

.. important::

    Before proceeding,
    it is important that you already know reStructuredText basic syntax.
    I'd like to suggest two links:

    * `The official reStructuredText Primer <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_
    * `The Sphinx reStructuredText Primer <http://sphinx-doc.org/rest.html>`_


Making Presentations
====================

By default,
every section of a reStructuredText (rst) document becomes a slide.
A typical presentation in reStructuredText (rst) has the following pattern:

.. code-block:: rst

    Topic 1
    =======

    * Item A
    * Item B


    Topic 2
    =======

    * Item C
    * Item D

When converted by rst2html5slides,
the result is:

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
    </head>
    <body>
    <deck>
        <slide id="topic-1">
            <header>
                <h1>Topic 1</h1>
            </header>
            <section>
                <ul>
                    <li>Item A</li>
                    <li>Item B</li>
                </ul>
            </section>
        </slide>
        <slide id="topic-2">
            <header>
                <h1>Topic 2</h1>
            </header>
            <section>
                <ul>
                    <li>Item C</li>
                    <li>Item D</li>
                </ul>
            </section>
        </slide>
    </deck>
    </body>
    </html>

.. note::

    Note that both :literal:`<deck>` and :literal:`<slide>` are custom HTML tags.
    The former wraps all slides while the latter wraps each slide.
    You can style and select them in CSS and Javascript
    but you also can change them
    if prefer or need to
    :ref:`adapt your presentation to a framework or stylesheet <adapting your presentation>`.


A rst section is initiated by a title of any level,
but in rst2html5slides, only sections from the highest level become slides:

.. code-block:: rst

    Slide 1
    =======

    Slide contents

    Slide 2
    =======

    Subtitle
    --------

    * item A
    * item B

will be translated to:

.. code-block:: html

    ...
    <body>
    <deck>
        <slide id="slide-1">
            <header>
                <h1>Slide 1</h1>
            </header>
            <section>Slide contents</section>
        </slide>
        <slide id="slide-2">
            <header>
                <h1>Slide 2</h1>
                <h2>Subtitle</h2>
            </header>
            <section>
                <ul>
                    <li>item A</li>
                    <li>item B</li>
                </ul>
            </section>
        </slide>
    </deck>
    </body>
    </html>

You are not limited to section titles, paragraphs and lists.
All other reStructuredText constructs are available to your presentation
such as `images <http://docutils.sourceforge.net/docs/ref/rst/directives.html#images>`_,
`tables <http://docutils.sourceforge.net/docs/ref/rst/directives.html#tables>`_,
`code-blocks <http://docutils.sourceforge.net/docs/ref/rst/directives.html#code>`_
etc.


Untitled Slides
===============

Sometimes, you might want an untitled slide.
This can be accomplished using a
`transition marker <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#transitions>`_:

.. code-block:: rst

    Untitled slide 1

    ----

    Untitled slide 2

    ----

    Untitled slide 3

which becomes:

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
    </head>
    <body>
    <deck>
        <slide>
            <section>Untitled slide 1</section>
        </slide>
        <slide>
            <section>Untitled slide 2</section>
        </slide>
        <slide>
            <section>Untitled slide 3</section>
        </slide>
    </deck>
    </body>
    </html>


Some Useful reStructuredText Directives to Presentations
========================================================

reStructuredText has two useful directives to register some document metadata directly
into the HTML head section:
`title <http://docutils.sourceforge.net/docs/ref/rst/directives.html#metadata-document-title>`_
and `meta <http://docutils.sourceforge.net/docs/ref/rst/directives.html#meta>`_:

.. code-block:: rst

    .. title:: My Presentation Title
    .. meta::
        :author: André Felipe Dias
        :keywords: mercurial, web presentation, rst2html5slides

which translates to:

.. code-block:: html
    :emphasize-lines: 6, 7

    <!DOCTYPE html>
    <html>
    <head>
        <title>My Presentation Title</title>
        <meta charset="utf-8" />
        <meta content="André Felipe Dias" name="author" />
        <meta content="mercurial, web presentation, rst2html5slides" name="keywords" />
    </head>
    <body></body>
    </html>

Another important directive is
`class <http://docutils.sourceforge.net/docs/ref/rst/directives.html#class>`_,
which sets the "class" attribute value on its content
or on the first immediately following non-comment element.
When making presentations,
you use :literal:`class` directive to set the class of a slide:

.. code-block:: rst
    :linenos:
    :emphasize-lines: 1, 9, 18

    .. class:: logo-background

    Topic X
    =======

    paragraph


    .. class:: section-title

    ----

    New Chapter

    Topic Y
    =======

    .. class:: hint

    * This also works
    * Substructure here


which translates to:

.. code-block:: html
    :linenos:
    :emphasize-lines: 3, 9, 17

    ...
    <deck>
        <slide class="logo-background" id="topic-x">
            <header>
                <h1>Topic X</h1>
            </header>
            <section>paragraph</section>
        </slide>
        <slide class="section-title">
            <section>New Chapter</section>
        </slide>
        <slide id="topic-y">
            <header>
                <h1>Topic Y</h1>
            </header>
            <section>
                <ul class="hint">
                    <li>This also works</li>
                    <li>Substructure here</li>
                </ul>
            </section>
        </slide>
    </deck>
    ...


Slide Attributes
================

Slide attributes are set via rst fields declared just **above the desired slide**.
There is no restriction on field name or value.
They are directly included as slide tag attributes.
Example:

.. code-block:: rst

    :id: Opening
    :data-x: 1000
    :data-y: 500
    :data-scale: 3

    Presentation Opening

resulting in:

.. code-block:: html

    ...
    <deck>
        <slide data-y="500" data-x="1000" id="Opening" data-scale="3">
            <section>Presentation Opening</section>
        </slide>
    </deck>
    ...


Manual Positioning of Slides
============================

You can position slides manually through :literal:`data-*` attributes
which are used by `impress.js`_ and `jmpress.js`_ to set the position/zoom/rotation of a slide.
The most common fields are:

.. extracted from Hovercraft's documentation

* :literal:`data-x`: The horizontal position of a slide in pixels. Can be negative.
* :literal:`data-y`: The vertical position of a slide in pixels. Can be negative.
* :literal:`data-z`: This controls the position of the slide on the z-axis.
  Setting this value to -3000 means it’s positioned -3000 pixels away.
  This is only useful when you use data-rotate-x or data-rotate-y,
  otherwise it will only give the impression that the slide is made smaller,
  which isn’t really useful.
* :literal:`data-scale`: Sets the scale of a slide, which is what creates the zoom.
  Defaults to 1. A value of 4 means the slide is four times larger.
  In short: Lower means zooming in, higher means zooming out.
* :literal:`data-rotate-x`: The rotation of a slide in the x-axis, in degrees.
  This means you are moving the slide in a third dimension compared with other slides.
  This is generally cooll effect, if used right.
* :literal:`data-rotate-y`: The rotation of a slide in the x-axis, in degrees.
* :literal:`data-rotate-z`: The rotation of a slide in the x-axis, in degrees.
  This will cause the slide to be rotated clockwise or counter-clockwise.
* :literal:`data-rotate`: The same as data-rotate-z.

Unless there is an automatic distribution function defined,
the same set of :literal:`data-*` attributes are applied to the following slides
until you overwrite some of their values.
For example:

.. code-block:: rst

    :data-x: 1000
    :data-y: 1000

    slide 1

    :data-x: 2000

    ----

    slide 2

    :data-y: -1000

    ----

    slide 3


results in:

.. code-block:: html

    ...
    <deck>
        <slide data-x="1000" data-y="1000">
            <section>slide 1</section>
        </slide>
        <slide data-x="2000" data-y="1000">
            <section>slide 2</section>
        </slide>
        <slide data-x="2000" data-y="-1000">
            <section>slide 3</section>
        </slide>
    </deck>
    ...

Note that :literal:`slide 2` kept the same :literal:`data-y` value from :literal:`slide 1`
and :literal:`slide 3` has the same :literal:`data-x` value from :literal:`slide 2`.

.. attention::

    Positional attributes must be declared above the desired slide.
    So, :literal:`:data-x: 2000` refers to :literal:`slide 2`
    while :literal:`:data-y: -1000` changes :literal:`slide 3`.


Automatic Positioning of Slides
===============================

Manual positioning is annoying if all you need is a simple presentation.
In such cases,
you should use one of the automatic distribution functions provided by :literal:`rst2html5slides`.
For the time being, there are three functions available:

#. :literal:`linear`: horizontal distribution by regular increments of :literal:`data-x`.
#. :literal:`grid`: similar to linear, but a new line is created at every 4 slides.
   This number can be changed passing an additional parameter.
#. :literal:`grid_rotate`: similar to :literal:`grid`,
   but the slide is rotated in 180 degrees when line changes.

To define an automatic positioning function,
use a presentation directive at the beginning of the presentation:

.. code-block:: rst

    .. presentation
        :distribution: grid 2

    slide 1

    ----

    slide 2

    ----

    slide 3

which translates to:

.. code-block:: html

    ...
    <deck>
        <slide data-x="0">
            <section>slide 1</section>
        </slide>
        <slide data-x="1600">
            <section>slide 2</section>
        </slide>
        <slide data-y="1600" data-x="0">
            <section>slide 3</section>
        </slide>
    </deck>
    ...


.. tip::

    :literal:`grid 1` makes a column.


Increment Values
----------------

The default value for increment :literal:`data-x` and :literal:`data-y` is 1600.
To change this, specify different values with :literal:`increment` attribute
declaring one or two values (see the next section for an example).
A single value will be applied to both :literal:`data-x` and :literal:`data-y`.


Interfering on Automatic Positioning
====================================

Even using automatic positioning,
you can change the position of one slide setting some :literal:`data-*` attributes.
The automatic distribution will restart from this slide.

Example:

.. code-block:: rst

    .. presentation::
        :distribution: grid_rotate 2
        :increment: 1000 800

    slide 1

    :data-x: -500
    :data-y: -1000
    :data-scale: 3
    :data-rotate-z: 90

    ----

    The automatic positioning restarts at this slide
    due to its custom positioning

    ----

    Same line yet

    ----

    New line, with rotation

resulting in:

.. code-block:: html

    ...
    <deck>
        <slide data-x="0" data-rotate-z="0">
            <section>slide 1</section>
        </slide>
        <slide data-y="-1000" data-x="-500" data-rotate-z="90" data-scale="3">
            <section>The automatic positioning restarts at this slide due to its custom positioning</section>
        </slide>
        <slide data-y="-1000" data-x="500" data-rotate-z="90" data-scale="3">
            <section>Same line yet</section>
        </slide>
        <slide data-y="-200" data-x="500" data-rotate-z="269.9" data-scale="3">
            <section>New line, with rotation</section>
        </slide>
    </deck>
    ...


.. _adapting your presentation:

Adapting to a Presentation Framework
====================================

Each presentation framework has its particularities or choices regarding style and structure of slides,
but  it is not always necessary to change the structure of a raw rst2html5slides translation.
For example, `jmpress.js`_ is rather flexible.
You could configuring it to accept a :literal:`deck` tag as the root element and
:literal:`slide` tags as steps:

.. code-block:: javascript

    $(function() {
        $('deck').jmpress({
            stepSelector: 'slide'
        });
    });

rst2html5slides translations can also be used unchanged in `deck.js`_:

.. code-block:: javascript

    $(function() {
        $.deck("slide");
    });


Adjusting Presentation Structure
--------------------------------

You might want to change the rst2html5slides default structure
to adapt its result to a framework structure or to an existent style.
For example,
`impress.js` expects a presentation strictly follow the structure:

.. code-block:: html

    <body>
        <div id="impress">
            <div class="step">
                ...
            </div>
            <div class="step">
                ...
            </div>
            ...
        </div>
    </body>

rst2html5slides result structure can be configured
by :literal:`--deck-selector` and :literal:`--slide-selector` parameters
or by a :literal:`presentation` directive
with :literal:`deck_selector` and :literal:`slide_selector` options.
To configure rst2html5slides to conform to impress.js
you can use:

.. code-block:: bash

    $ rst2html5slides --deck-selector 'div#impress' --slide-selector 'div.step' ...

or

.. code-block:: rst

    .. presentation::
        :deck_selector: div#impress
        :slide_selector: div.step

.. tip::

    Follow the CSS selector format to specify tag, class and id.


Templates
---------

Just changing HTML structure isn't enough.
You also need to include all framework files in presentations.
One way is passing parameters to rst2html5slides:

* :literal:`--script`
* :literal:`--script-defer`
* :literal:`--stylesheet`

Example:

.. code-block:: bash

    $ rst2html5slides.py \
        --stylesheet jmpress.css \
        --script http://code.jquery.com/jquery-latest.min.js \
        --script jmpress.js \
        --script-defer jmpress_init.js \
        --deck-selector '#jmpress' \
        example.rst example.html

However,
the simplest way is through templates
where all necessary links, scripts and even additional constructs are already declared
and the job of rst2html5slides is just filling in the contents of the presentation.
Example:

.. code-block:: html

    <!DOCTYPE html>
    <html {html_attr}>
    <head>
        <!-- styles and scripts for a jmpress.js presentation -->
        <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport" />
        <link href="css/jmpress.css" rel="stylesheet" />
        <link href="css/default.css" rel="stylesheet" />
        <link href="css/pygments.css" rel="stylesheet" />
        <script src="http://code.jquery.com/jquery-latest.min.js"></script>
        <script src="js/jmpress.js"></script>
        <script src="js/jmpress_init.js" defer="defer"></script>
        {head}
    <body>{body}
    <div class="hint">
        <p>Use a spacebar or arrow keys to navigate</p>
    </div>
    </body>
    </html>

.. code-block:: bash

    $ rst2html5slides --template jmpress_template.html example.rst example.html

