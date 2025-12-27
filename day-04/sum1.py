def sum_of_pos_num(numbers):
    sum=0
    for i in numbers:
        if i>=0:
            sum+=i
    print(sum)

numbers=[12,3,454,6,767,90,-2,-1]
sum_of_pos_num(numbers)