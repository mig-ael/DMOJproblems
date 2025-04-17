# Snow Calls

keypad=[["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y","Z"]]
ammount=int(input())
s=''
a=[]
total=[]
for i in range(ammount):
    s=input()

    for char in s:
            if char !='-':
                a.append(str(char))
            for num in keypad:
                for letter in num:
                    if char==letter:
                        a.pop()
                        a.append(keypad.index(num)+2)
    a.insert(3,'-')
    a.insert(7,'-')
    total.append(a)
    a=[]
for i in total:
    for j in range(12):
        
        print(i[j],end='')
    print()