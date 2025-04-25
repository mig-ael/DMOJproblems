# Slot Machines

total =int(input())

slot1=int(input())
slot2=int(input())
slot3=int(input())

maxslot1=35
maxslot2=100
maxslot3=10

count=0
while total!=0:
    #slot1
    total-=1
    slot1+=1
    count+=1
    if maxslot1-slot1==0:
        total+=30
        slot1=0
    #slot2
    total-=1
    slot2+=1
    count+=1
    if maxslot2-slot2==0:
        total+=60
        slot2=0
    
    #slot3
    total-=1
    slot3+=1
    count+=1 
    if maxslot3-slot3==0:
        total+=9
        slot3=0
       
print(f"Martha plays {count} times before going broke.")

