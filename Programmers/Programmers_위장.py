def solution(clothes):
    answer = 0
    dic = {}
    sum = 1
    
    for i,j in clothes:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1
    
    for i in dic.values():
        sum = sum * (i + 1)
            
    answer = sum - 1
    
    return answer
