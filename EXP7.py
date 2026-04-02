INF = 999999
N = 5   # Number of vertices in graph

# Creating graph by adjacency matrix method
G = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]

selected = [0, 0, 0, 0, 0]
no_edge = 0
selected[0] = True

print("Edge : Weight")

while (no_edge < N - 1):
    minimum = INF
    a = 0
    b = 0

    for m in range(N):
        if selected[m]:
            for n in range(N):
                if ((not selected[n]) and G[m][n]):
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n

    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected[b] = True
    no_edge += 1
