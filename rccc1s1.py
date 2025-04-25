# Word Bot

v= 'aeiouy'
c= 'bcdfghjklmnpqrstvwxyz'
ac=[]
av=[]
s=(input())
n,capc,capv=map(int,s.split())
word=input()
countc=0
countv=0
for i in range(n):
    if word[i] in c:
        countc+=1
    else:
        ac.append(countc)
        countc=0
if countc>0:
    ac.append(countc)
for i in range(n):
    if word[i] in v:
        countv+=1
    else:
        av.append(countv)
        countv=0
if countv>0:
    av.append(countv)
ac.sort()
av.sort()
print("NO") if (ac[-1])>capc or (av[-1])>capv else print("YES")