import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

city = [-1] * (n + 1)
city[x] = 0

queue = deque([x])
while queue:
    v = queue.popleft()
    
    for i in graph[v]:
        if city[i] == -1:
            city[i] = city[v] + 1
            queue.append(i)
        
for i in range(1, n + 1):
    if city[i] == k:
        print(i)
        
if k not in city:
    print(-1)
