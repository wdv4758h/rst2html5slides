#!/bin/bash

# Commands to generate html from rst sources:

# Simple presentation using deck.js

rst2html5slides \
    --template templates/deck-template.html \
    simple.rst simple_deck.html

# Simple presentation using jmpress

rst2html5slides \
    --template templates/jmpress_template.html \
    --stylesheet 'css/simple.css' \
    --deck-selector 'div#jmpress' \
    --slide-selector 'div.step' \
    --distribution linear \
    simple.rst simple_jmpress.html


# impress/jmpress demo via template

rst2html5slides \
    --template templates/jmpress_template.html \
    jmpress.rst jmpress_via_template.html


# impress/jmpress demo via parameters
# the final result is the same of the previous command

rst2html5slides \
    --stylesheet "http://fonts.googleapis.com/css?family=Open+Sans:regular,semibold,italic,italicsemibold|PT+Sans:400,700,400italic,700italic|PT+Serif:400,700,400italic,700italic" \
    --stylesheet css/impress.css \
    --script http://code.jquery.com/jquery-latest.min.js \
    --script js/jmpress/jmpress.js \
    --script-defer js/jmpress/jmpress_init.js \
    jmpress.rst jmpress_via_parameters.html

exit 0
