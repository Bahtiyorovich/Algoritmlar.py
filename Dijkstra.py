# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 20:48:30 2021

@author: User
"""


# Bu yerda graf yasadik:
# graph={}
# graph['A']=['B','C']
# graph['A']={}
# graph['A']['B']=2
# graph['A']['C']=6
# print(graph)
# print(graph['A'].keys())
# print(graph['A']['B'])
# print(graph['A']['C'])
# from pprint import pprint as print
# print(graph)
# otalar = {
#     'B': 'A',
#     'C': 'A',
#     'D': None,
#     'E': None,
#     'F': None,}
# ishlandi=[]

# narxlar = {
#     'B': 2,
#     'C': 6,
#     'D': float('inf'),
#     'E': float('inf'),
#     'F': float('inf')}
# # eng arzon tugun topish funksiyasi:
# def eng_arzon_tugun_top(narxlar):
#     eng_arzon=float("inf")
#     eng_arzon_tugun=None
#     for tugun in narxlar:
#         narx = narxlar[tugun]
#         if narx < eng_arzon and tugun not in ishlandi:
#             eng_arzon = narx
#             eng_arzon_tugun = tugun
#     return eng_arzon_tugun

# print(narxlar)    
# tugun=eng_arzon_tugun_top(narxlar)
# print(f"Eng arzon tugun: {tugun}")

# # dijkstra algoritmi kodi:
# while tugun is not None:
#     qoshnilar = graph[tugun] # Eng yaqin tugunning qo'shnilarini topamiz
#     narx = narxlar[tugun] # Ularning narxini olamiz
#     for qoshni in qoshnilar.keys(): # Har bir qo'shni uchun...
#         yangi_narx = narx + qoshnilar[qoshni] # shu qo'shniga borish narxini hisoblaymiz
#         if narxlar[qoshni]>yangi_narx: # agar bu tugunga borish avvalgidan arzonroq bo'lsa:
#             narxlar[qoshni] = yangi_narx # shu tugunga borish narxini yangilaymiz
#             otalar[qoshni] = tugun # va bu tugun otasini ham yangilaymiz.
#     ishlandi.append(tugun) # tugunn ishlov berilgan tugunlar qatoriga qo'shamiz
#     tugun = eng_arzon_tugun_top(narxlar)  
# print(narxlar)























