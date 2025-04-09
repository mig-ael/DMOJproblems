# https://dmoj.ca/problem/ccc00j2

start = int(input())
end= int(input())
a=[0,1,8,69]
ammount=0
for i in range(start,end+1):
    counter=0
    for pos in str(i):
        if pos ==0:
            counter+=1
    if counter>=len(str(i)):
        ammount+=1




print(ammount,counter)