# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:23:26 2020

@author: alperekener
"""

ldizisi=[]
x=[]
fdizisi=[]
n=int(input("Veri değeri sayısı: "))
bulunacak=float(input("x: "))

for i in range(0,n):
    nokta=float(input("x({}): ".format(i)))
    f=float(input("f(x{}): ".format(i)))
    x.append(nokta)
    fdizisi.append(f)
sonuc=1

for i in range (0,n):
    for j in range(0,n):
        if(j!=i):
            deger= float ((bulunacak-x[j])/(x[i]-x[j]))
            sonuc= float (sonuc*deger)          
      
        
    ldizisi.append(sonuc)
    sonuc=1

total=0
    
for g in range(0,n):
    islem= float (ldizisi[g]*fdizisi[g])
    total=total+islem
print("------------------------------------------")

for i in range (0,n):
    print("L{}: {}".format(i,ldizisi[i]))
print("\n ---------------------------------------")
print("\n f({}): {}".format(bulunacak,total))



            