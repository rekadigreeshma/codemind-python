n = int(input())
arr = list(map(int,input().split()))
res,ele,reps = [],0,1
for i in range(n//2):
    res +=[arr[ele]]*arr[reps]
    ele,reps = ele+2,reps+2
print(*res)