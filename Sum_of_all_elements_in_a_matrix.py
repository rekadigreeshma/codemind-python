r,c = map(int,input().split())
tot = 0
mat = [list(map(int,input().split()))for i in range(r)]
for i in  range(r):
    for j in range(c):
        tot += mat[i][j]
print(tot)