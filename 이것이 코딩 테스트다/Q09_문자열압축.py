#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(s):
    answer = 1
    
    if len(s) == 1:
        return answer
        
    answer_list = []
    
    half = len(s) // 2
    
    for i in range(1, half + 1):
        a = 0
        count = 1
        compare = s[0:i]
        
        for j in range(1, len(s) // i):
            if compare == s[i * j:i * (j + 1)]:
                count += 1
            else:
                if count == 1:
                    a += i
                else:
                    a += len(str(count)) + i
                count = 1
                compare = s[i * j:i * (j + 1)]
        if count == 1:
            a += i
        else:
            a += len(str(count)) + i
            
        # 나누어 떨어지지 않는 경우
        a += len(s) % i
        
        answer_list.append(a)
        
    answer = min(answer_list)
    
    return answer

