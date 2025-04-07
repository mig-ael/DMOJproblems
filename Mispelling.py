# https://dmoj.ca/problem/a1

n = int(input())
a=[]
for i in range(n):
    misspelled=''
    baseWord=''
    correctWord =input('')

    for j in range(2,len(correctWord)):
        baseWord+=correctWord[j]
    
    for j in range(len(baseWord)):
        if j != int(correctWord[0])-1:
            misspelled+=baseWord[j]
    a.append(misspelled)
    
for i,word in enumerate(a,1):

    print(f"{i} {word}")