# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:32:23 2020

@author: alperekener
"""
import math

totalx=0
totaly=0
totalxkare=0
totalxy=0
sayac=0

for i in range(0,5):
    x=float(input("x: "))
    y=float(input("y: "))
    
    #x=math.log(x,10)  Güç denklemi gibi çevirme gereken şeyler varsa
    #y=math.log(y,10)  Burdan x ve y değerlerini ayarla.
    xkare=x*x
    xy= x*y
    totalx=totalx+x
    totaly=totaly+y
    totalxkare=totalxkare+xkare
    totalxy=totalxy+xy
    sayac=sayac+1
    print("\n {}. ADIM:  xy= {}  ,   xkare= {}".format(sayac,xy,xkare))
    print("___________________________________")
    

print("\n Toplam | x:{} | y:{} | xy:{} | xkare:{}".format(totalx,totaly,totalxy,totalxkare))
print("___________________________________")
print("\n{} a(0) + {} a(1) = {} \n{} a(0) + {} a(1) = {}".format(sayac,totalx,totaly,totalx,totalxkare,totalxy))