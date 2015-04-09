# -*- encoding: utf-8 -*-
import glob
import io
import re
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()

setup(
    name='rst2html5slides',
    version='1.0',
    license='MIT License',
    author='André Felipe Dias',
    author_email='andref.dias@gmail.com',
    keywords=['restructuredText', 'slide', 'docutils', 'presentation', 'html5'],
    description='rst2html5slides extends rst2html5 to generate a deck of slides from '
                'a reStructuredText file that can be used with any web presentation '
                'framework such as impress.js, jmpress.js or deck.js.',
    long_description="%s\n%s" % (read("README.rst"),
                                 re.sub(":obj:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst"))),
    platforms='any',
    install_requires=read('requirements.txt').split(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Utilities',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    zip_safe=False,
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(i))[0] for i in glob.glob("src/*.py")],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'rst2html5slides = rst2html5slides:main',
        ],
    },
    data_files=[
        ('template', glob.glob('src/template/*')),
        ('css', glob.glob('src/css/*.css')),
        ('js', glob.glob('src/js/*.js')),
        ('js/jmpress', glob.glob('src/js/jmpress/*')),
    ],
)
