#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys
import codecs
import unittest

from rst2slideshow import SlideShowWriter
from docutils.core import publish_parts, publish_doctree, publish_from_doctree
from nose.tools import assert_equals
from tempfile import gettempdir

tmpdir = gettempdir()
unittest.TestCase.maxDiff = None

def rst_to_slideshow(case, part):
    overrides = case.copy()
    rst = overrides.pop('rst')
    overrides.pop('out')
    overrides.setdefault('indent_output', False)
    return publish_parts(writer=SlideShowWriter(), source=rst,
                          settings_overrides=overrides)[part]

def extract_variables(module):
    '''
    Extract variables of a test data module.
    Variables should be a dict().
    For example, {'rst': rst, 'out':out, ...}
    '''
    return ((v, getattr(module, v)) for v in dir(module)
        if not v.startswith('__') and isinstance(getattr(module, v), dict))


# def test_head():
#     '''
#     test the head part of a rst2html5 conversion
#     '''
#     import head_cases
#     func = lambda x: rst_to_slideshow(x, 'head')
#     for test_name, case in extract_variables(head_cases):
#         yield _test_part, func, test_name, case


def test_body():
    '''
    test the body part of a rst2html5 conversion
    '''
    import body_cases
    func = lambda x: rst_to_slideshow(x, 'body')
    for test_name, case in extract_variables(body_cases):
        yield _test_part, func, test_name, case



def test_transform_doctree():
    '''
    Test doctree transformation to conform to a html5 Slide
    '''
    import transform_cases
    old_stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')
    func = lambda x: rst_to_slideshow(x, 'pseudoxml')
    try:
        for test_name, case in extract_variables(transform_cases):
            yield _test_part, func, test_name, case
    finally:
        sys.stderr.close()
        sys.stderr = old_stderr



def _test_part(func, test_name, case):
    try:
        assert_equals(func(case), case['out'])
    except Exception as error:
        '''
        write temp files to help manual testing
        '''
        filename = os.path.join(tmpdir, test_name)
        with codecs.open(filename + '.rst', encoding='utf-8', mode='w') as f:
            f.write(case['rst'])

        if isinstance(error, AssertionError):
            error.args = ('%s: %s' % (test_name, error.message), )
        raise error
