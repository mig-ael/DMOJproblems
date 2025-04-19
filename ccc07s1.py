# Federal Voting Age

amount=int(input())
year=2007
month=2
day=27
def check(y,m,d):
    if m<13 and d<32:
        if year-y>18:
            print("Yes")
        elif year-y>16 and m<=month and d<=day:
            print("Yes")

        elif year>16 and m==2 and d==29:
            print("Yes")
        else:
            print("No")

for i in range(amount):
    date=input()
    check(*map(int,date.split()))
