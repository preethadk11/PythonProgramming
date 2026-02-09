binary=1010
decimal=0
power=0
n=binary
while n>0:
    rem=n%10
    decimal=decimal+rem*(2**power)
    power+=1
    n=n//10
print(decimal)
decimal=10
n=decimal
mid=0
while(n>0):
    rem=n%2
    mid=mid*10+rem
    n=n//2
print(mid)
