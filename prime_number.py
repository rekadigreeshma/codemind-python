n = int(input())
a = 0
for i in range(1,((n//2)+1)):
    if n%i==0:
        a+=1
if a==1:
    print("prime")
else:
    print("not a prime")