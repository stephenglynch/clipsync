#!/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Copyright (c) 2017 Stephen G. Lynch

# Contribitors:
#   Stephen G. Lynch <stepheng.lynch@gmail.com>

import socket
import threading
import time
import importlib
import sys

import pytest

if sys.platform == 'linux':
	import gi
	gi.require_version('Gtk', '3.0')
	from gi.repository import Gtk, Gdk
else:
	raise ImportError


import clipboard as cb


def test_platform_error():
	save_platform = sys.platform
	sys.platform = 'abcd'
	with pytest.raises(ImportError):
		importlib.reload(cb)
	sys.platform = save_platform

@pytest.mark.skipif(sys.platform != 'linux',
                    reason="only runs on Linux")
def test_get_clipboard():
	clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
	
	test_text = 'abcd'
	copied_text = None
	def helper():
		nonlocal copied_text
		copied_text = cb.get_next_copy()

	copy_thread = threading.Thread(target=helper)
	copy_thread.start()
	clipboard.set_text(test_text, -1)
	copy_thread.join()

	assert copied_text == test_text





	