n = int(input())
arr = list(map(int,input().split()))
a,b = map(int,input().split())
tot = 0
for i in arr:
    if not(a<=i<=b):
        tot += i
print(tot)