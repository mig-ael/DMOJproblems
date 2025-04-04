#https://dmoj.ca/problem/a3

n=int(input())
a=[]
for i in range(n):
    k=int(input())
    i=1
    while ((k+i)**3)%1000!=888:
        i+=1
    a.append(i+k)

for num in a:
    print(num)