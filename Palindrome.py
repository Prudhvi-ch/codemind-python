a=int(input())
t=a
rev=0
while a>0:
    b=a%10
    rev=rev*10+b
    a//=10
if rev==t:
    print("True")
else:
    print('False')