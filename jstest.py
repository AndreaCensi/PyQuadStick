#!/usr/bin/env python

'''
jstest.py - Displays axis, button, and hat mappings for a joystick or other controller

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

import pygame
import sys

if __name__ == "__main__":

    pygame.display.init()
    pygame.joystick.init()
    js = pygame.joystick.Joystick(0)
    js.init()
            
    while True:

        pygame.event.pump()   
                
        for k in range(js.get_numaxes()):
            sys.stdout.write('A%d: %+3.3f ' % (k, js.get_axis(k)))

        sys.stdout.write(' | ')

        for k in range(js.get_numbuttons()):
            sys.stdout.write('B%d: %d ' % (k, js.get_button(k)))

        sys.stdout.write(' | ')

        for k in range(js.get_numhats()):
            sys.stdout.write('H%d: %d ' % (k, js.get_hat(k)[1]))

        sys.stdout.write('\r')
          
