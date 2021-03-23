# 백준에서 시간초과가 뜬 풀이

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
count = 0
noCity = False
visited = [False] * (n + 1)

queue = deque([x])
answer = deque([x])
visited[x] = True

while count != k:
    v = queue.popleft()
    answer.popleft()

    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True

    if len(answer) == 0:
        answer = deque(list(queue))
        count += 1
        
    if len(queue) == 0:
        noCity = True
        break
        
if noCity:
    print(-1)
else:
    for a in answer:
        print(a)
