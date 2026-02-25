def addd(num):
    if num==0:
        return 0
    else:
        return num+addd(num-1)
num=int(input())
print(addd(num))