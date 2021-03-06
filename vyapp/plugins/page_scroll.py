"""
Overview
========

This plugin turns possible to scroll pages.

Usage
=====

Press <Key-Q> in NORMAL mode to scroll one page up.
Press <Key-A> in NORMAL mode to scroll one page down.

Key-Commands
============

Mode: NORMAL
Event: <Key-Q> 
Description: Scroll a page up.


Mode: NORMAL
Event: <Key-A> 
Description: Scroll one page down.

"""


def install(area):
    area.install(('NORMAL', '<Key-Q>', lambda event: event.widget.scroll_page_up()),
                 ('NORMAL', '<Key-A>', lambda event: event.widget.scroll_page_down()))





