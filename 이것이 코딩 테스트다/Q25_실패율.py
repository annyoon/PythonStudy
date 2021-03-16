def solution(N, stages):
    answer = []
    users = [0] * (N + 1) # 스테이지에 도달한 사람 카운트
    fail = [0] * (N + 1) # 아직 클리어하지 못한 사람 카운트
    
    for stage in stages:
        if stage != (N + 1):
            fail[stage] += 1
            users[stage] += 1
        for n in range(stage):
            users[n] += 1
    
    for i in range(1, N + 1):
        if users[i] == 0:
            answer.append([0, i])
        else:
            answer.append([fail[i]/users[i], i])
            
    answer.sort(key = lambda x: (-x[0], x[1]))
    
    for j in range(N):
        answer[j] = answer[j][1]
    
    return answer
