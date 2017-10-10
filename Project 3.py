# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:01:33 2017
@author: tina-
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
        return(FourVector(transm.dot(self.coordvec)))
    
    def ptrans(self, xv):
        g=1/sqrt(1-xv**2)
        transm=array([[g,-xv*g,0,0],[-xv*g,g,0,0],[0,0,1,0],[0,0,0,1]])
        a=array([[self.t,0,0,0]])
        a.shape=(4,1)
        return(FourVector(transm.dot(a)))
    
#x=linspace(0,1,5000,endpoint=False)
#y=[]
#t0=FourVector((1,0,0,0))
#for i in x:
#    y.append(t0.ptrans(i).t)
        
#plot(x,y)    


class VelocityVector:
    def __init__(self,vxyz):
        if isinstance(vxyz,ndarray):
            vxyz.shape=(3,1)
            self.vx=vxyz[0,]
            self.vy=vxyz[1,]
            self.vz=vxyz[2,]
            self.coordvec=vxyz
        elif isinstance(vxyz,(tuple,list)):
            self.vx=vxyz[0]
            self.vy=vxyz[1]
            self.vz=vxyz[2]
            self.coordvec=array([vxyz])
            self.coordvec.shape=(3,1)
        else:
            raise TypeError('Input must be array, tuple, or list')
            
    def __repr__(self):
        return '{}'.format(self.coordvec)
        
    def veltrans(self,vx):
        return 'not ready'
           
xv=
yv=
zv=
gamma=1/sqrt(1-(xv**2+yv**2+zv**2))

transvm=array([[gamma,-xv*gamma,-yv*gamma,-zv*gamma],[-xv*gamma,(gamma-1)xv**2/(xv**2+yv**2+zv**2)+1,-xv*gamma,(gamma-1)xv*yv/(xv**2+yv**2+zv**2),-xv*gamma,(gamma-1)xv*zv/(xv**2+yv**2+zv**2)],[-yv*gamma,(gamma-1)yv*xv/(xv**2+yv**2+zv**2),(gamma-1)yv**2/(xv**2+yv**2+zv**2)+1,(gamma-1)yv*zv/(xv**2+yv**2+zv**2)],[-zv*gamma,(gamma-1)zv*xv/(xv**2+yv**2+zv**2),(gamma-1)zv*yv/(xv**2+yv**2+zv**2),(gamma-1)zv**2/(xv**2+yv**2+zv**2)+1])      
        
        
