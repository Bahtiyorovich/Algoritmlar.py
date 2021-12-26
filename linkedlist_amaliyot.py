# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:09:48 2021

@author: User
"""

from linkedlistfunc import Node, Linkedlist
# linked list yaratamiz:

llist=Linkedlist

llist.head=Node('Dushanba')
tuesday=Node('Seshanba')
wednesday=Node('Chorshanba')

#Tugunlarni bog'laymiz
llist.head.next=tuesday
tuesday.next=wednesday

# Qiymatlarni consolga chiqarish

llist.push('Yakshanba')
llist.printlist()
llist.append("Juma")
#llist.printList()

llist.deleteNode('Yakshanba')
llist.printlist()










































