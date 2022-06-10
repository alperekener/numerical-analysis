# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:30:49 2020

@author: alperekener
"""
import math


def f(x): #soruda verilen fonksiyonu burada tanımla
    sonuc= float(math.pow(x,3)-(13*x)-12)
    return sonuc

    
x0=float(input("x0: "))
x1=float(input("x1: "))
x2=float(input("x2: ")) #Eğer iki nokta verilmişse, 3. bulmak için ikisinin ort al.


sayac=1
ea=100
print("i: 0 | xr: {} | Ea: ".format(x2))
#while(ea>0.01):   #hata oranı verirse
for i in range (0,4):
    
    x0fonk=f(x0)
    x1fonk=f(x1)
    x2fonk=f(x2)
    
    h0=x1-x0
    s0= float((x1fonk-x0fonk)/(x1-x0))
    
    h1=x2-x1
    s1= float ((x2fonk-x1fonk)/(x2-x1))
    
    a= (s1-s0)/(h1+h0)
    b= (a*h1)+s1
    c=f(x2)
    
    delta= float (math.pow(b,2)-(4*a*c))
    kokdelta= math.sqrt(delta)
    
    payda1= b+kokdelta
    payda2= b-kokdelta
    
    if(payda1>payda2):
        payda=payda1
    else:
        payda=payda2
        
    x3= float (x2+ (((-2)*c)/payda))
    
    
    
    
    ea= float((abs((x3-x2)/x3))*100)
    
      
    
    
    
    print(" i: {} | xr: {} | Ea: %{} ".format(sayac,x3,ea))
    sayac+=1
    
    x0=x1
    x1=x2
    x2=x3