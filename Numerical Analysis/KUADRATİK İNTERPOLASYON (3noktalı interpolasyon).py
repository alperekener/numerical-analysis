# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:30:49 2020

@author: alperekener
"""
import math


def f(b0,b1,b2,x0,x1,x): #soruda verilen fonksiyonu burada tanımla
    sonuc = float (b0 + (b1*(x-x0)) + (b2*(x-x0)*(x-x1)))
    return sonuc


    
x0=float(input("x0: "))
fx0= float(input("f(x0): "))

x1=float(input("x1: "))
fx1= float(input("f(x1): "))

x2=float(input("x2: "))
fx2= float(input("f(x2): "))

x=float(input("x: "))
gercek=float(input("Gerçek kök: "))

b0 = fx0
b1 = float ((fx1-fx0)/(x1-x0))

pay1=float((fx2-fx1)/(x2-x1))
pay2=float((fx1-fx0)/(x1-x0))
pay=pay1-pay2
payda=float(x2-x0)
b2= float(pay/payda)

sonuc = f(b0,b1,b2,x0,x1,x)

et= float ((gercek-sonuc)/gercek)*100

print("\n b0: {}  |  b1: {}  |  b2: {}  ".format(b0,b1,b2))

print("\n f(x) = f({}) = {}  |  Et: %{} ".format(x,sonuc,et))
