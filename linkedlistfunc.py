# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:08:57 2021

@author: User
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Linkedlist:
    def __init__(self):
        self.head=None


    def printList(self):
        temp=self.head                
        while temp:
            print(temp.data)
            temp=temp.next


    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node


    def insertafter(self,prev_node,new_data):
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node


    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
            last.next=new_node

    def delete(self,key):
        temp=self.head
        if (temp and temp.data==key):
            self.head=temp.next
            temp=None
            return
        while temp:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            return
        prev.next=temp.next
        temp=None
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            