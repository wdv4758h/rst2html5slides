# -*- coding: utf-8 -*-

import math
from docutils.parsers.rst import Directive, directives

def _apply_data(slide, **kwargs):
    attribs = unicode(slide.attrib)
    if 'data-' not in attribs:
        slide(**kwargs)
    return

def linear(slides, incr_x, incr_y, parameter):
    '''
    Linear distribution
    '''
    x = 0
    for slide in slides:
        slide(data_x=x)
        x += incr_x

def square(slides, incr_x, incr_y, amount=None):
    amount = amount or 4
    x = 0
    y = -incr_y
    for index, slide in enumerate(slides):
        if not index % amount:
            x = 0
            y += incr_y
        _apply_data(slide, data_x=x, data_y=y)
        x += incr_x

def square2(slides, incr_x, incr_y, amount=None):
    amount = amount or 4
    incr_x = -incr_x
    x = 0
    y = -incr_y
    rotate_z = 179.9  # jmpress doesn't rotate clockwise when it is 180
    for index, slide in enumerate(slides):
        if not index % amount:
            x += incr_x
            y += incr_y
            incr_x = -incr_x
            rotate_z = rotate_z == 0 and 179.9 or 0
        x += incr_x
        _apply_data(slide, data_x=x, data_y=y, data_rotate_z=rotate_z)

def spiral(slides, incr_x, incr_y, radius=None):
    '''
    not working yet
    '''
    radius = radius or 1200
    incr_rotate = int(radius / 180. * math.pi)
    rotate = -incr_rotate
    for index, slide in enumerate(slides):
        x = int(math.cos(index) * radius)
        y = int(math.sin(index) * radius)
        z = int(math.log(index + 1) * radius)
        rotate += incr_rotate
        _apply_data(slide, data_x=x, data_y=y, data_z=z, data_rotate_x=rotate,
            data_rotate_y=(rotate + incr_rotate), data_rotate_z=33)
