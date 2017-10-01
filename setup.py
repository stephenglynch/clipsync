#!/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Copyright (c) 2017 Stephen G. Lynch

# Contribitors:
#   Stephen G. Lynch <stepheng.lynch@gmail.com>

from setuptools import setup

setup(
	name='clipsync',
	version='0.0.1',
	description='app for synchronising desktop clipboard with android',
	url='https://github.com/stephenglynch/clipsync',
	author='Stephen G Lynch',
	author_email='stepheng.lynch@gmail.com',
	license='MPL v2',
	packages=['clipboard', 'clipsync'],
	zip_safe=False
	)