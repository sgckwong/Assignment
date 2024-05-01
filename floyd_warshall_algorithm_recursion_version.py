

import sys

def floyd_warshall_recursive(graph, start, end, k):
    if k == 0:
        return graph[start][end]
    
    exclude_k = floyd_warshall_recursive(graph, start, end, k - 1)
    include_k = floyd_warshall_recursive(graph, start, k, k - 1) + floyd_warshall_recursive(graph, k, end, k - 1)
    
    return min(exclude_k, include_k)

def floyd_warshall(graph):
    n = len(graph)
    dist = [[sys.maxsize] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = floyd_warshall_recursive(dist, i, j, k)
    
    return dist


graph = [
    [0, 5, sys.maxsize, 10],
    [sys.maxsize, 0, 3, sys.maxsize],
    [sys.maxsize, sys.maxsize, 0, 1],
    [sys.maxsize, sys.maxsize, sys.maxsize, 0]
]

result = floyd_warshall(graph)
for row in result:
    print(row)

