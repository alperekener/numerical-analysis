# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:32:23 2020

@author: alperekener
"""
import math

totalt=0
totalz=0
totaltkare=0
totaltz=0
sayac=0

for i in range(0,4):
    x=float(input("x: "))
    y=float(input("y: "))
    
    #x=math.log(x,10)  Güç denklemi gibi çevirme gereken şeyler varsa
    #y=math.log(y,10)  Burdan x ve y değerlerini ayarla.
   
    t=math.log(x,10)
    z=math.log(y,10)
    
    tkare=t*t
    tz= t*z
    totalt=totalt+t
    totalz=totalz+z
    
    totaltkare=totaltkare+tkare
    totaltz=totaltz+tz
    sayac=sayac+1
    
    print("\n {}. ADIM:  t= {}  ,   z= {}  ,  tkare= {}  ,  tz= {} ".format(sayac,t,z,tkare,tz))
    print("___________________________________")
    

print("\n Toplam | t:{} | z:{} | tkare:{} | tz:{}".format(totalt,totalz,totaltkare,totaltz))
print("___________________________________")
print("\n{} a(0) + {} a(1) = {} \n{} a(0) + {} a(1) = {}".format(sayac,totalt,totalz,totalt,totaltkare,totaltz))