#!/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Copyright (c) 2017 Stephen G. Lynch

# Contribitors:
#   Stephen G. Lynch <stepheng.lynch@gmail.com>

"""
ClipSync module used by the interface to find and select a device to synchronise
clipboard with.
"""

import socket
import threading
import time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


UDP_ADDRESS_BC = ('<broadcast>', 50002)


class ClipSync:
    """
    A class that represents a connection to an external mobile whose clipboard
    we are syncing with.
    """

    def __init__(self):
        #setup clipboard
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.stop_broadcast = threading.Event()
        self._external_device = None

    def _broadcast_thread(self):
        #create broadcasting socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.connect(UDP_ADDRESS_BC)

        #loops until there is a response from listening thread
        while not self.stop_broadcast.is_set():
            s.send('clipsync:broadcast')
            time.sleep(0.25)

    def _listener_thread(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(UDP_ADDRESS_BC)

        while True:
            data = s.recv(50)
            if data == 'clipsync:response':
                self.stop_broadcast.set()
                break

    def find_devices(self):
        """
        Broadcasts and lists devices that respond

          :returns: list of ClipSync devices
          :rtype: list
        """

        self._response = False
        self._devices = []

        #Create and start threads
        bc_thread = threading.Thread(target=self._broadcast_thread)
        list_thread = threading.Thread(target=self._listener_thread)
        #Start threads
        bc_thread.start()
        list_thread.start()
        #Wait for threads to finish
        bc_thread.join()
        list_thread.join()

        return ['TODO:return list of devices']

    def select_device(self, address):
        """
        Selects the device whose clipboard will be synced

          :param address: address of the device to connect 
          :type address: (host, port)
        """

        self._external_device = address

    def synchronise(self):
        """
        Maintains synchronicity between paired devices clipboards. An external
        device must have been selected first.
        """

        if self._external_device is None:
            raise Exception




def update_phone_clipboard(board, event):
    #TODO: This needs to properly fleshed
    print('Clipboard changed')
    print(board.wait_for_text())
    print('')

    
if __name__ == '__main__':

    cs = ClipSync()
    cs.find_a_device()

