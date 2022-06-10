# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:30:49 2020

@author: alperekener
"""
import math


def f(x0,x1,x,fx0,fx1): #soruda verilen fonksiyonu burada tanımla
    pay= float((fx1-fx0)*(x-x0))
    payda= float(x1-x0)
    sonuc = float(fx0+(pay/payda))
    return sonuc


    
x0=float(input("x0: "))
fx0= float(input("f(x0): "))

x1=float(input("x1: "))
fx1= float(input("f(x1): "))

x=float(input("x: "))
gercek=float(input("Gerçek kök: "))

sonuc=f(x0,x1,x,fx0,fx1)

et= float ((gercek-sonuc)/gercek)*100

print("\n x0: {}  |  x1: {}  |  x: {}  ".format(x0,x1,x))
print("\n f({}): {}  |  f({}): {}  ".format(,x0,fx0,x1,fx1))
print("\n f(x) = f({}) = {}  |  Et: %{} ".format(x,sonuc,et))
