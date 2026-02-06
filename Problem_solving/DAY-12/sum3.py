num=input()
two_numbers=list(map(int,num.split()))
while(two_numbers[1] != 0):
    r=two_numbers[0] % two_numbers[1]
    two_numbers[0]=two_numbers[1]
    two_numbers[1]=r
print(two_numbers[0])
