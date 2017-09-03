#/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


def print_something(board, event):
    print('Clipboard changed')
    print(board, event)
    print('')

    
if __name__ == '__main__':
    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
    clipboard.connect('owner-change', print_something)
    Gtk.main()
