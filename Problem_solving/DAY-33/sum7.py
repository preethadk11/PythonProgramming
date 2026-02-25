'''def number(num):
    if num==0:
        return
    
    number(num-1)
    print(num)
number(5)'''
def number(num):
    if num==0:
        return
    print(num)
    number((num-1))
number(5)