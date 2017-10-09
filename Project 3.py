# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:58:04 2017
@author: monte
"""
from scipy import *
from pylab import *
import sys    

class FourVector:
    def __init__(self,t,x,y,z):
        self.t=t
        self.x=x
        self.y=y
        self.z=z
        self.coordvec=array([[self.t],[self.x],[self.y],[self.z]])
        
    def __repr__(self):
        return'{}'.format(array([[self.t],[self.x],[self.y],[self.z]]))        
        
    def MinkProd(self, other):
        if isinstance(other, ndarray):
            other.shape=(1,4)
            other.t=other[0]
            other.x=other[1]
            other.y=other[2]
            other.z=other[3]        
        return(-self.t*other.t+self.x*other.x+self.y*other.y+self.z*other.z)
  
    def trans(self, xv):
        j=1/sqrt(1-xv**2)
    
        transm=([j,-xv*j,0,0],[-xv*j,j,0,0],[0,0,1,0],[0,0,0,1])
