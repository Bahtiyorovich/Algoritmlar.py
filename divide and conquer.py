# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:26:20 2021

@author: User
"""
# 2 ta sonning eng katta umumiy bo'luvchisini topish
# 1-usul (ayirish usuli)

# def gcd(a,b):    
#     if a==0:
#         return b
#     if a>b:
#         a,b=b,a    
#     return gcd(b-a,a)

# 2- usul qoldiqli usuli
# def gcd(a, b):
#     if a == 0 :
#         return b      
#     return gcd(b%a, a)


# def summa(array):
#     if array == []:
#         return 0
#     return array[0]+summa(array[1:])

#array qiymatlari sonini topish:
    
# def ar_len(array):
#     return len(array)

# def maxArray(array):
#     array.sort()
#     return f"Eng kichigi: {array[0]},eng kattasi: {array[-1]}"

#Binarysearch bilan rekursiyaning birga ishlatilishi:
# def binarySearch(array,value,start=0,end=None):
#     array.sort()
#     if end is None:
#         end = len(array)-1
#     if start>end:
#         return None
    
#     mid = (start+end)//2
#     if array[mid]==value:
#         return mid
#     elif array[mid]>value:
#         return binarySearch(array,value,start,mid-1)
#     else:
#         return binarySearch(array,value,mid+1,end)
#     return None











