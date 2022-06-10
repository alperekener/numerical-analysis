# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:37:07 2020

@author: alperekener
"""
iterasyon=1
c1 = 0
c2 = 0
c3 = 0
c4= 0
hata1=100
hata2=100
hata3=100
hata4=100
for i in range(0,7):
#while ((hata1>=5)&(hata2>=5)&(hata3>=5)): #Buradaki 5 yerine izin verilen hata %sini yaz.
    yedek1=float(c1)
    yedek2= float(c2)
    yedek3=float (c3)
    yedek4= float (c3)
    
    c1=float((1-c2-c3)/4) #Sorudaki denklemden bilinmeyenleri çek.
    
    
    c2=float((2-c1-c4)/4)
    
    
    c3=float((((-1)*(c1+c4)))/4)
    
    
    c4=float((1-(c2+c3))/4)
    
    
    hata1= float(((c1-yedek1)/c1)*100)
    hata2= float(((c2-yedek2)/c2)*100)
    hata3= float(((c3-yedek3)/c3)*100)
    hata4= float(((c4-yedek4)/c4)*100)
    
    print("---- {}. İTERASYON --- \n c1:{} \n c2:{} \n c3: {} \n c4: {} \n Hata1:%{} \n Hata2:%{} \n Hata3:%{} \n Hata4: {}".format(iterasyon,c1,c2,c3,c4,hata1,hata2,hata3,hata4))
    print("________________________________________")
    iterasyon+=1