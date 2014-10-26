'''
frsky.py - Python class for polling FrSky R/C transmitters

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

from quadstick.axial.rc import RC

class Taranis(RC):

    def __init__(self, jsid=0):
        '''
        Creates a new FrSky Taranis object.
        '''

        RC.__init__(self, 'Taranis', jsid)

    # Default to Linux 
        self.pitch_axis  = 2
        self.roll_axis   = 1
        self.yaw_axis    = 5
        self.climb_axis  = 0
        self.switch_a_axis = 3
        self.switch_b_axis = 4

        if self.platform == 'Windows':
            self.yaw_axis    = 3
            self.switch_a_axis = 5
            self.switch_b_axis = 4

        elif self.platform == 'Darwin':
            self.pitch_axis  = 0
            self.roll_axis   = 3
            self.yaw_axis    = 1
            self.climb_axis  = 2
            self.switch_a_axis = 4
            self.switch_b_axis = 5

        self.pitch_sign = +1
        self.roll_sign  = -1
        self.yaw_sign   = +1

    def poll(self):
        '''
        Polls the Taranis R/C transmitter.

        Controls are Mode 2 (Left stick throttle / yaw; Right stick pitch / roll).

        Altitude hold: Switch A halfway down
        Position hold: Switch A completely down
        Autopilot:     Switch B down (overrides altitude / position hold)

        Returns demands (pitch, roll, yaw, climb) and switches (pos-hold, alt-hold, autopilot).
        '''

        return RC._poll(self)

    def _get_alt_hold(self):

        # POS-HOLD implies ALT-HOLD
        return (not self._get_autopilot()) and (self._get_pos_hold() or RC._get_axis(self, self.switch_a_axis) > 0)

    def _get_pos_hold(self):

        return (not self._get_autopilot()) and (RC._get_axis(self, self.switch_a_axis)  > .9)

    def _get_autopilot(self):

        return RC._get_axis(self, self.switch_b_axis)  > 0


class TH9X(RC):

    def __init__(self, jsid=0):
        '''
        Creates a new FrSky TH9X object.
        '''

        RC.__init__(self, 'TH9X', jsid)

    # Default to Linux 
        self.pitch_axis  = 1
        self.roll_axis   = 0
        self.yaw_axis    = 5
        self.climb_axis  = 2
        self.switch_axis = 3

        if self.platform == 'Windows':
            self.yaw_axis    = 3
            self.switch_axis = 5

        elif self.platform == 'Darwin':
            self.pitch_axis  = 3
            self.roll_axis   = 2
            self.yaw_axis    = 1
            self.climb_axis  = 0
            self.switch_axis = 4

        self.pitch_sign = +1
        self.roll_sign  = -1
        self.yaw_sign   = +1

    def poll(self):
        '''
        Polls the TH9X R/C transmitter.

        Controls are Mode 2 (Left stick throttle / yaw; Right stick pitch / roll).

        For altitude / position hold and autopilot, see 
        http://3drobotics.com/wp-content/uploads/2014/04/IRIS-Flight-Checklist-v5.pdf

        Returns demands (pitch, roll, yaw, climb) and switches (pos-hold, alt-hold, autopilot).
        '''

        return RC._poll(self)



    def _get_alt_hold(self):

        # POS-HOLD implies ALT-HOLD
        return self._get_pos_hold() or RC._get_axis(self, self.switch_axis) > 0.4

    def _get_pos_hold(self):

        switch = RC._get_axis(self, self.switch_axis)
     
        return switch < 0 and switch > -0.3

    def _get_autopilot(self):

        switch = RC._get_axis(self, self.switch_axis)

        return switch >= 0 and switch < 0.4
