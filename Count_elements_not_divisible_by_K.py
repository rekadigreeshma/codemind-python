n,k = map(int,input().split())
arr = list(map(int,input().split()))
ele = len([i for i in arr if i % k!=0])
print(ele)