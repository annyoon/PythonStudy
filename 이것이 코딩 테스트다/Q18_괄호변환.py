#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(p):
    answer = ''
    
    if len(p) == 0:
        return answer
    
    count1 = 0 # count '('
    count2 = 0 # count ')'
    
    for i in range(len(p)):
        if p[i] == '(':
            count1 += 1
        else:
            count2 += 1
            
        if count1 == count2:
            break
    
    u = p[:count1 + count2]
    v = p[count1 + count2:]
    
    if u[0] == '(':
        answer = u + solution(v) # u가 올바른 문자열
    else:
        string = "(" + solution(v) + ")"
        u = u[1:len(u) - 1]
        
        for j in range(len(u)):
            if u[j] == '(':
                string += ")"
            else:
                string += "("
                
        answer = string
        
    return answer

