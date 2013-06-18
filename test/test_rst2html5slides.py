#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys
import codecs
import unittest

from rst2html5slides import SlideShowWriter
from docutils.core import publish_parts
from nose.tools import assert_equals
from tempfile import gettempdir

tmpdir = gettempdir()
unittest.TestCase.maxDiff = None


def rst_to_html5slides_part(case):
    overrides = case.copy()
    rst = overrides.pop('rst')
    part = overrides.pop('part')
    overrides.pop('out')
    overrides.setdefault('indent_output', True)
    return publish_parts(writer=SlideShowWriter(), source=rst,
                         settings_overrides=overrides)[part]


def extract_variables(module):
    '''
    Extract variables of a test data module.
    Variables should be a dict().
    For example, {'rst': rst, 'out':out, ...}
    '''
    return (
        (v, getattr(module, v)) for v in dir(module)
        if not v.startswith('__') and isinstance(getattr(module, v), dict)
    )


def test():
    '''
    Test cases
    '''
    import cases
    old_stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')
    try:
        for test_name, case in extract_variables(cases):
            _test_part.description = test_name
            yield _test_part, test_name, case
    finally:
        sys.stderr.close()
        sys.stderr = old_stderr


def _test_part(test_name, case):
    result = rst_to_html5slides_part(case)
    try:
        assert_equals(result, case['out'])
    except Exception as error:
        '''
        write temp files to help manual testing
        '''
        filename = os.path.join(tmpdir, test_name)
        with codecs.open(filename + '.rst', encoding='utf-8', mode='w') as f:
            f.write(case['rst'])
        with codecs.open(filename + '.result', encoding='utf-8', mode='w') as f:
            f.write(result)
        with codecs.open(filename + '.expected', encoding='utf-8', mode='w') as f:
            f.write(case['out'])

        if isinstance(error, AssertionError):
            error.args = ('%s\n%s' % (test_name, error.message), )
        raise error
