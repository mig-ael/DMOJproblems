# Arranging Books

start=list(input())
books=start[:]
L=0
M=0
for char in books:
    if char=='L':
        L+=1
    if char=='M':
        M+=1
def large():
    for j in range(len(books)):
        for i in range(len(books)):
            if books[i]=='L' and i>0:
                books.pop(i)
                books.insert(i-1,"L")


def med():
    for j in range(len(books)):
        for i in range(len(books)):
            if books[i]=='M' and i>0:
                books.pop(i)
                books.insert(i-1,"M")


def check():
    tempL=0
    tempM=0
    if books[:]!=start[:]:
        tempL=1
        tempM=1
        for i in range(len(books)):
            if books[i]!='L' and start[i]!='L' and (books[i]!='M' and start[i]!='M'):
                tempL+=1
            if books[i]!='M' and start[i]!='M' and (books[i]!='L' and start[i]!='L'):
                tempM+=1
    return tempL+tempM

if L>0 and M>0:
    med()
    large()
    
    print(check())

elif L>0 and M==0:
    large()
    print(check())

elif L==0 and M>0:
    med()
    print(check())

else:
    print(0)
