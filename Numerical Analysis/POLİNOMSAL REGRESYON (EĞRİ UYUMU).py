# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:32:23 2020

@author: alperekener
"""
import math

totalx=0
totaly=0
totalxkare=0
totalxküp=0
totalx4=0
totalxy=0
totalxkarey=0
sayac=0

for i in range(0,6): #Kaç tane nokta varsa 5 yerine yaz.
    x=float(input("x: "))
    y=float(input("y: "))
    
    
    
    xkare=x*x
    xy= x*y
    xküp=math.pow(x,3)
    x4=math.pow(x,4)
    xkarey=xkare*y
    
    totalx=totalx+x
    totaly=totaly+y
    totalxkare=totalxkare+xkare
    totalxy=totalxy+xy
    totalxküp=totalxküp+xküp
    totalx4=totalx4+x4
    totalxkarey=totalxkarey+xkarey
    
    sayac=sayac+1
    
    print("\n {}. ADIM: xkare= {} , xküp= {} , x^4= {} , xy= {} , x^2.y= {} ".format(sayac,xkare,xküp,x4,xy,xkarey))
    print("_________________________________________________________________")
    

print("\n Toplam | x:{} | y:{} | xkare:{} | xküp: {} | x^4: {} | xy: {} | x^2.y: {}".format(totalx,totaly,totalxkare,totalxküp,totalx4,totalxy,totalxkarey))
print("____________________________________________________________________________")
print("\n{} a(0) + {} a(1) + {} a(2) = {} ".format(sayac,totalx,totalxkare,totaly))
print("\n{} a(0) + {} a(1) + {} a(2) = {} ".format(totalx,totalxkare,totalxküp,totalxy))
print("\n{} a(0) + {} a(1) + {} a(2) = {} ".format(totalxkare,totalxküp,totalx4,totalxkarey))

