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
        print(self.coordvec)
    
    def transf(self,other):
        xtransmat=array([[1,0],[other[0],1]])
        ytransmat=array([[1,0],[other[1],1]])
        transdmat=array([[dot(self.xvec,xtransmat)],[dot(self.yvec,ytransmat)]])
        return(transdmat)
    