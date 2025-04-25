# Ragaman

s1=input()
s2=input()
line1=[]
line2=[]
count=0
removed=[]


for char in s2:
    if char!='*':
        line2.append(char)
    else:
        count+=1

for char in s1:
    if char!='*':
        line1.append(char)

# print(line1,line2,removed)
if len(line1)-count==len(line2):
    if sorted(line1)==sorted(line2):
        print("A")
        
    else:
        print("N")
else:
    print("N")