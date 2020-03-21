import math
l = 109
v = int(input())
t = int(input())
s = v * t
if(s<0):
    print(int(109+(math.fmod(s,l))))
elif s==0:
    print(0)
else:
    print(int(math.fmod(s,l)))



