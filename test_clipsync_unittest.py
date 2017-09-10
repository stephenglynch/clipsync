#!/bin/env python

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

    #check broad cast is epected
    assert 'clipsync:broadcast' in s.recv(50)
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
        print('send broadcast')
        s.send('clipsync:response')
        time.sleep(0.1)



