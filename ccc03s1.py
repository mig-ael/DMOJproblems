# Snakes and ladders

import sys
roll = int(input())
pos=1
while roll!=0:
    if pos<101 and pos+roll<101 and 1<roll and roll<13:
        pos+=roll
    if pos==54:
        pos=19
    elif pos==90:
        pos=48
    elif pos==99:
        pos=77
    elif pos==9:
        pos=34
    elif pos==40:
        pos=64
    elif pos==67:
        pos=86
    print(f"You are now on square {pos}")
    if pos==100:
        print("You win!")
        sys.exit()
    else:
        roll=int(input())

if roll==0:
    print("You Quit!")