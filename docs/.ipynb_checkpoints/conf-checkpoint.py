# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from myst_parser import __version__

# -- Project information -----------------------------------------------------

project = 'Math 1431'
copyright = '2024, Michael McCabe'
author = 'Michael McCabe'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx', #https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
    'sphinx.ext.todo',
    'sphinx.ext.coverage', #https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode', 
    'sphinx.ext.githubpages',
    'myst_parser', #https://myst-parser.readthedocs.io/en/latest/
    'sphinxcontrib.tikz', #https://readthedocs.org/projects/sphinxcontrib-tikz/
    'sphinx_design', #https://sphinx-design.readthedocs.io/en/sbt-theme/
    'sphinx_thebe', #https://sphinx-thebe.readthedocs.io/en/latest/
    'sphinx_proof', #https://sphinx-proof.readthedocs.io/en/latest/
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# -- MyST extentions -----------------------------------------------------
# Go to https://myst-parser.readthedocs.io/en/v0.15.1/sphinx/reference.html
# for more information.
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 2
myst_footnote_transition = True
myst_dmath_double_inline = True
panels_add_bootstrap_css = False

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build', 
    'Thumbs.db', 
    '.DS_Store', 
    '.ipynb_checkpoints', 
    'chapterone/.ipynb_checkpoints',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}


# -- add the repository name when ready--------------------------------------
#html_theme_options = {
#    ...
#    "repository_url": "https://github.com/{your-docs-url}",
#    "use_repository_button": True,
#    ...
#}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Math1431notes'

# -- sphinxcontribTiKz -------------------------------------------------------
# github at https://github.com/sphinx-contrib/tikz
# -- Options specific to sphinxcontrib-tikz -------------------------------

# For latex target the tikzlibraries have to be specified explicitly
# tikz_latex_preamble = '\input{pppppreamble.tex}'
tikz_tikzlibraries = 'arrows'

# Use default suite
tikz_proc_suite = "GhostScript"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'\usepackage{pgf,tikz} \usetikzlibrary{arrows} \newcommand{\ddx}[1]{\frac{d}{dx}\left[#1\right]} \newcommand{\ddt}[1]{\frac{d}{dt}\left[#1\right]} \newcommand{\dydx}{\frac{dy}{dx}} \newcommand{\dxdt}{\frac{dx}{dt}} \newcommand{\dydt}{\frac{dy}{dt}} \newcommand{\dzdt}{\frac{dz}{dt}} \newcommand{\R}{\mathbb{R}} \newcommand{\Q}{\mathbb{Q}} \newcommand{\N}{\mathbb{N}} \newcommand{\Z}{\mathbb{Z}}',

    # Latex figure (float) alignment
    #
    'figure_align': 'htbp',
}
latex_engine = "xelatex"
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'preamble.tex', 'Math 1431 Notes',
     'Michael McCabe', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'math1431', 'Math 1431 Notes',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Math1431', 'Math 1431 Notes',
     author, 'Math1431', 'Lecture notes and more for math 1431 at the College of DuPage.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {'https://docs.python.org/3': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
