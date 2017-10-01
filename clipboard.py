#!/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Copyright (c) 2017 Stephen G. Lynch

# Contribitors:
#   Stephen G. Lynch <stepheng.lynch@gmail.com>

"""
This will be a portable module for obtaining changes to the platform's
clipboard.
"""

import sys
import threading

if sys.platform == 'linux':
	import gi
	gi.require_version('Gtk', '3.0')
	from gi.repository import Gtk, Gdk
else:
	raise ImportError



def get_next_copy():
	"""
	Blocking function that waits for a change in the clipboard. Once clipboard
	has been updated function returns the new clipboard.
	"""
	clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
	copied_text = None

	def handler(clipboard, owner):

		nonlocal copied_text
		copied_text = clipboard.wait_for_text()
		Gtk.main_quit()

	clipboard.connect('owner-change', handler)
	Gtk.main()

	return copied_text






