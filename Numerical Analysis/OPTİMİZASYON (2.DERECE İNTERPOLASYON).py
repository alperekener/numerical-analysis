# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:24:57 2020

@author: alperekener
"""
import math
def f(x): #trigo. olursa sayıyı önce dereceye sonra radyana çevir.
    derece= math.degrees(x)
    sonuc= float((2*(math.sin(math.radians(derece))))-(math.pow(x,2)/10))
    return sonuc



x0 = float(input("x0: "))
x1 = float(input("x1: "))
x2 = float(input("x2: "))

pay= float((f(x0)*(math.pow(x1,2)-math.pow(x2,2)))+(f(x1)*(math.pow(x2,2)-math.pow(x0,2)))+(f(x2)*(math.pow(x0,2)-math.pow(x1,2))))
payda= float ((2*f(x0)*(x1-x2))+(2*f(x1)*(x2-x0))+(2*f(x2)*(x0-x1)))
    
x3=float(pay/payda)

print("\n i: 1  | x0: {}  |  x1: {}  | x2: {}  ".format(x0,x1,x2))
print(" f(x0): {}  | f(x1): {}  | f(x2): {}  |".format(f(x0),f(x1),f(x2)))
print(" x3: {}  |  f(x3):  {} ".format(x3,f(x3)))
print("---------------------------------------------")
sayac=2

for i in range(0,5):
    
    if(f(x1)<f(x3)):
        x0=x1
        yedek=x1
        x1=x3
    else:
        x2=x1
        yedek=x1
        x1=x3
    
    
    ea= float((abs((f(x3)-f(yedek))/f(x3)))*100)
    
    pay= float((f(x0)*(math.pow(x1,2)-math.pow(x2,2)))+(f(x1)*(math.pow(x2,2)-math.pow(x0,2)))+(f(x2)*(math.pow(x0,2)-math.pow(x1,2))))
    payda= float ((2*f(x0)*(x1-x2))+(2*f(x1)*(x2-x0))+(2*f(x2)*(x0-x1)))
    
    x3=float(pay/payda)
    
    print("\n i: {}  | x0: {}  |  x1: {}  | x2: {}  ".format(sayac,x0,x1,x2))
    print(" f(x0): {}  | f(x1): {}  | f(x2): {}  |".format(f(x0),f(x1),f(x2)))
    print(" x3: {}  |  f(x3):  {}  |  Hata: %{}".format(x3,f(x3),ea)) 
    print("-----------------------------------------------------------")
    
    sayac+=1