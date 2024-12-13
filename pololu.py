# The MIT License (MIT)
#
# Copyright (c) 2024 Fermilab Robotics
#               
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from machine import Pin
import time

class POLOLU_36v4:
    
    def __init__(self, DirPin=Pin(0, Pin.OUT), StepPin=Pin(1, Pin.OUT)):
        self.DirPin = DirPin
        self.StepPin = StepPin
    
    def step_forward(self, count, delay=1):
        """ step forward 'count' number of steps """
        """ with a default delay of 100 mS between each step"""
        for i in range(0, count):
            self.DirPin.on()
            self.StepPin.on()
            time.sleep_ms(delay)
            self.StepPin.off()
            time.sleep_ms(delay)

    def step_backwards(self, count, delay=1):
        """ step backwards 'count' number of steps """
        """ with a default delay of 100 mS between each step"""
        for i in range(0, count):
            self.DirPin.off()
            self.StepPin.on()
            time.sleep_ms(delay)
            self.StepPin.off()
            time.sleep_ms(delay)
        
