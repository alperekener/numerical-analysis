# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:30:49 2020

@author: alperekener
"""
import math


def f(x): #soruda verilen fonksiyonu burada tanımla
    
    sonuc= float((x**3)-(x**2)+(4*x)-4)
    return sonuc

def fturev(x): #soruda verilen fonksiyonu burada tanımla
    
    sonuc= float((3*x**2)-(2*x)+4)
    return sonuc 
    
x0=float(input("x0: "))
gercek=float(input("Gerçek kök: "))

sayac=1
ea=100
x0fonk=f(x0)
x0turevfonk=fturev(x0)
x1= float(x0-(f(x0)/fturev(x0)))
ea= float((abs((x1-x0)/x1))*100)
oran=float((abs((gercek-x1)/gercek))*100)
et=round(oran,5)
print(" i: 0 | xi: {} | x(i+1): {} | f(xi): {} | f'(xi): {} | Ea: %{} | Et: {} ".format(x0,x1,x0fonk,x0turevfonk,ea,et))

#while(ea>0.01):   #hata oranı verirse
for i in range (0,2):
    
    x0=x1
    
    x1= float(x0-(f(x0)/fturev(x0)))
        
    x1fonk=f(x1)
    x1turevfonk=fturev(x1)
    
    
    ea= float((abs((x1-x0)/x1))*100)
    
    ea=round(ea,8)
    oran=float((abs((gercek-x1)/gercek))*100)
    et=round(oran,5)
    
    
    print(" i: {} | xi: {} | x(i+1): {} |f(xi): {} | f'(xi): {} | Ea: %{} | Et: %{} ".format(sayac,x0,x1,x1fonk,x1turevfonk,ea,et))
    sayac+=1
    
    