#!/bin/env python

import socket
import threading
import time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


UDP_ADDRESS_BC = ('<broadcast>', 50002)


class ClipSync:

    def __init__(self):
        #setup clipboard
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.stop_broadcast = threading.Event()

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

    def find_device(self):
        """
        Finds first device that responds
        """

        self._response = False

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


def update_phone_clipboard(board, event):
    #TODO: This needs to properly fleshed
    print('Clipboard changed')
    print(board.wait_for_text())
    print('')

    
if __name__ == '__main__':

    print 'started'

    cs = ClipSync()
    cs.find_a_device()

    print 'finished'
