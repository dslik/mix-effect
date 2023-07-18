#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# CDMI specification documentation build configuration file, created by
# sphinx-quickstart on Wed Nov  8 13:25:30 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import codecs
from string import Template

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinxcontrib.bibtex']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md', '.txt']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = '2810A'
copyright = '2022, David Slik'
author = 'David Slik'

licensetext = codecs.open('license.md', encoding='utf-8').read() + codecs.open('revisions.tex', encoding='utf-8').read()

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.4'
# The full version, including alpha/beta/rc tags.
release = '0.4'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [ 'readme.md', 'license.md']

# latex_appendices = ['bom']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Enable the use of numfig
numfig = True

# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'xelatex'

latex_contents = r'''
    \licensepage
    \tableofcontents
    \clearpage
    \listoffigures
    \clearpage
    \listoftables
    \clearpage
    \pagenumbering{arabic}
'''

latex_use_xindy = False

latex_defns = Template(r'''
    \def\licensepage{
        \pagestyle{normal}
        ${licensetext}
        \clearpage
    }
''')

# -- SNIA-style Title Page ---------------------------------------------
latex_maketitle = r'''
    \begin{titlepage}
        \begingroup % for PDF information dictionary
           \def\endgraf{ }\def\and{\& }%
           \pdfstringdefDisableCommands{\def\\{, }}% overwrite hyperref setup
           \hypersetup{pdfauthor={David Slik}, pdftitle={2810A Assembly}}%
        \endgroup

        \begin{tikzpicture}[remember picture, overlay]
          \draw[line width = 2pt] ($(current page.north west) + (0.5in,-0.5in)$) rectangle ($(current page.south east) + (-0.5in,0.5in)$);
        \end{tikzpicture}

        \begin{center}
            {\Huge ASSEMBLY INSTRUCTIONS }\par
            \vspace{10pt}
            {\Large 2810A M/E Source Selector module }\par
            \vspace{20pt}
            \sphinxlogo
            \vspace{20pt}
            {\Large Document control number: 2810-8010 }\par
            \vspace{10pt}
            {\Large Document date: 2022-09-04 }\par
            \vspace{10pt}
            {\Large Document revision: v0.4 }\par
            \vspace{20pt}
        \end{center}
        \begin{flushleft}
            {\normalsize
                ABSTRACT: This document provides instructions on how to assembly and test a 2810A Source Selector module. A complete bill of materials is included as an annex. 
            }\par
            {\normalsize
               Suggestions and corrections should be directed to http://www.github.com/dslik/mix-effect/issues
            }\par
            {\large
               Serial number:\quad\quad\quad\quad\quad\quad\quad\quad Assembly date:\quad\quad\quad\quad\quad\quad\quad\quad Assembled by:
            }\par
        \end{flushleft}
        \setcounter{footnote}{0}
        \let\thanks\relax\let\maketitle\relax
    \end{titlepage}
    \setcounter{page}{1}
    \pagenumbering{roman}
'''

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    'fncychap': '',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'inputenc': '',
    'utf8extra': '',

    'printindex': '',
    'fontpkg': r'''
    % Set fonts
    \usepackage{fontspec}
    \setsansfont{Arial}
    \setmainfont{Arial}
    \setmonofont{Courier New}

    % Adjust font size
    \usepackage{scrextend}
    \changefontsizes[10pt]{9pt}

    \usepackage{enumitem}

    ''',

    'preamble': r'''


    % Graphics package
    \usepackage{graphbox}

    % Make table headers lightgray
    \usepackage{colortbl}
    \protected\def\sphinxstyletheadfamily {\cellcolor{lightgray}\sffamily}

    % Change Latex's Part/Chapter/Appendix to Part/Section/Annex
    \addto\captionsenglish{\renewcommand{\partname}{Part~}}
    \addto\captionsenglish{\renewcommand{\chaptername}{Section~}}
    \addto\captionsenglish{\renewcommand{\appendixname}{Annex~}}
    \addto\captionsenglish{\renewcommand{\figurename}{Fig.\enspace}} 
    \usepackage{chngcntr}
    \counterwithout{figure}{chapter}
    \counterwithout{table}{chapter}
    
    % Change the tables of content/figure/table
    \usepackage{tocloft}
    \setlength{\cftchapnumwidth}{18pt}
    \setlength{\cftsecnumwidth}{24pt}
    \setlength{\cftsubsecnumwidth}{28pt}
    \message{figure}
    \newlength{\myfiglen}
    \renewcommand{\cftfigpresnum}{\figurename}
      \renewcommand{\cftfigaftersnum}{:}
      \settowidth{\myfiglen}{\cftfigpresnum\cftfigaftersnum}
      \addtolength{\cftfignumwidth}{\myfiglen}
    \message{table}
    \newlength{\mytablen}
    \renewcommand{\cfttabpresnum}{\tablename}
      \renewcommand{\cfttabaftersnum}{:}
      \settowidth{\mytablen}{\cfttabpresnum\cfttabaftersnum}
      \addtolength{\cfttabnumwidth}{\mytablen}
    \message{chapter}
    \newlength{\mychaplen}
    \renewcommand{\cftchappresnum}{\chaptername}
      \renewcommand{\cftchapaftersnum}{:}
      \settowidth{\mychaplen}{\cftchappresnum\cftchapaftersnum}
      \addtolength{\cftchapnumwidth}{\mychaplen}


    % Clear pages before new Part
    \usepackage{titlesec}
    \usepackage{tikz}
    \usetikzlibrary{calc}

    % Change the page headers
    \makeatletter
    \fancypagestyle{normal}{
        \fancyhf{}
        \fancyhead[LE,LO]{{\py@HeaderFamily 2810-8010 - 2810A assembly instructions v\version}}
        \fancyhead[RE,RO]{{\py@HeaderFamily Public / Controlled}}
        \fancyfoot[LE,LO]{{\py@HeaderFamily \copyright \  VE7FIM 2022}}
        \fancyfoot[RE,RO]{{\py@HeaderFamily\thepage}}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
        }

    \fancypagestyle{plain}{
        \fancyhf{}
        \fancyhead[LE,LO]{{\py@HeaderFamily 2810-8010 - 2810A assembly instructions v\version}}
        \fancyhead[RE,RO]{{\py@HeaderFamily Public / Controlled}}
        \fancyfoot[LE,LO]{{\py@HeaderFamily \copyright \  VE7FIM 2022}}
        \fancyfoot[RE,RO]{{\py@HeaderFamily\thepage}}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
        }
    \makeatother

    % Create linenumers
    \usepackage{lineno} 
    \linenumbers

''' + latex_defns.substitute(licensetext=licensetext),   

    'tableofcontents': latex_contents,
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    
    'sphinxsetup': 'verbatimhintsturnover=true',
    'extraclassoptions': 'openany',
    'releasename': 'Version',
    'maketitle': latex_maketitle,    
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, '2810-8010.tex', '2810A assembly instructions',
     'DRAFT', 'manual'),
]

latex_logo = 'images/2810A.jpg'
latex_toplevel_sectioning = 'part'



