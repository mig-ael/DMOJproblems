# Roll the Dice

m =int(input())
n=int(input())
count=0
for i in range(1,m+1):
    for j in range(1,n+1):
        if i+j==10:
            count+=1
if count==1:
    print(f"There is {count} way to get the sum 10.")
else:
    print(f"There are {count} ways to get the sum 10.")