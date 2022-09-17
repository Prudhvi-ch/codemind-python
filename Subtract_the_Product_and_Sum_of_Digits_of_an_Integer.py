a=int(input())
b=1
c=0
while a>0:
    d=a%10
    b*=d
    c+=d
    a//=10
    e=b-c
print(e)