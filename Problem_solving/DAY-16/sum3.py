def prime(num):
    if num<0:
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                return False
                break
        else:
            return True
num=int(input())
prime(num)
for i in range(2,(num//2)+1):
    a=i
    b=num-i
    if prime(a) and prime(b):
        print(f'{num}={a}+{b}')