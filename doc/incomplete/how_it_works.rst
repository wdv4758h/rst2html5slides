

Lessons Learned from Similar Projects
=====================================

.. list-table:: Similar Projects
    :header-rows: 1
    :widths: 15 20 15 30 30

    * - Project
      - Description
      - Presentation Type
      - Positive
      - Negative
    * - Hieroglyph_
      - based on Sphinx_
      - `Google HTML5 slides template`_
      - Good and extensive documentation
      - Sphinx is great for managing related documentation files,
        but it is overkill to independent presentations.
    * - `python-impress`_
      - based on Sphinx
      - impress.js
      - Brought up the idea of positioning functions such as :literal:`linear` and :literal:`grid`
      - The same critic to Sphinx applies here
    * - Hovercraft_
      - based on lxml to convert rst files to impress.js presentations
      - impress.js
      - * Good documentation and examples
        * Uses field lists (:literal:`:field: value`) instead of directives to specify
          slide and presentation parameters
        * SVG Path to positioning
      - lxml transformations seems unnatural to docutils' philosophy and harder to extend.

Lessons:

#. Sphinx is not necessary to a rst-to-presentation converter.
   Worse, it adds up an extra effort to be extended that is not worth to presentations.
#. Positioning functions are useful to create
   a standard slide distribution when you don't want to worry about it
#. Field lists are interesting to specify slide attributes.
#. All projects listed are tied to a specific presentation framework.
   They would be more flexible if they were framework agnostic.



.. [#] http://en.wikipedia.org/wiki/Lightweight_markup_language