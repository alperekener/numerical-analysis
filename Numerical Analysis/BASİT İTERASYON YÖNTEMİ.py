# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:19:05 2020

@author: alperekener
"""
import math

def f(x): #soruda verilen fonksiyonu burada tanımla
    sonuc= float(math.exp(-x))
    return sonuc


x0=float(input("x0: "))
gercek=float(input("Gerçek kök (verilmemişse 1 yaz): "))
sayac=1

ea=100.00

#for i in range(0,10):   #iterasyon sayısı isterse
while(ea>1.93):   #hata payı verirse
    x1 = f(x0)
    ea= float((abs((x1-x0)/x1))*100)
    et= float((abs((gercek-x1)/gercek))*100)
    print(" i: {} | x({}): {} | Ea: %{} | Et: %{}".format(sayac,sayac,x1,ea,et))
    sayac+=1
    yedek=x1
    x0=x1
    
    