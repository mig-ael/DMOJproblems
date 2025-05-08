# Anagram Checker

# s1=sorted(input().replace(' ',''))
# s2=sorted(input().replace(' ',''))
# count=0

# for i in range(len(s1)):
#     if s1[i]==s2[i]:
#         count+=1

# print("Is an anagram.") if count>=len(s1) and count>=len(s2) else print('Is not an anagram.')


a=[1,2,3]
b=[]

for ele in a:
    b[0]=a.pop(ele)

print(a,b)