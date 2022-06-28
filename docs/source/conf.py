# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
import ceres_workshop

# -- Project information -----------------------------------------------------

project = "CEReS Workshop"
copyright = "2022, Joe Marsh Rossney"
author = "Joe Marsh Rossney"

# The full version, including alpha/beta/rc tags
version = ceres_workshop.__version__
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
]

# Napoleon
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_attr_annotations = True
napoleon_include_special_with_doc = True
# napoleon_use_param = True
# napoleon_type_aliases = {}

# External links
# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
extlinks = {
    "arxiv": ("https://arxiv.org/abs/%s", "arxiv:%s"),
}

# Intersphinx
intersphinx_mapping = {
    "torch": ("https://pytorch.org/docs/stable", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["../_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_short_title = "CEReS Workshop"

html_theme = "cloud"
html_theme_options = {
    # "roottarget":
    "stickysidebar": True,
    "highlighttoc": True,
    "sidebar_localtoc_title": "Contents",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["../_static"]
