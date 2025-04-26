# A String Problem

s=list(input())
count=0
i=0
while i<(len(s)-2):
    if s[i]!=s[i+1]:
        count+=1
        s.pop(i)
    else:
        i+=1     
print(count)