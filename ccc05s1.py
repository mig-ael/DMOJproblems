# Snow Calls

keypad=[["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y","Z"]]
exclude=[1,2,3,4,5,6,7,8,9,0]
ammount=int(input())

for i in range(ammount):
    s=input()
    for char in s:
        if (char not in exclude) or char!="-":
            for num in keypad:
                for letter in num:
                    if char==letter:
                        print(keypad.index(num)+2,end='')
        else:
            print(char,end='')