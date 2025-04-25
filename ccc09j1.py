# ISBN

num1=int(input())
num2=int(input())
num3=int(input())
sum=0
a=[9,7,8,0,9,2,1,4,1,8]
a.extend([num1,num2,num3])

coef=1
for i in range(len(a)):
    coef=1 if i%2==0 else 3
    
    sum+=(a[i]*coef)

print("The 1-3-sum is "+str(sum))
