# 2022.08.08
# 백준 / 1260번 DFS와 BFS

from collections import deque

ans_dfs = []
ans_bfs = []

def DFS(graph, n, visited):
    visited[n] = True
    ans_dfs.append(str(n))
    for i in graph[n]:
        if not visited[i]:
            visited[i] = True
            DFS(graph, i, visited)

def BFS(graph, n, visited):
    queue = deque([n])
    visited[n] = True

    while queue:
        v = queue.popleft()
        ans_bfs.append(str(v))
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M, V = map(int, input().split(' '))
graph = {x : set() for x in range(1, N+1)}

for i in range(1, M+1):
    a, b = map(int, input().split(' '))
    graph[a].add(b)
    graph[b].add(a)

for g in graph:
    graph[g] = list(graph[g])
    graph[g].sort()

DFS(graph, V, [False] * (N+1))
BFS(graph, V, [False] * (N+1))

print(' '.join(ans_dfs))
print(' '.join(ans_bfs))

# 입출력 예

# 입력 1
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 출력 1
# 1 2 4 3
# 1 2 3 4

# 입력 2
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1

# 출력 2
# 3 1 2 5 4
# 3 1 4 2 5

# 입력 3
# 10 10 4
# 5 4
# 6 4
# 6 8
# 8 9
# 1 10
# 2 10
# 10 3
# 8 2
# 1 7
# 4 10

# 출력 3
# 4 5 6 8 2 10 1 7 3 9
# 4 5 6 10 8 1 2 3 9 7