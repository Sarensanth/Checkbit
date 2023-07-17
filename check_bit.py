def checkbit(a,b):
    for i in range(b):
        a>>=1
    if a&1:
        return 1
    else:
        return 0

a=int(input())
b=int(input())
print(checkbit(a,b))