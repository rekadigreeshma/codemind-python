import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==  0:
            return False
    return True
n = int(input())
arr = list(map(int,input().split()))
k = int(input())
c = len([i for i in arr if i<=k and isPrime(i) == True])
print(c)