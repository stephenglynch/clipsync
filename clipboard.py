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

try:
	if sys.platform == 'linux':
		import gi
		gi.require_version('Gtk', '3.0')
		from gi.repository import Gtk, Gdk
	else:
		raise ImportError

except ImportError:
	raise ImportError('Dependency not met')



def clipboard_change():
	"""
	Blocking function that waits for a change in the clipboard. Once clipboard
	has been updated function returns the new clipboard.
	"""

	clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

	clipboard.connect('owner-change', _handler)

	Gtk.main()


def _handler(clipboard, owner):

	print(clipboard.wait_for_text())
	Gtk.main_quit()







