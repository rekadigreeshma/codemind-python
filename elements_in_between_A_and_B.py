n = int(input())
arr = list(map(int,input().split()))
a,b = map(int,input().split())
ele = [i for i in arr if a<= i <= b]
print(*ele) if ele else print(-1)