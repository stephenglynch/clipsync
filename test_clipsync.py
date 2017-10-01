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

import pytest

from clipsync import *

TIMEOUT = 5.

@pytest.fixture
def clipsync():
    return ClipSync()

@pytest.mark.timeout(TIMEOUT)
def test_broadcast(clipsync):
    #create socket to listen to broadcast and check
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(UDP_ADDRESS_BC)

    #start broadcast thread
    bc_thread = threading.Thread(target=clipsync._broadcast_thread)
    bc_thread.start()

    #check broadcast is expected
    assert b'clipsync:broadcast' in s.recv(50)
    clipsync.stop_broadcast.set()
    bc_thread.join()

@pytest.mark.timeout(TIMEOUT)
def test_listener(clipsync):
    #create broadcasting socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(UDP_ADDRESS_BC)

    #start broadcast thread
    lis_thread = threading.Thread(target=clipsync._listener_thread)
    lis_thread.start()

    #loops until thread is innactive
    while lis_thread.is_alive():
        s.send(b'clipsync:response')
        time.sleep(0.1)

def test_send_string():

    assert SEND_STRING.format(str(1234)) == 'CLIPSYNC:CLIPBOARD:1234'
    assert SEND_STRING.format(str(123456)) == 'CLIPSYNC:CLIPBOARD:1234'

def test_send_string_len():

    assert len(SEND_STRING.format(str(1234))) == SEND_STRING_LEN
    assert len(SEND_STRING.format(str(123456))) == SEND_STRING_LEN
    assert len(SEND_STRING.format(str(12))) == SEND_STRING_LEN

def test_send_string_re():

    assert SEND_STRING_PATTERN.match('CLIPSYNC:CLIPBOARD:1234')
    assert SEND_STRING_PATTERN.match('CLIPSYNC:CLIPBOARD:12  ')
    assert not SEND_STRING_PATTERN.match('CLIPSYNC:clipboard:1234')





