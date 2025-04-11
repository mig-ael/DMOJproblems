# AmeriCanadian

vowels=["a","e","i","o","u","y"]
word=input()
words=[]
def can(word):
    if len(word)>4 and word[len(word)-1]=='r' and word[len(word)-2]=='o' and word[len(word)-2-1] not in vowels:
        for i in range(len(word)-1):
            print(word[i],end='')
        print("ur")
    else:
        print(word)    

while word!='quit!':
    words.append(word)
    word=input()

for word in words:
    can(word)
