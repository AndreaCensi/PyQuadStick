'''
quadstick/__init__.py - Python class for polling quadrotor flight-simulator controllers

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
import pygame.locals
from platform import platform
import sys
import traceback


class QuadStick(object):

    def __init__(self, name):
        '''
        Creates a new QuadStick object.
        '''

        # Init pygame
        pygame.init()
        pygame.display.init()
        
        self.screen = pygame.display.set_mode((500,280), pygame.locals.RESIZABLE)

        self.font = pygame.font.SysFont('Courier', 20)

        pygame.display.set_caption('QuadStick: ' + name)

        # Supports keyboard polling
        self.keys = []

        # Supports autopilot toggling for non-R/C controllers
        self.auto    = False
        self.toggled = False

        self.name = name

        self.platform = platform()[0:platform().find('-')]

        self.row_height = 30

    def __str__(self):
        '''
        Returns a string representation of this QuadStick object
        '''
        return self.name

    def _poll(self, demands, switches):

        self._show_demand(demands, 0, -1, 'Pitch')
        self._show_demand(demands, 1, -1, 'Roll')
        self._show_demand(demands, 2, +1, 'Yaw')
        self._show_demand(demands, 3, +1, 'Climb')
 
        self._show_switch(switches[2], 2, 'Autopilot')

        # Autopilot turns off altitude hold, position hold
        self._show_switch(switches[0] and not switches[2], 0, 'Altitude hold')
        self._show_switch(switches[1] and not switches[2], 1, 'Position hold')

        pygame.display.flip()

        return demands, switches
 
    def running(self):
        '''
        Returns True if the QuadStick is running, False otherwise. Run can be terminated by hitting
        ESC.
        '''

        self.keys = pygame.event.get()

        for event in self.keys:

            if event.type == pygame.locals.QUIT:
                return False

            elif event.type == pygame.locals.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.locals.RESIZABLE)

            elif (event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_ESCAPE):
                return False

        return True
 
    def error(self):
        '''
        Displays the most recent exception as an error message, and waits for ESC to quit.
        '''
        exc_type, exc_obj, tb = sys.exc_info()

        while True:

            self.screen.fill((0,0,0)) # Erase previous screen
            tb = traceback.format_exc()
            self._draw_label_in_row('ERROR', 0, color=(255,0,0))
            row = 1
            for line in tb.split('\n'):
                self._draw_label_in_row(line, row)
                row += 1
            self._draw_label_in_row('Hit ESC to exit', row)

            pygame.display.flip()

            if not self.running():
                pygame.quit()
                sys.exit()

    def _show_switch(self, switchval, index, label):

        x = 200
        y = 180 + index * 30
        r = 10

        # Draw a white ring around the button
        pygame.draw.circle(self.screen, (255,255,255), (x, y), r, 1)

        # Draw a white or black disk inside the ring depending on switch state
        pygame.draw.circle(self.screen, (255,255,255) if switchval else (0,0,0), (x, y), r-3)

        self._draw_label(label, y-10)

    def _show_demand(self, demands, index, sign, label):

        # color for no-demand baseline
        color = (0, 0, 255) 

        demand = sign * demands[index]

        if demand > 0:
            color =  (0, 255, 0)

        if demand < 0:
            color =  (255, 0, 0)

        x = 200			# X coordinate for zero demand
        y = 20 + index * 30
        w = 100			# width of rectangel for maximum demand
        h = 20

        # Draw a black rectangle over whole area
        pygame.draw.rect(self.screen, (0,0,0), (x-w-1, y, x+w, 20))

        # Draw a colorful rectangle to represent the demand
        pygame.draw.rect(self.screen, color, (x, y, demand*w, 20))

        self._draw_label(label, y)

    def _draw_label_in_row(self, text, row, color=(255,255,255)):

        self._draw_label(text, row*self.row_height, color)

    def _draw_label(self, text, y, color=(255,255,255)):

        surface = self.font.render(text, True, color, (0, 0, 0))
        surface.set_colorkey( (0, 0, 0) )
 
        self.screen.blit(surface, (20, y))
 

    def _toggle_autopilot(self, trigger):

        if trigger:
            if not self.toggled:
                self.auto = not self.auto
            self.toggled = True
        else:
            self.toggled = False

        return self.auto
