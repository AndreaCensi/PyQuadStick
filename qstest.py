#!/usr/bin/env python

'''
qstest.py - PyQuadStick test program

    Copyright (C) 2014 Simon D. Levy

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as 
    published by the Free Software Foundation, either version 3 of the 
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
'''

# Choose your controller ======================================================

#from quadstick.axial.game.logitech import ExtremePro3D as Controller
#from quadstick.axial.game.sony import PS3 as Controller
#from quadstick.axial.rc.spektrum import DX8 as Controller
from quadstick.axial.rc.frsky import Taranis as Controller
#from quadstick.keyboard import Keyboard as Controller

# =============================================================================


controller = Controller()

while (controller.running()):

    controller.poll()
