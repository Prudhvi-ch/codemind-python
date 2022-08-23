num =int(input())
n1, n2 =-1,1
for i in range(0,num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")