Examples
========

.. important::

    All plataform files (such as `deck.js`_ or `jmpress.js`_) are supposed to be already downloaded
    at :code:`css` and :code:`javascript` directories.


1. simple.rst
-------------

A simple presentation with 4 slides.
One of them has a subtitle and another one doesn't have a title.


.. literalinclude:: examples/simple.rst
    :language: rst

To convert it to a deck presentation,
there is no additional adjustments needed since deck.js follows a linear flow.
The command to build it is shown below:

.. literalinclude:: examples/build.sh
    :language: bash
    :lines: 7-9

You can see the result `here <examples/simple_deck.html>`_.

To build a jmpress/impress presentation,
it is necessary to define some sort of positional distribution.
Fortunately, :code:`rst2html5slides` provides a few default functions.
The command to build a jmpress presentation from the same previous simple presentation is:

.. literalinclude:: examples/build.sh
    :language: bash
    :lines: 13-19

See the result: `simple_jmpress.html <examples/simple_jmpress.html>`_.


2. jmpress.rst
--------------

Impress.js has a nice `demo presentation <http://bartaz.github.io/impress.js/#/bored>`_
that shows how it works.
Jmpress.js also has the `same presentation <http://jmpressjs.github.io/jmpress.js/examples/impress/#/bored>`_.
Now, rst2html5slides shows how to produce that presentation from a reStructuredText file:

.. literalinclude:: examples/jmpress.rst
    :language: rst

You can build it using a template:

.. literalinclude:: examples/build.sh
    :language: bash
    :lines: 24-26

or via parameters:

.. literalinclude:: examples/build.sh
    :language: bash
    :lines: 32-38

The `first <examples/jmpress_via_template.html>`_ and
the `second <examples/jmpress_via_parameters.html>`_ generated files are equivalent
and pretty close to the originals, aren't they?

.. _impress.js: http://github.com/bartaz/impress.js
.. _jmpress.js: http://jmpressjs.github.io/jmpress.js/
.. _deck.js: http://imakewebthings.com/deck.js/
