n = int(input())

a = []
for i in range(n):
    a.append([int(x) for x in input().split()])

m = len(a[0])

si, sj, ti, tj = map(int, input().split())

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

vis = [[False for j in range(m)] for i in range(n)]

def dfs(i, j):
    vis[i][j] = True
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if (ni >= 0) and (ni < n) and (nj >= 0) and (nj < m) and (not vis[ni][nj]) and (a[i][j] != a[ni][nj]):
            dfs(ni, nj)

dfs(si, sj)

print('caminho encontrado' if vis[ti][tj] else 'caminho nao encontrado')
