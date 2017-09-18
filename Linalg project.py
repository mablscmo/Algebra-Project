# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 12:51:24 2017

@author: Oscar
"""
from scipy import *
from pylab import *

class gtrans:
    def __init__(self,x,y,t=1):
        self.coordvec=array([[x],[y]])
        self.angle=arccos(x/sqrt(x**2+y**2))
        self.xvec=array([[t],[x]])
        self.yvec=array([[t],[y]])
        
    def __repr__(self):
        return '{}'.format(self.coordvec)
    
    def transf(self,other):
        xtransmat=array([[1,0],[-other.coordvec[0,0],1]])
        ytransmat=array([[1,0],[-other.coordvec[1,0],1]])
        x=dot(xtransmat,self.xvec)
        y=dot(ytransmat,self.yvec)
        return(array([[x[1,0]],[y[1,0]]]))
    
    
