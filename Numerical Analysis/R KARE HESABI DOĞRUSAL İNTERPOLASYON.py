# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:31:33 2020

@author: alperekener
"""
import math

def yfonk(x):
    y= float ((-2.375716)+(0.2843819*x))  #Doğrusal interpol.de bulduğun denklemi yaz.
    return y

xdizisi=[]
ydizisi=[]
ytahmin=[]
ytoplam=0
payekledizisi=[]
paydaekledizisi=[]
for i in range(0,5): #nokta sayısı
    x=float(input("X: "))
    y=float(input("Y: "))
    ydizisi.append(y)
    ytahmin.append(yfonk(x))
    ytoplam=ytoplam+y
    
yort=ytoplam/5  #nokta sayısı  

    
paytoplam=0
paydatoplam=0
for i in range(0,5):
    taban1= (ydizisi[i]-ytahmin[i])
    payekle= math.pow(taban1,2)
    payekledizisi.append(payekle)
    paytoplam=paytoplam+payekle
    taban2= (ydizisi[i]-yort)
    paydaekle=math.pow(taban2,2)
    paydaekledizisi.append(paydaekle)
    paydatoplam=paydatoplam+paydaekle
    
rkare= float (1-(paytoplam/paydatoplam))

sayac=1

for i in range(0,5):
    print("\n {}. ADIM:  ytahmin: {}  ,  (yi-ytahmin)^2: {}  ,  (yi-yort)^2: {} ".format(sayac,ytahmin[i],payekledizisi[i],paydaekledizisi[i]))
    print("------------------------------------------------------------------------------------------------------------------------------------------")
print("\n   Y ort: {}  ,   R kare: {} ".format(yort,rkare))