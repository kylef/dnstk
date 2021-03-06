import sys, os

sys.path.append(os.path.abspath('..'))
from dnstk import __version__

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'dnstk'
copyright = u'2012, Kyle Fuller'
version = __version__
release = __version__
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'dnstkdoc'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'dnstk.tex', u'dnstk Documentation',
   u'Kyle Fuller', 'manual'),
]

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'dnstk', u'dnstk Documentation',
     [u'Kyle Fuller'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'dnstk', u'dnstk Documentation',
   u'Kyle Fuller', 'dnstk', 'One line description of project.',
   'Miscellaneous'),
]

