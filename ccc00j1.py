# Calendar

start,end = map(int,input().split())
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']

print(' '.join(days))
print('  ', end='')

count = 0

for i in range(1, end+1):
    if count >= len(days):
        count=0
        
        print()
        
        if i > 9:
            print(' ', end='')
        
        else:
            print('  ', end='')
    
    elif i > 8:
        print(i, end='  ')

    else:
        print(i, end='   ')
        
    count += 1
