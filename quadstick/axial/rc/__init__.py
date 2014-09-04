'''
rc/__init__.py - Python class for polling R/C transmitters using 
                 Wailly PPM-to-USB cable.

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

from quadstick.axial import Axial
import os

import pygame

class RC(Axial):

    def __init__(self, name, jsid=0):
        '''
        Creates a new RC object.
        '''

        Axial.__init__(self, name)

    def _get_pitch(self):
    
        return self.pitch_sign * RC._get_axis(self, self.pitch_axis)

    def _get_roll(self):
    
        return self.roll_sign * RC._get_axis(self, self.roll_axis)

    def _get_yaw(self):

        return self.yaw_sign * RC._get_axis(self, self.yaw_axis)
 
    def _get_climb(self):

        return Axial._get_axis(self, self.climb_axis)    
