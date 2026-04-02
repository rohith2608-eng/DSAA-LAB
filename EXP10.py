INF = 99999

def floydWarshall(graph, n):
    dist = graph

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],
                                  dist[i][k] + dist[k][j])

    print(dist)
    return dist


graph = [
    [0, 5, INF, INF],
    [50, 0, 15, 5],
    [30, INF, 0, 15],
    [15, INF, 5, 0]
]

floydWarshall(graph, 4)
