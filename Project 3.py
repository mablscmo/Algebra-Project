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
        
    def veltrans(self,vx,vy=0,vz=0):
        gamma=1/sqrt(1-(vx**2+vy**2+vz**2))
        transvm=array([[gamma,-vx*gamma,-vy*gamma,-vz*gamma],[-vx*gamma,(gamma-1)vx**2/(vx**2+vy**2+vz**2)+1,-vx*gamma,(gamma-1)vx*vy/(vx**2+vy**2+vz**2),-vx*gamma,(gamma-1)vx*vz/(vx**2+vy**2+vz**2)],[-vy*gamma,(gamma-1)vy*vx/(vx**2+vy**2+vz**2),(gamma-1)vy**2/(vx**2+vy**2+vz**2)+1,(gamma-1)vy*vz/(vx**2+vy**2+vz**2)],[-vz*gamma,(gamma-1)vz*vx/(vx**2+vy**2+vz**2),(gamma-1)vz*vy/(vx**2+vy**2+vz**2),(gamma-1)vz**2/(vx**2+vy**2+vz**2)+1]) 
        return
    
