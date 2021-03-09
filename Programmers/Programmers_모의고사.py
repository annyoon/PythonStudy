#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(answers):
    answer = []
    
    count = [0, 0, 0]
    
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if student1[i % 5] == answers[i]:
            count[0] += 1
        if student2[i % 8] == answers[i]:
            count[1] += 1
        if student3[i % 10] == answers[i]:
            count[2] += 1
            
    score = max(count)
    
    if count[0] == score:
        answer.append(1)
    if count[1] == score:
        answer.append(2)
    if count[2] == score:
        answer.append(3)
    
    return answer

