'''
keyboard.py - Python class for using a keyboard to control a quadrotor

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
import pygame.locals

class Keyboard(QuadStick):

    def __init__(self):
        '''
        Creates a new Keyboard object.
        '''
        QuadStick.__init__(self, 'Keyboard')

        self.pitch = 0
        self.roll = 0
        self.yaw = 0
        self.climb = 0

    def poll(self):
        '''
        Polls the keyboard, using the numeric keypad and spacebar:

          8/2     : Pitch forward, backward
          4/6     : Roll leftward, rightward
          0/Enter : Yaw nose left, right
          9/3     : Climb, descend

          Spacebar: Toggle autopilot

        Altitude and position hold are always on.

        Returns demands (pitch, roll, yaw, climb) and switches (pos-hold, alt-hold, autopilot).
        '''

        for event in self.keys:

            if event.type == pygame.locals.KEYDOWN or event.type == pygame.locals.KEYUP:

                # Turn numeric keypad keys into demands
                self.pitch = self._key2demand(self.pitch, event, 264, 258) # 8, 2
                self.roll  = self._key2demand(self.roll,  event, 262, 260) # 6, 4
                self.yaw   = self._key2demand(self.yaw,   event, 256, 271) # 0, Enter
                self.climb = self._key2demand(self.climb, event, 259, 265) # 3, 9

                # Spacebar toggles autopilot
                if event.key == 32:
                    QuadStick._toggle_autopilot(self, event.type == pygame.locals.KEYDOWN)

        # Altitude and position hold are always on
        return QuadStick._poll(self, (self.pitch, self.roll, self.yaw, self.climb), (True, True, self.auto))

    def _key2demand(self, demand, event, lokey, hikey):

        if event.type == pygame.locals.KEYDOWN:
            if event.key == lokey:
                demand = -1
            elif event.key == hikey:
                demand = +1
        else:
            if event.key == lokey or event.key == hikey:
                demand = 0

        return demand

    # For testing: don't call pygame.event.get() more than needed
    def _get_keys(self):

        return self.keys
