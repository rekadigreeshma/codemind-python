n = int(input())
arr = list(map(int,input().split()))
c = 0
lst = []
for i in arr:
    if i %2!=0 and i not in lst:
        lst.append(i)
        c +=1
print(c)