# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:14:50 2020

@author: alperekener
"""

import math

def f(x):
    
    sonuc= float(-1.5*(x**6)-(2*x**4)+12*x)
    return sonuc

def fturev(x): #fonksiyonun türevi
    
    sonuc= float(-9*(x**5)-(8*x**3)+12)
    return sonuc

def fturev2(x): #fonksiyonun 2. türevi
    
    sonuc= float((-45*x**4)-(24*x**2))
    return sonuc

x0=float(input("x0: "))

for i in range(0,5):
    
    print(" i: {}  |  x: {}  |  f(x): {}  |  f'(x): {}  |  f''(x): {} ".format(i,x0,f(x0),fturev(x0),fturev2(x0)))
    
    yedek = x0
    x0 = yedek-(fturev(yedek)/fturev2(yedek))