# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:58:04 2017
@author: monte
"""
from scipy import *
from pylab import *
import sys    

class FourVector:
    def __init__(self, t, x, y, z):
        self.t=t
        self.x=x
        self.y=y
        self.z=z
        
  def MinkProd(self, other):
    return(-self.t*other.t+self.x*other.x+self.y*other.y+self.z*other.z)
  
