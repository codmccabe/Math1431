# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# imports for python

import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Math 1431 Notes'
copyright = '2024, Michael McCabe'
author = 'Michael McCabe'
release = 'Fall 2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'myst_parser',
	'sphinx_design',
	'sphinx_proof',
	'matplotlib.sphinxext.only_directives',
        'matplotlib.sphinxext.plot_directive',
        'IPython.sphinxext.ipython_directive',
        'IPython.sphinxext.ipython_console_highlighting',
	'sphinx.ext.inheritance_diagram',
        'numpydoc'
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'chapter1/.ipynb_checkpoints','.ipynb_checkpoints','chapter2/.ipynb_checkpoints']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
