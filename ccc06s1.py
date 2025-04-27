# Canadian Calorie Counting

a=[[461,431,420,0],[100,57,70,0],[130,160,118,0],[167,266,75,0]]
total=0
for i in range(4):
    num=int(input())
    type=a[i]
    total+=type[num-1]

print(f'Your total Calorie count is {total}.')