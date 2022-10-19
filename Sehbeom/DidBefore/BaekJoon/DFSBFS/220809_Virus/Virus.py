# 22.08.09
# 백준 / 2606번 바이러스

from collections import deque


def DFS(graph, v, visited, answer):
    answer[0] += 1
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited, answer)


def BFS(graph, start, visited, answer):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        answer[0] += 1

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N = int(input())
M = int(input())

graph = {x: set() for x in range(1, N+1)}

for i in range(M):
    a, b = map(int, input().split(" "))
    graph[a].add(b)
    graph[b].add(a)

for g in graph:
    graph[g] = list(graph[g])
    graph[g].sort()

answer = [0]
# DFS(graph, 1, [False]*(N+1), answer)
BFS(graph, 1, [False]*(N+1), answer)
print(answer[0]-1)
