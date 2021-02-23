#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(participant, completion):
    answer = ''
    dic = {}

    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        
    for i in completion:
        if i in dic:
            dic[i] -= 1
    
    for i in dic:
        if dic[i] == 1:
            answer = i
    
    return answer

