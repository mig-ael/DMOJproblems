# Flipper

flips=input()
grid=[1,2,3,4]
for flip in flips:
    if flip=='H':
        grid[0],grid[2]=grid[2],grid[0]
        grid[1],grid[3]=grid[3],grid[1]
    else:
        grid[0],grid[1]=grid[1],grid[0]
        grid[2],grid[3]=grid[3],grid[2]

for i in range(len(grid)):
    if i%2==0:
        print(grid[i],end=' ')
    else:
        print(grid[i])