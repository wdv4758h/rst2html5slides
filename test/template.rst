.. role:: raw-html(raw)
    :format: html

.. class:: title-slide segue nobackground

Title goes here :raw-html:`<br />` Up two lines
-----------------------------------------------

Subtitle goes here
~~~~~~~~~~~~~~~~~~~

..

Slide with Bullets
------------------

-  Titles are formatted as Open Sans with bold applied and font size is
   set at 45
-  Title capitalization is title case

   -  Subtitle capitalization is title case

-  Subtitle capitalization is title case
-  Titles and subtitles should never have a period at the end

Slide with Bullets that Build
-----------------------------

Subtitle Placeholder
~~~~~~~~~~~~~~~~~~~~

A list where items build:

-  Pressing 'h' highlights code snippets
-  Pressing 'p' toggles speaker notes (if they're on the current slide)
-  Pressing 'f' toggles fullscreen viewing
-  Pressing 'w' toggles widescreen
-  Pressing 'o' toggles overview mode
-  Pressing 'ESC' toggles off these goodies

Another list, but items fade as they build:

-  Hover over me!
-  Hover over me!
-  Hover over me!

Slide with (Smaller Font)
-------------------------

-  All `links <http://www.google.com>`_ open in new tabs.
-  To change that this, add ``target="_self"`` to the link.

Hidden slides are left out of the presentation.

Code Slide (with Subtitle Placeholder)
--------------------------------------

Subtitle Placeholder
~~~~~~~~~~~~~~~~~~~~

Press 'h' to highlight important sections of code (wrapped in ``<b>``).

.. code-block:: javascript

    <script type='text/javascript'>
      // Say hello world until the user starts questioning
      // the meaningfulness of their existence.
      function helloWorld(world) {
        for (var i = 42; --i >= 0;) {
          alert('Hello ' + String(world));
        }
      }
    </script>


.. slide::
    :title: Code Slide (Smaller Font)
    :contents_class: smaller

.. code-block:: javascript

    // Say hello world until the user starts questioning
    // the meaningfulness of their existence.
    function helloWorld(world) {
      for (var i = 42; --i >= 0;) {
        alert('Hello ' + String(world));
      }
    }

.. code-block:: css

    <style>
      p { color: pink }
      b { color: blue }
    </style>

.. code-block:: html

    <!DOCTYPE html>
    <html>
        <head>
            <title>My Awesome Page</title>
        </head>
        <body>
            <p>Hello world</p>
        <body>
    </html>


Slide with Image
----------------

.. image:: chart.png

.. slide::
    :title: Slide with Image (Centered horz/vert)
    :contents_class: flexbox vcenter

.. image:: barchart.png

Table Option A
--------------

Subtitle Placeholder
~~~~~~~~~~~~~~~~~~~~

.. role:: highlight
    :class: highlight

+---------+---------------+---------------+--------------------------+---------------+
|         | Column 1      | Column 2      | Column 3                 | Column 4      |
+=========+===============+===============+==========================+===============+
| Row 1   | placeholder   | placeholder   | :highlight:`placeholder` | placeholder   |
+---------+---------------+---------------+--------------------------+---------------+
| Row 2   | placeholder   | placeholder   | placeholder              | placeholder   |
+---------+---------------+---------------+--------------------------+---------------+
| Row 3   | placeholder   | placeholder   | placeholder              | placeholder   |
+---------+---------------+---------------+--------------------------+---------------+
| Row 4   | placeholder   | placeholder   | placeholder              | placeholder   |
+---------+---------------+---------------+--------------------------+---------------+
| Row 5   | placeholder   | placeholder   | placeholder              | placeholder   |
+---------+---------------+---------------+--------------------------+---------------+

Table Option A (Smaller Text)
-----------------------------

Subtitle Placeholder
~~~~~~~~~~~~~~~~~~~~

.. class:: smaller

+---------+---------------+---------------+---------------+---------------+
|         | Column 1      | Column 2      | Column 3      | Column 4      |
+=========+===============+===============+===============+===============+
| Row 1   | placeholder   | placeholder   | placeholder   | placeholder   |
+---------+---------------+---------------+---------------+---------------+
| Row 2   | placeholder   | placeholder   | placeholder   | placeholder   |
+---------+---------------+---------------+---------------+---------------+
| Row 3   | placeholder   | placeholder   | placeholder   | placeholder   |
+---------+---------------+---------------+---------------+---------------+
| Row 4   | placeholder   | placeholder   | placeholder   | placeholder   |
+---------+---------------+---------------+---------------+---------------+
| Row 5   | placeholder   | placeholder   | placeholder   | placeholder   |
+---------+---------------+---------------+---------------+---------------+

Table Option B
--------------

Subtitle Placeholder
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :stub-columns: 1
    :class: rows

    Header 1, placeholder, :highlight:`placeholder`, placeholder
    Header 2, placeholder, placeholder, placeholder
    Header 3, placeholder, placeholder, placeholder
    Header 4, placeholder, placeholder, placeholder
    Header 5, placeholder, placeholder, placeholder


Slide Styles
------------

.. role:: red
    :class: red

.. role:: green
    :class: green

.. role:: yellow
    :class: yellow

.. role:: blue
    :class: blue

.. role:: gray
    :class: gray:

-  :red:`class="red"`
-  :blue:`class="blue"`
-  :green:`class="green"`
-  :yellow:`class="yellow"`
-  :gray:`class="gray"`

I am centered text with a Button and Disabled button.

.. figure:: images/google_developers_icon_128.png
   :align: center
   :alt:

.. class:: segue dark nobackground

Segue Slide
-----------

Subtitle Placeholder
~~~~~~~~~~~~~~~~~~~~

.. slide::
    :class: fill nobackground
    :title: Full Image (with Optional Header)

www.flickr.com/photos/25797459@N06/5438799763/

.. slide::
    :class: segue dark quote nobackground
    :contents_class: flexbox vleft auto-fadein

.. epigraph::

    This is an
    example of quote text.


.. slide::
    :class: thank-you-slide segue nobackground
    :title: Thank You!

.. figure:: images/google_developers_icon_128.png
   :align: center
   :alt:

Contato:

.. csv-table::
    :stub-columns: 1
    :class: contact

    g+, plus.google.com/1234567890
    twitter, @yourhandle
    www, www.you.com
    github, github.com/you

.. figure:: images/google_developers_logo_white.png
   :align: center
   :alt:

.. |Description| image:: chart.png
.. |image3| image:: barchart.png