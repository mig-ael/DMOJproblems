# Arranging Books

books=list(input())
L=0
M=0
for char in books:
    if char=='L':
        L+=1
    if char=='M':
        M+=1
def large():
    countL=0
    for j in range(len(books)):
        for i in range(len(books)):
            if books[i]=='L' and i>0:
                books.pop(i)
                books.insert(i-1,"L")
                countL+=1


    return countL//i

def med():
    countM=0
    for j in range(len(books)):
        for i in range(len(books)):
            if books[i]=='M' and i>0:
                books.pop(i)
                books.insert(i-1,"M")
                countM+=1


    return countM//i


if L>0 and M>0:
    print(med()+large())

elif L>0 and M==0:
    print(large())

elif L==0 and M>0:
    print(med())
