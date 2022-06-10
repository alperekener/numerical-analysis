# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:30:49 2020

@author: alperekener
"""
import math


def f(x): #soruda verilen fonksiyonu burada tanımla
    sonuc= float(math.exp(-x)-x)
    return sonuc

    
x0=float(input("x0: "))
s=float(input("S: "))
gercek=float(input("Gerçek kök (yoksa rastgele gir): "))  #Outputtaki Et %si. kök verilmemişse Ea'ya bak.
sayac=1
ea=100
x0fonk=f(x0)

verifonk=f(x0+(s*x0))

print(" i: 0 | x(0): {} | f(x(0): {} | f(x0,S.x(0): {} ".format(x0,x0fonk,verifonk))
#while(ea>0.01):   #hata oranı verirse
for i in range (0,2):
    
    deger=x0*s
    x1= float(x0-(deger*(f(x0)/(f(x0+deger)-f(x0)))))
        
    x1fonk=f(x1)
    veri=x0+deger
    verifonk=f(veri)
    
    if(sayac==1):
        ea=100
    else:
        ea= float((abs((x1-x0)/x1))*100)
    
    
    et=float((abs((gercek-x1)/gercek))*100)
    
    
    
    print(" i: {} | x({}): {} | f(x({}): {} | f(x{},S.x{}): {} | Ea: %{} | Et: %{} ".format(sayac,sayac,x1,sayac,x1fonk,sayac,sayac,verifonk,ea,et))
    sayac+=1
    
    x0=x1