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

import clipboard as cb

def test_platform_error():

	save_platform = sys.platform
	sys.platform = 'abcd'
	with pytest.raises(ImportError):
		importlib.reload(cb)
	sys.platform = save_platform



	