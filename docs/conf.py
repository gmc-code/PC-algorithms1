# Configuration file for the Sphinx documentation builder.
# see https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
import os
import sys
import sphinx_rtd_theme
project = 'PC-algorithms'
copyright = '2022-4, GMC'
author = 'GMC'

sys.path.insert(0, os.path.abspath('../../'))
package_path = os.path.abspath('../..')
os.environ['PYTHONPATH'] = ':'.join((package_path, os.environ.get('PYTHONPATH', '')))

# -- General configuration ---------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'sphinx_togglebutton',
    'sphinx_design',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# if using To Dos and want them to showup
todo_include_todos = True

# default python Pygments (syntax highlighting) style to use.
# for other styles see https://pygments.org/docs/lexers/#lexers-for-python-and-related-languages
pygments_style = 'sphinx'

jupyter_sphinx_thebelab_config = {
    'requestKernel': True,
    'binderOptions': {
        'repo': "binder-examples/requirements",
    },
}

# -- Options for HTML output -------------------------------

# The theme to use for HTML and HTML Help pages.
# See the documentation for a list of builtin themes.

html_theme = 'sphinx_rtd_theme'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = "PC-algorithms"

# Use custom css
html_css_files = ["css/custom.css"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_static_path = ['../_static/'] # for jupyter

# -- sphinx-rtd-theme Theme Options ------
# See: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html

html_theme_options = {
    'logo_only': False,  # False so text is shown
    'display_version': False,  # False so doc version not shown
    'prev_next_buttons_location': 'both',  # Can be bottom, top, both , or None
    'style_external_links': True,  # True to Add an icon next to external links
    # 'style_nav_header_background': 'blue',
    'style_nav_header_background': 'linear-gradient(to right, blueviolet 15%, limegreen 50%, royalblue 80%)',
    # Toc options; 
    'collapse_navigation': False,  # False so nav entries have the [+] icons
    'sticky_navigation': False,  # False so the nav does not scroll
    'navigation_depth': 4,  # -1 for no limit
    'includehidden': True,  # displays toctree that are hidden
    'titles_only': True  # False so page subheadings are in the nav.
}

# -- RTDs logos -------------------------------
html_favicon = "_static/favicon.ico"
html_logo = "_static/logo_navyblue.png"
