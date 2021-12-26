# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 18:53:19 2021

@author: User
"""


# from collections import deque
# def search(start_node,target="Elon mask"):
#     search_queue=deque()
#     search_queue+=graph[start_node]
#     searched=set()
#     while search_queue:
#         person=search_queue.popleft()
#         if person not in searched:
#             if person==target:
#                 print(f"{target} ni topdik!")
#                 return True
#             else:
#                 search_queue+=graph[person]
#     return False

# if __name__=="__main__":
#     graph={'siz':['ali','vali','tohir'],
#            'ali':['aziz','olim'],
#            'vali':['botir','ziyoda'],
#            'tohir':['Elon mask','mohir'],
#            'olim':[],'aziz':[],'botir':[],
#            'ziyoda':[],'Elon mask':[]}
#     search('siz','Elon mask')


# help(deque)
# Help on class deque in module collections:

# class deque(builtins.object):
#  |  deque([iterable[, maxlen]]) --> deque object
#  |  
#  |  A list-like sequence optimized for data accesses near its endpoints.
#  |  
#  |  Methods defined here:
#  |  
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |  
#  |  __bool__(self, /)
#  |      self != 0
#  |  
#  |  __contains__(self, key, /)
#  |      Return key in self.
#  |  
#  |  __copy__(...)
#  |      Return a shallow copy of a deque.
#  |  
#  |  __delitem__(self, key, /)
#  |      Delete self[key].
#  |  
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |  
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |  
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |  
#  |  __getitem__(self, key, /)
#  |      Return self[key].
#  |  
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |  
#  |  __iadd__(self, value, /)
#  |      Implement self+=value.
#  |  
#  |  __imul__(self, value, /)
#  |      Implement self*=value.
#  |  
#  |  __init__(self, /, *args, **kwargs)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |  
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |  
#  |  __len__(self, /)
#  |      Return len(self).
#  |  
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |  
#  |  __mul__(self, value, /)
#  |      Return self*value.
#  |  
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |  
#  |  __reduce__(...)
#  |      Return state information for pickling.
#  |  
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |  
#  |  __reversed__(...)
#  |      D.__reversed__() -- return a reverse iterator over the deque
#  |  
#  |  __rmul__(self, value, /)
#  |      Return value*self.
#  |  
#  |  __setitem__(self, key, value, /)
#  |      Set self[key] to value.
#  |  
#  |  __sizeof__(...)
#  |      D.__sizeof__() -- size of D in memory, in bytes
#  |  
#  |  append(...)
#  |      Add an element to the right side of the deque.
#  |  
#  |  appendleft(...)
#  |      Add an element to the left side of the deque.
#  |  
#  |  clear(...)
#  |      Remove all elements from the deque.
#  |  
#  |  copy(...)
#  |      Return a shallow copy of a deque.
#  |  
#  |  count(...)
#  |      D.count(value) -> integer -- return number of occurrences of value
#  |  
#  |  extend(...)
#  |      Extend the right side of the deque with elements from the iterable
#  |  
#  |  extendleft(...)
#  |      Extend the left side of the deque with elements from the iterable
#  |  
#  |  index(...)
#  |      D.index(value, [start, [stop]]) -> integer -- return first index of value.
#  |      Raises ValueError if the value is not present.
#  |  
#  |  insert(...)
#  |      D.insert(index, object) -- insert object before index
#  |  
#  |  pop(...)
#  |      Remove and return the rightmost element.
#  |  
#  |  popleft(...)
#  |      Remove and return the leftmost element.
#  |  
#  |  remove(...)
#  |      D.remove(value) -- remove first occurrence of value.
#  |  
#  |  reverse(...)
#  |      D.reverse() -- reverse *IN PLACE*
#  |  
#  |  rotate(...)
#  |      Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |  
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |  
#  |  maxlen
#  |      maximum size of a deque or None if unbounded
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |  
#  |  __hash__ = None


















