# https://dmoj.ca/problem/aac1p1

a,b = map(int, input().split())

if a**2>((b**2)*3.14):
    print("SQUARE")
else:
    print("CIRCLE")