# -*- coding: utf-8 -*-
# This file is part of TextVentures - https://github.com/RMed/textventures
#
# Copyright (C) 2013 Rafael Medina García <rafamedgar@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
This module contains the gettext translation instances for a simplified
access to on-the-fly language changing options.
"""

import gettext, os
import config
import locale

# English (original)
en = gettext.translation('textventures',
        os.path.dirname(locale.__file__), languages=['en'])
# Spanish
es = gettext.translation('textventures', 
        os.path.dirname(locale.__file__), languages=['es'])

def startup():
    """Get the language of the program at startup."""
    print os.path.join('.', 'locale')
    # Get from file
    try:
        # Open language file
        lang_file = open(config.LANG_FILE, 'r')
        # Read language file
        config.LANG = lang_file.readline()
        # Close language file
        lang_file.close()
    except:
        # Create language file
        lang_file = open(config.LANG_FILE, 'w')
        # Write into file (default language)
        lang_file.write('en')
        # Change program language
        config.LANG = 'en'
        # Close language file
        lang_file.close()

    # Change language
    change(config.LANG)

def change(language):
    """Change the language of the program.

    Arguments:
        language -- language code to use
    """
    # Open language file
    lang_file = open(config.LANG_FILE, 'w')

    # Check language code
    if language == 'es':
        # Spanish
        es.install()
        # Change language file
        lang_file.write('es')  
        # Change language variable
        config.LANG = 'es'
    else:
        # English (default language)
        en.install()
        # Change language file
        lang_file.write('en')
        # Change language variable
        config.LANG = 'en'

    # Close file
    lang_file.close()
