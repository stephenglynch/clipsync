"""
This will be a portable module for obtaining changes to the platform's
clipboard.
"""

import sys
import threading

try:
	if sys.platform == 'linux2':
		import gi
		gi.require_version('Gtk', '3.0')
		from gi.repository import Gtk, Gdk

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







