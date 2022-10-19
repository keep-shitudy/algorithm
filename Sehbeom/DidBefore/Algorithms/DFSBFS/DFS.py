graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def DFS(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

def DFS_Stack(graph, start, visited):
    stack = [start]
    temp = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                temp.append(i)

        temp.reverse()
        stack.extend(temp)
        temp.clear()


DFS(graph, 1, [False]*len(graph))
print("\n")
DFS_Stack(graph, 1, [False]*len(graph))