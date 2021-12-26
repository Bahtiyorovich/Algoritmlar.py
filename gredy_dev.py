# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 01:18:19 2021

@author: User
"""

# gredy algoritm:
import pickle # pickle- funksiyasi pickle yordamida yozilgan fayllarni faqat pythonning o'zida o'qish!
from pprint import pprint as print
# ma'lumotlarni o'qiymiz:
with open('binolar.dat','rb') as file:
    binolar=pickle.load(file)
    hududlar=pickle.load(file)
print(binolar)

# Gredy algoritmini kodini yozamiz:

yakuniy_binolar=set() # set()- funksiyasi bosh toplam yaratish:
while hududlar:
    best_bino=None
    qamralgan_hududlar=set()# set()- funksiyasi bosh toplam yaratish:
    for bino,bino_qamrovi in binolar.items():
        qamrov=hududlar&bino_qamrovi # &-funksiyasi toplam elementlarining kesishmasini aniqlaydi!
        print(f"{bino}:{qamrov}")
        if len(qamrov)>len(qamralgan_hududlar):
            best_bino=bino
            qamralgan_hududlar=qamrov
    hududlar-=qamralgan_hududlar
    yakuniy_binolar.add(best_bino) # add-funksiyasi elemntni yangi toplamga qoshish:
    print(f"Tanlangan bino: {best_bino}")
    print(f"Qolgan hududlar: {hududlar}")
    print(f"Tanlangan binolar: {yakuniy_binolar}")
    input() # kodimizni 'input' orqali qadamba-qadam bajariladigan qildik "Enter" ni bosasiz!
for key in yakuniy_binolar:
    print(binolar[key])
print("Amalyot yakunlandi!")   
    
    
    
    