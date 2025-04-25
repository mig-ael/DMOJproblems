# It's Cold Here!

s='te mp'
min=float('inf')
a=[]
while s.split()[0]!="Waterloo":
    s=input()
    for i in range(len(s.split())):
        if i%2!=0:
            x=int(s.split()[i])
            if x<min:
                min=x
                a=[]
                a.append(s)
print((a[0].split())[0])

#didnt realize could use city, temp = s.split()