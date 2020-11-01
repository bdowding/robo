#!/usr/bin/python

import gpiozero
import time

class Stepper(object):
  steps = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
  ]

  def __init__(self, a, b, c, d):
    self.steppers = [a, b, c, d]
    self.index = 0
  
  def walk(self, count, fwd):
    for i in range(count):
      self.step(fwd)
      time.sleep(0.001)
  
  def step(self, fwd):
    if fwd:
      self.index += 1
    else:
      self.index -= 1
    self.index = self.index % len(self.steps)
    self.set_step(self.index)
    
  def set_step(self, step_index):
    step_values = self.steps[step_index % len(self.steps)]
    
    for i in range(4):
      if step_values[i] == 0:
        self.steppers[i].off()
      elif step_values[i] == 1:
        self.steppers[i].on()


shoulder = Stepper(gpiozero.LED(22), gpiozero.LED(23), gpiozero.LED(24), gpiozero.LED(27))
elbow = Stepper(gpiozero.LED(6), gpiozero.LED(13), gpiozero.LED(19), gpiozero.LED(26))

