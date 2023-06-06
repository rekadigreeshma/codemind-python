def first_odd(n,arr):
    for i in range(n):
        if arr[i] %2 ==1:
            return i
n = int(input())
arr = list(map(int,input().split()))
print(sum(arr[:first_odd(n,arr)]))