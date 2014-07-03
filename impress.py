# -*- coding: utf-8 -*-

import math
from docutils.parsers.rst import Directive, directives

INCR_X = 1240
INCR_Y = 800

class Impress(Directive):
    '''
    Set impress global options
    '''
    final_argument_whitespace = True
    has_content = False
    option_spec = {
        'distribution': directives.unchanged,
        'incr_x': int,
        'incr_y': int,
    }

    opts = {
        'distribution': 'manual',
        'incr_x': INCR_X,
        'incr_y': INCR_Y,
    }

    def run(self):
        Impress.opts.update(self.options)
        return []


def manual(slides):
    pass

def linear(slides):
    '''
    Linear distribution
    '''
    x = 0
    incr_x = Impress.opts['incr_x']
    for slide in slides:
        slide(data_x=x)
        x += incr_x


def square(slides, amount=4):
    incr_x = Impress.opts['incr_x']
    incr_y = Impress.opts['incr_y']
    x = 0
    y = -incr_y
    for index, slide in enumerate(slides):
        if not index % amount:
            x = 0
            y += incr_y
        slide(data_x=x, data_y=y)
        x += incr_x


def square2(slides, amount=4):
    incr_x = -Impress.opts['incr_x']
    incr_y = Impress.opts['incr_y']
    x = 0
    y = -incr_y
    rotate_z = 180
    for index, slide in enumerate(slides):
        if not index % amount:
            incr_x = -incr_x
            y += incr_y
            rotate_z = rotate_z == 0 and 180 or 0
        slide(data_x=x, data_y=y, data_rotate_z=rotate_z)
        x += incr_x


def spiral(slides, radius=1200):
    incr_rotate = (radius / 180. * math.pi)
    rotate = -incr_rotate
    for index, slide in enumerate(slides):
        x = math.cos(index) * radius
        y = math.sin(index) * radius
        z = math.log(index) * radius
        rotate += incr_rotate
        slide(data_x=x, data_y=y, data_z=z, data_rotate_x=rotate, data_rotate_y=rotate, data_rotate_z=rotate)
