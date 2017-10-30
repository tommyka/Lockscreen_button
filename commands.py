#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright: (c) 2017, Tommy Kjær Andersen. All rights reserved.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import subprocess

def lockscreen():
    """
    Locks the screen on a mac
    """
    subprocess.call('pmset displaysleepnow', shell=True)
