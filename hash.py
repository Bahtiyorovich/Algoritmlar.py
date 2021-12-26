# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 12:44:56 2021

@author: User
"""


# hash jadvallari bilan amaliyot:

#1:

# def hashfun1(text):
#     """Kiritilgan matn uzunligini hash sifatida qaytarish"""
#     return len(text)
# print(hashfun1("olma"))

#2:
# import string
# alphabet=list(string.ascii_lowercase)
# def hashfun2(text):
#     """Kiritilgan matnning birinchi harfini index sifatida qaytaradi"""
#     return alphabet.index(text[0].lower())
# print(hashfun2("apple"))

# 3:
 
# import string
# alphabet=list(string.ascii_lowercase)
# primes=[2,3,5,7,11,13,17,19,23,29,31,41,43,47,53,59,61,67,71,73]
# def hashfun3(text):
#     """Kiritlgan matnning har bir harfini mos tub songa almashtiradi va barcha sonlarni qo'shib yuboradi
#     Yuqoridagi yig'indini 10 ga bo'ladi va qoldiqni qaytaradi"""
#     sum=0
#     for t in text.lower():
#         sum+=primes[alphabet.index(t)]

#     return sum%10
# print(hashfun3("orange"))



















