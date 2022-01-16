import math
def dem(n):
    n=n*2
    m=int(math.sqrt(n))
    d=0
    y=0
    for x in range(2,m+1,1):
        if n%x==0:
            y=int(n/x)
            if ((y-x)%2!=0):
                d+=1
    return d
t=int(input())
while t!=0:
    t-=1
    n=int(input())
    print(dem(n))