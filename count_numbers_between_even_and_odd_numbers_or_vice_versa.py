n = int(input())
arr = list(map(int,input().split()))
out = 0
for i  in range(n-2):
    if arr[i]%2==0 and arr[i+2] %2 == 1 or arr[i]%2 ==1 and arr[i+2]%2 == 0:
        out +=1
print(out)
