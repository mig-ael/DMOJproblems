# Fraction Action

numerator=int(input())
denominator=int(input())
whole=0
while denominator<=numerator:
    numerator-=denominator
    whole+=1

for i in range(denominator,0,-1):
    if (float(numerator//i)==numerator/i) and float(denominator//i)==denominator/i:
        numerator=numerator//i
        denominator=denominator//i

if numerator!=0 and whole!=0:
    print(f'{whole} {numerator}/{denominator}')

elif whole==0 and numerator>0:
    print(f'{numerator}/{denominator}')

else:
    print(whole)