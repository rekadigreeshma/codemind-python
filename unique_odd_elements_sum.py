n = int(input())
arr = list(map(int,input().split()))
un_odd =  [i for i in arr if i % 2 == 1]
print(sum(set(un_odd)))