.. presentation::
    :distribution: linear
    :increment: 1000 800

.. title:: Positioning Tutorial


Positioning
===========

The best way to positioning slides is combining automatic distribution function and
manual positioning of some specific slides to get custom effects.


Automatic Distribution
======================

There are three distribution functions available:
:literal:`linear`, :literal:`grid` and :literal:`grid_rotate`.
You can specify one of them through a :literal:`--distribution` parameter or a rst directive:

.. code-block:: rst

    .. presentation:: grid 3
        :increment: 1000 800


Manual Positioning
==================

Regardless of an automatic distribution or not,
any slide can be manually positioned using :literal:`data-` fields just before the slide.

The general pattern is:

.. code-block:: rst

    :data-field-1: value
    :data-field-2: value

    slide title or body


Data Fields
===========

Any field starting with :literal:`data-` will be converted to a :literal:`data-` attribute.
There is no filtering.

Common data-fields are::

    data-x          Position on the X-axis
    data-y          Position on the Y-axis
    data-z          Position on the Z-axis (which means 3D!)
    data-rotate     Rotation in degrees
    data-rotate-z   An alias for data-rotate
    data-rotate-x   Rotation on the X-axis, which again means 3D effects
    data-rotate-y   Rotation on the Y-axis
    data-scale      The size of the slide, which means zooming effects

Let's do some zoom and rotate!


:data-scale: 5
:data-rotate: 90
:data-y: 6000

Zoom out!
=========

So here we rotated 90 degrees and zoomed out five times.


:data-x: -4000

Sticky data!
============

All fields are "sticky!"
That means that they keep the same value as the last slide. So this slide will
keep the 90 degree rotation and scale of 5.

But I set the X position to -4000, so we now move on the X-scale instead.
Negative numbers are not a problem.

It needs to be -4000 now, since we zoomed out five times. That means that the
ordinary presentation size of 1024*800 pixels are now 5120*400 pixels
(assuming you use a 4:3 screen size).


Like this
=========

You just prefix the position with an ``r`` and it becomes relative. That
means that if the previous slide moves, this moves with it. You'll find that
it's generally good practice to use mostly relative positioning if you are
still flexible about what your slides are and what they should say or
in which order.

For some types of presentation, where typography is important, you need to
decide everything that the slide should say and their position from the
start. Then absolute positioning works fine. But otherwise you probably want
to use relative positioning.


:data-scale: 0.15
:data-y: -275
:data-x: 150
:data-rotate: -90

**A warning!**
==============


:data-x: 1000
:data-scale: 1

Didn't that slide look good?
============================

Don't worry, when you make big zooms, different browsers will behave
differently and be good at different things. Some will be slow and jerky on
the 3D effects, and others will show fonts with jagged edges when you zoom.
Older and less common browsers can also have problems with 3D effects.



3D!
===

Now it gets complicated!



:data-rotate-y: 0
:data-y: 100
:data-x: -1000

3D Rotation
===========

We have already seen how we can rotate the slide with ``:data-rotate:``. This is actually rotation
in the Z-axis, so you can use ``:data-rotate-z:`` as well, it's the same thing.
But you can also rotate in the Y-axis.



:data-x: 0
:data-y: 0
:data-rotate-y: 90

3D Rotation
===========

That was a 90 degree rotation in the Y-axis.
Let's go back.


:data-x: 0
:data-y: 0
:data-rotate-y: 0


:data-x: -1000
:data-y: 0
:data-rotate-y: 0

3D Rotation
===========

Notice how the text was invisible before the rotation?
The text is there, but it has no depth, so you can't see it.
Of course, the same happens in the X-axis.


:data-x: 0
:data-y: 0
:data-rotate-x: 90

3D Rotation
===========

That was a 90 degree rotation in the X-axis.
Let's go back.


:data-x: 0
:data-y: 0
:data-rotate-x: 0


:data-x: -1000

3D Positioning
==============

You can not only rotate in all three dimensions, but also position in all
three dimensions. So far we have only used ``:data-x`` and ``:data-y``, but
there is a ``:data-z`` as well.


:data-z: 1000
:data-x: 0
:data-y: 0

Z-space
=======


:data-x: 0
:data-y: -500

Z-space
=======

This can be used for all sorts of interesting effects. It should be noted
that the depth of the Z-axis is quite limited in some browsers.

If you set it too high, you'll find the slide appearing low and upside down.


:data-x: 800
:data-y: 0

Z-space
=======

But well used it can give an extra wow-factor,


:data-z: 0
:data-x: 0
:data-y: 200
:data-scale: 2

and have text pop out at you!



:data-x: 3000
:data-y: 1500
:data-scale: 15
:data-rotate-z: 0
:data-rotate-x: 0
:data-rotate-y: 0
:data-z: 0


That's all for now
==================

*Have fun!*


.. This tutorial is available as `source code <../_sources/examples/positioning.txt>`_.
.. based on hovercraft's example
   (https://hovercraft.readthedocs.org/en/1.0/_sources/examples/positions.txt)


.. _jmpress.js: http://jmpressjs.github.io/jmpress.js/
