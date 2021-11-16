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

sys.path.insert(0, os.path.abspath(os.path.join("..", "src")))


# -- Project information -----------------------------------------------------

project = "template-python-project"
copyright = "2021, Guillaume Gautier"
author = "Guillaume Gautier"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    # Official Sphinx extensions
    # https://www.sphinx-doc.org/en/master/usage/extensions/index.html
    "sphinx.ext.autodoc",  # Include documentation from docstrings
    # "sphinx.ext.autosectionlabel",  # Allow reference sections using its title
    # "sphinx.ext.autosummary",  # Generate autodoc summaries
    # "sphinx.ext.coverage",  # Collect doc coverage stats
    "sphinx.ext.doctest",  # Test snippets in the documentation
    "sphinx.ext.duration",  # Measure durations of Sphinx processing
    # "sphinx.ext.extlinks",  # Markup to shorten external links
    "sphinx.ext.githubpages",  # Publish HTML docs in GitHub Pages
    # "sphinx.ext.graphviz",  # Add Graphviz graphs
    # "sphinx.ext.ifconfig",  # Include content based on configuration
    # "sphinx.ext.imgconverter",  # A reference image converter using Imagemagick
    # "sphinx.ext.inheritance_diagram",  # Include inheritance diagrams
    # "sphinx.ext.intersphinx",  # Link to other projects’ documentation
    # "sphinx.ext.linkcode",  # Add external links to source code
    # "sphinx.ext.imgmath",  # Render math as images
    "sphinx.ext.mathjax",  # Render math via JavaScript
    # "sphinx.ext.jsmath",  # Render math via JavaScript
    "sphinx.ext.napoleon",  # Support for NumPy and Google style docstrings
    "sphinx.ext.todo",  # Support for todo items # .. todo:: directive
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    # Non-official Sphinx extensions
    # https://github.com/sphinx-contrib/
    "sphinxcontrib.bibtex",  # Sphinx extension for BibTeX style citations
    "sphinxcontrib.proof",  # Sphinx extension to typeset theorems, proofs
    # Non-official Sphinx extension for matplotlib plots
    # https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html?highlight=plot_directive#module-matplotlib.sphinxext.plot_directive
    "matplotlib.sphinxext.plot_directive",  # .. plot:: directive for plt.plot
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
html_static_path = ["_static"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes.
# https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes
# or third-party themes
# https://sphinx-themes.org/
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# -- Extension configuration -------------------------------------------------

# sphinxcontrib-bibtex https://sphinxcontrib-bibtex.readthedocs.io/en/latest/index.html
bibtex_bibfiles = ["./bibliography/bibliography.bib"]
bibtex_encoding = "latin"
# bibtex_reference_style = "alpha"  # alpha, plain , unsrt, and unsrtalpha

# matplotlib.sphinxext.plot_directive
# https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html

# plot_include_source = True
# plot_html_show_source_link =
# plot_pre_code =
# plot_basedir =
# plot_formats =
# plot_html_show_formats =
# plot_rcparams =
# plot_apply_rcparams =
# plot_working_directory =
# plot_template =
