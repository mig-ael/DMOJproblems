# https://dmoj.ca/problem/aac2p0

n = int(input())

if n%2 ==0:
    x=n-2
else:
    x=n-1

a = (n+x)//2
print(a)