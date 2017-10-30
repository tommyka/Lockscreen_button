#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright: (c) 2017, Tommy Kjær Andersen. All rights reserved.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import glob
import commands
import time
import serial

def start():
    """ Start listening for usbports """
    while True:
        ports = find_usbport()
        num_ports = len(ports)

        if num_ports != 0:
            listen(ports[0])
        else:
            print 'serial not found'

        time.sleep(10)

def find_usbport():
    """ Glob to find """
    usbports = glob.glob('/dev/tty.wch*')
    return usbports

def listen(port):
    """ Listen on the serial port """

    ser = serial.Serial(port, 9600)
    try:
        print 'Start listing on ' + port
        while True:
            readout = ser.read()

            print('value', readout)

            if readout == '1':
                commands.lockscreen()
    except serial.SerialException:
        print "Error with serial port"
        return

if __name__ == "__main__":
    start()
