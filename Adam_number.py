a=int(input())
b=a*a
rev=0
while a>0:
    c=a%10
    rev=rev*10+c
    a//=10
d=rev**2
f=0
while d>0:
    e=d%10
    f=f*10+e
    d//=10
if b==f:
    print('True')
else:
    print('False')