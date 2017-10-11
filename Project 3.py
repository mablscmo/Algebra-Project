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
    
def vtplot(tstart,tend=False,numtime=False,numpoints=1000):
    if tend==False:
        x=linspace(0,1,numpoints,endpoint=False)
        y=[]
        t0=FourVector((tstart,0,0,0))
        for i in x:
            y.append(t0.ptrans(i).t)
        plot(x,y)
    elif numtime==False:
        for t in range(tstart,tend+1):
            x=linspace(0,1,numpoints,endpoint=False)
            y=[]
            t0=FourVector((t,0,0,0))
            for i in x:
                y.append(t0.ptrans(i).t)
            if t==tstart:
                    plot(x,y,'r')
            elif t==tend:
                plot(x,y,'b')
            else:
                plot(x,y)  
    else:
        for t in linspace(tstart,tend,numtime):
            x=linspace(0,1,numpoints,endpoint=False)
            y=[]
            t0=FourVector((t,0,0,0))
            for i in x:
                y.append(t0.ptrans(i).t)
            if t==tstart:
                    plot(x,y,'r')
            elif t==tend:
                plot(x,y,'b')
            else:
                plot(x,y)

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
        
    def veltrans(self,ux):
        gamma=sqrt(1-ux**2)
        vxp=(self.vx-ux)/(1-self.vx*ux)
        vyp=self.vy/(gamma*(1-self.vy*ux))
        vzp=self.vz/(gamma*(1-self.vz*ux))
        return(VelocityVector((vxp,vyp,vzp)))
    


v=linspace(0,1,10000,endpoint=False)
a=-1
for theta in [math.pi/2,math.pi*80/180,math.pi*70/180]:
    a+=1
    p=[[],[],[]]
    pos=FourVector((1,cos(theta),sin(theta),0))
    for i in range(10000):
        newpos=pos.trans(-v[i])
        (x,y)=(newpos.x,newpos.y)
        newang=arccos(x/(x**2+y**2))*180/pi
        p[a].append(newang)
    plot(v,p[a])



L=[]
for i in range(10000):
    L.append(90-arcsin(v[i])*180/pi)
plot(v,L,'r')
        
