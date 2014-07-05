# -*- coding: utf-8 -*-

import math
from docutils.parsers.rst import Directive, directives

INCR_X = 1500
INCR_Y = 800

class Distribution(Directive):
    '''
    Set distribution global options
    '''
    required_arguments = 1
    final_argument_whitespace = False
    has_content = False
    option_spec = {
        'incr_x': int,
        'incr_y': int,
        'parameter': int,
    }
    _default_opts = {
        'distribution': 'manual',
        'incr_x': INCR_X,
        'incr_y': INCR_Y,
    }
    opts = _default_opts.copy()
    slides_distribution = 'manual'

    @classmethod
    def reset(cls):
        Distribution.opts = Distribution._default_opts.copy()
        Distribution.slides_distribution = 'manual'
        return

    def run(self):
        self.reset()
        Distribution.slides_distribution = self.arguments[0]
        Distribution.opts.update(self.options)
        return []


def manual(slides, parameter):
    pass

def linear(slides, parameter):
    '''
    Linear distribution
    '''
    x = 0
    incr_x = Distribution.opts['incr_x']
    for slide in slides:
        slide(data_x=x)
        x += incr_x

def square(slides, amount=None):
    amount = amount or 4
    incr_x = Distribution.opts['incr_x']
    incr_y = Distribution.opts['incr_y']
    x = 0
    y = -incr_y
    for index, slide in enumerate(slides):
        if not index % amount:
            x = 0
            y += incr_y
        slide(data_x=x, data_y=y)
        x += incr_x

def square2(slides, amount=None):
    amount = amount or 4
    incr_x = -Distribution.opts['incr_x']
    incr_y = Distribution.opts['incr_y']
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
        slide(data_x=x, data_y=y, data_rotate_z=rotate_z)

def spiral(slides, radius=None):
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
        slide(data_x=x, data_y=y, data_z=z, data_rotate_x=rotate, data_rotate_y=(rotate + incr_rotate), data_rotate_z=33)
