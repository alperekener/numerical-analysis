# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:19:05 2020

@author: alperekener
"""
import math

def f(x): #soruda verilen fonksiyonu burada tanımla
    sonuc= float((math.pow(x,3))-(7*math.pow(x,2))+14*x-6)
    return sonuc

xa=float(input("Xa: "))
xü=float(input("Xü: "))

xafonk= f(xa)
xüfonk= f(xü)
sayac=1
kontrol=xafonk*xüfonk
ea=100.00

if(kontrol>=0):
    print("f(xa).f(xü) < 0  koşulu sağlanmadı")
else:
    #for i in range(0,5):  #iterasyon sayısı verirse 5 yerine o sayıyı yaz.
    while (ea>0.001):   #Hata yüzdesi verirse bunu kullan.   
        xafonk= f(xa)
        xüfonk= f(xü)
        xr = float((xa+xü)/2)
        kökfonk= float(f(xr))
        if(sayac>1):
            ea = (abs((yedek-xr)/yedek))*100
        else:
            ea=100
       
        print("\n --------------- {}. İTERASYON --------------- ".format(sayac))
        print(" xa: {} | xü: {} | xr: {} | f(xa): {} | f(xü): {} | f(xr): {} | Ea: %{} ".format(xa,xü,xr,xafonk,xüfonk,kökfonk,ea))
        sayac=sayac+1
        if(xafonk*kökfonk<0):
            yedek=xr
            xü=xr
        else:
            yedek=xr
            xa=xr
    
    