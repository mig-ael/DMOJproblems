# CCC '03 J1 - Trident

t = int(input())
s=int(input())
h=int(input())
space=' '
for i in range (t):
    print(f"*{space*s}*{space*s}*")
print("*"*(3+s*2))
for i in range(h):
    print(f"{space*(1+s)}*")