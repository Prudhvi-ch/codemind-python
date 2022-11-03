x=int(input())
def rever(nu):
    sign=nu/abs(nu)
    number=abs(nu)
    stra=str(number)
    reverse_num=sign*int(stra[::-1])
    return reverse_num
print(format(rever(x),".0f"))
