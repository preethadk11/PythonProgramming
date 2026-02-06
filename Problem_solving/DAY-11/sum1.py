numbers=input("Enter three numbers:")
numbers=list(map(int,numbers.split()))
#print(max(numbers))
greatest=numbers[0]
for num in numbers:
    if num>greatest:
        greatest=num
print(greatest)
