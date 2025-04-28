# Magical Magnetic Marbles

n,k=map(int,input().split())
marbles=list(map(int,input()))
count=0

def organize():
    i=0
    while i<len(marbles)-1:
        if (marbles[i]==1 and marbles[i+1]==1):
            marbles.pop(i)
            marbles.insert(i,0)
        else:
            i+=1
organize()
i=0
while i<len(marbles) and k>0:
    if marbles[i]==1 and marbles[i-1]==0 and i>0:
        marbles[i-1]=1
        k-=1
        organize()
    elif marbles[i]==1 and marbles[i+1]==0 and i+1 <len(marbles):
        marbles[i]=1
        k-=1
        organize()
    i+=1



print(marbles.count(1))