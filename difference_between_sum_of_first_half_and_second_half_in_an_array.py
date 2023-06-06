n = int(input())
arr = list(map(int,input().split()))
print(abs(sum(arr[:(n//2)])- sum(arr[(n//2):])))
