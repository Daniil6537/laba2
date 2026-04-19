M = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
]


start, end = 5, 7
n = len(M)
dist = [10**9]*n
prev = [-1]*n
used = [0]*n
dist[start-1] = 0


for _ in range(n):
    u = -1
    for i in range(n):
        if not used[i] and (u == -1 or dist[i] < dist[u]):
            u = i


    used[u] = 1


    for v in range(n):
        if M[u][v] != 0:
            w = abs(M[u][v])  # ← ВОТ ГЛАВНОЕ
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u


path = []
v = end - 1
while v != -1:
    path.append(v + 1)
    v = prev[v]


print("Расстояние:", dist[end-1])
print("Путь:", path[::-1])