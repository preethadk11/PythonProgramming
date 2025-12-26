numbers=[12,3,44,5,66,49,0]
sum=0
for i in numbers:
    sum+=i
avg=sum/len(numbers)
print(f"sum is: {sum} and average is: {avg:.2f}")