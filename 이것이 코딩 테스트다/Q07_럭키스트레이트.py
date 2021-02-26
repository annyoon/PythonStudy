#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = input()
list1 = []
list2 = []

size = len(n) // 2

for i in range(size):
    list1.append(int(n[i]))
    list2.append(int(n[i + size]))
    
if sum(list1) == sum(list2):
    print("LUCKY")
else:
    print("READY")

