"""
Overview
========

This plugin implements Key-Commands to comment and uncomment blocks of code.

Usage
=====

In order to comment/uncomment a block of code it is needed to first select the region.

Open a programming file then select some lines with <Key-f> in NORMAL mode then
switch to ALPHA mode with <Key-3>.

Once it is in ALPHA mode then type <Key-e> to comment or <Key-r> to uncomment
the selected block of text.

The block of code will be commented based on the programming comment style of the language.

Key-Commands
============

Mode: ALPHA
Event: <Key-e>
Description: Add inline comments to a selected block of text.

Mode: ALPHA
Event: <Key-r>
Description: Remove inline comments from a selected block of text.

"""

from mimetypes import guess_type
from re import escape

DEFAULT = '#'
TABLE   = { 
              'text/x-python'            :'#',
              'text/x-java-source'       :'//',
              'text/x-csrc'              :'//',
              'text/x-sh'                :'#',
              'application/x-javascript' :'//',
              'text/x-c++src'            :'//'
          }

def add_inline_comment(area):
    """
    It adds inline comment to selected lines based on the file extesion.
    """

    comment = TABLE.get(guess_type(area.filename)[0], DEFAULT)
    area.replace_ranges('sel', '^ +|^', 
    lambda data, index0, index1: '%s%s ' % (area.get(index0, index1), comment))
    area.clear_selection()

def rm_inline_comment(area):
    """
    It removes the inline comments.
    """

    comment = TABLE.get(guess_type(area.filename)[0], DEFAULT)
    area.replace_ranges('sel', '^ *%s ?' % comment, 
    lambda data, index0, index1: area.get(index0, index1).replace(
        '%s ' % comment, '').replace(comment, ''))
    area.clear_selection()

def install(area):
    area.install(
    ('ALPHA', '<Key-r>', lambda event: rm_inline_comment(event.widget)),
    ('ALPHA', '<Key-e>', lambda event: add_inline_comment(event.widget)))





