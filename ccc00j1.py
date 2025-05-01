# Calendar

start,end = map(int,input().split())
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']

print(' '.join(days))
print(' '*(((start-1)*4)+2), end='')

count = start

for i in range(1, end+1):
    if count == len(days):
        
        if i+start>start:
            print(i,end='\n')
        else:
            print()

        if i > 8:
            print(' ', end='')
        
        else:
            print('  ', end='')
        count=0
    
    elif i > 8:
        print(i, end='  ')

    else:
        print(i, end='   ')
        
    count += 1
