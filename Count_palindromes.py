n = int(input())
arr = list(map(int,input().split()))
pal = len([i for i in arr if str(i) == str(i)[::-1]])
print(pal)