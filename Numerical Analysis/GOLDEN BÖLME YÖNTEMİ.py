# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:24:57 2020

@author: alperekener
"""
import math

def f(x): #trigo. olursa sayıyı önce dereceye sonra radyana çevir.
    
    sonuc= float((-1.5*x**6)-(2*x**4)+12*x)
    #sonuc=float((-1.5*x**6)-(2*x**4)+(12*x))
    return sonuc

r = 0.618

xa = float(input("Xa: "))
xü = float(input("Xü: "))
sayac=2

d= float(r*(xü-xa))
x1= float(xa+d)
x2= float(xü-d)
    
fx1=f(x1)
fx2=f(x2)

    
print("\n i: 1   |  xa: {}  | xü: {}  |".format(xa,xü))
print("\n x1: {}  |  x2: {}  | f(x1): {} | f(x2): {}   ".format(x1,x2,fx1,fx2))
print("------------------------------------------------------")

yedek1= xü
yedek2= xa

if (fx1<fx2):
    xü=x1
    opt=x1

else:
    xa=x2
    opt=x2

for i in range(0,4):
    
    deger= float(abs((yedek1-yedek2)/opt)*100)
    ea= float ((1-r)*deger)
    
    d= float(r*(xü-xa))
    x1= float(xa+d)
    x2= float(xü-d)
    
    fx1=f(x1)
    fx2=f(x2)
    
    
    
    print("\n i: {}   |  xa: {}  | xü: {}  | Ea: %{}  | Xopt: {}   ".format(sayac,xa,xü,ea,opt))
    print("\n x1: {}  |  x2: {}  | f(x1): {} | f(x2): {}   ".format(x1,x2,fx1,fx2))
    print("------------------------------------------------------")
    
    yedek1=xü
    yedek2=xa
    
    if (fx1<fx2):
                
        xü=x1
        opt=x1

    else:
        xa=x2
        opt=x2
        
    sayac=sayac+1