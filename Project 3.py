# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:58:04 2017
@author: monte
"""
from scipy import *
from pylab import *
import sys    

class FourVector:
    def __init__(self,txyz):
        if isinstance(txyz,ndarray):
            txyz.shape=(4,1)
            self.t=txyz[0,]
            self.x=txyz[1,]
            self.y=txyz[2,]
            self.z=txyz[3,]
            self.coordvec=txyz
        elif isinstance(txyz,(tuple,list)):
            self.t=txyz[0]
            self.x=txyz[1]
            self.y=txyz[2]
            self.z=txyz[3]
            self.coordvec=array([[txyz[0]],[txyz[1]],[txyz[2]],[txyz[3]]])
        else:
            raise TypeError('Input must be array, tuple, or list')
        
    def __repr__(self):
        return'{}'.format(self.coordvec)        

        
    def MinkProd(self, other):
        if not isinstance(other,(ndarray,tuple,list,FourVector)):
            raise TypeError('Input must be array, tuple, list, or Fourvector')
        if isinstance(other, ndarray):
            other.shape=(1,4)
            other.t=other[0]
            other.x=other[1]
            other.y=other[2]
            other.z=other[3]
        if isinstance(other,tuple,list):
            other.t=other[0]
            other.x=other[1]
            other.y=other[2]
            other.z=other[3]
        return(-self.t*other.t+self.x*other.x+self.y*other.y+self.z*other.z)
  
    def trans(self, xv):
        g=1/sqrt(1-xv**2)
        transm=array([[g,-xv*g,0,0],[-xv*g,g,0,0],[0,0,1,0],[0,0,0,1]])
        return(transm.dot(self.coordvec))
