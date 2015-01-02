'''
__init__.py - Python class for polling axial controllers (gamepad, joystick, R/C)

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

from quadstick import QuadStick

import pygame

class Axial(QuadStick):

    def __init__(self, name, jsid=0):
        '''
        Creates a new Axial object with specified name ('PS3', 'FrSky', etc.) and optional id number.
        '''

        QuadStick.__init__(self, name)

        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(jsid)
        self.joystick.init()
        self.joystick.get_axis(jsid)

    def _pump(self):

        pygame.event.pump()   


    def _poll(self):
        '''
        Polls the Axial object, returning demands (pitch, roll, yaw, climb) and
        switches (pos-hold, alt-hold, autopilot).
        '''

        Axial._pump(self)   

        demands = self._get_pitch(), self._get_roll(), self._get_yaw(), self._get_climb()

        switches = self._get_alt_hold(), self._get_pos_hold(), self._get_autopilot()

        return QuadStick._poll(self, demands, switches)

    def _get_axis(self, k):

        return self.joystick.get_axis(k)

    def _get_button(self, k):

        return self.joystick.get_button(k)

    def _get_keys(self):

        return pygame.event.get()
