def solution(n, lost, reserve):
    answer = n - len(lost)
    dic = {}
    
    # 딕셔너리 초기화
    for r in reserve:
        # 체육복을 잃어버렸지만 여벌이 있는 사람
        if r in lost:
            dic[r] = 1
            answer += 1
        else:
            # 체육복을 잃어버리지 않고 여벌도 있는 사람
            dic[r] = 0
    
    for l in lost:
        # 본인 여벌 사용
        if l in reserve:
            continue
        if l - 1 in reserve:
            # 다른 사람의 여벌 사용
            if dic[l - 1] == 0:
                dic[l - 1] = 1
                answer += 1
                continue
        if l + 1 in reserve:
            if dic[l + 1] == 0:
                dic[l + 1] = 1
                answer += 1
                
    return answer

