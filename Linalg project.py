# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 12:51:24 2017

@author: Oscar
"""
from scipy import *
from pylab import *

class gtrans2vec:
    def __init__(self,xy,t=1):
        if isinstance(xy,ndarray):
            xy.shape=(2,1)
            self.coordvec=xy
            self.angle=arccos(xy[0,0]/sqrt(xy[0,0]**2+xy[1,0]**2))
            self.xvec=array([[t],[xy[0,0]]])
            self.yvec=array([[t],[xy[1,0]]])
            self.length=sqrt(xy[0,0]**2+xy[1,0]**2)
        if isinstance(xy,(tuple,list)):
            self.coordvec=array([[xy[0]],[xy[1]]])
            self.angle=(arccos(xy[0]/sqrt(xy[0]**2+xy[1]**2)))/math.pi*180
            self.xvec=array([[t],[xy[0]]])
            self.yvec=array([[t],[xy[1]]])
            self.length=sqrt(xy[0]**2+xy[1]**2)
        else:
            raise TypeError('Input must be array, tuple, or list')
        
        
        
    def __repr__(self):
        return '{}'.format(self.coordvec)
    
    
    
    
    def trans(self,other):
        if isinstance(other,ndarray):
            if other.shape==(2,1) or other.shape==(1,2) or other.shape==(2,):
                other.shape=(2,)
                xtransmat=array([[1,0],[-1*other[0],1]])
                ytransmat=array([[1,0],[-1*other[1],1]])
                x=dot(xtransmat,self.xvec)
                y=dot(ytransmat,self.yvec)
                return(gtrans2vec((x[1,0],y[1,0])))
            else:
                raise TypeError('The velocities must be a 2-vec')
        else:
            raise TypeError('Argument must be an array')
            
    def transangle(self,other):
        a=self.trans(other)
        return(a.angle)


v=linspace(0,1,10001)
a=-1
for theta in [math.pi/2,math.pi*80/180,math.pi*70/180]:
    a+=1
    p=[[],[],[]]
    pos90=gtrans2vec((cos(theta),sin(theta)))
    for i in range(10001):
        p[a].append(pos90.transangle(array([-v[i],0])))
    plot(v,p[a])

L=[]
for i in range(10001):
    L.append(90-arctan(v[i])*180/pi)
plot(v,L)


