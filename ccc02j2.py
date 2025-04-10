# AmeriCanadian

vowels=["a","e","i","o","u","y"]

word=input()
while word!='quit!':
    if len(word)>4 and word[len(word)-1-2]!=vowels and word[len(word)-1]=='r' and word[len(word)-2]=='o':
        for i in range(len(word)-1):
            print(word[i],end='')
        print("ur")
    else:
        print(word)
    word=input()
    
    