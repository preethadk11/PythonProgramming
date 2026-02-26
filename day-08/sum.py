'''numbers=["apple","orange","banana"]
even=[x[0].upper() for x in numbers ]
print(even)'''
'''n=int(input())
arr=list(map(int, input().split()))
unique_score=list(set(arr))
unique_score.sort()
print(unique_score)'''
this_list=[]
for i in range(int(input())):
    name=input()
    grades=float(input())
    this_list.append([name,grades])
scores=[x[1] for x in this_list]
lowest=min(scores)
scores=[s for s in scores if s!= lowest]
second_lowest=min(scores)
print(second_lowest)
scores=[s for s in scores if s!= second_lowest]
third_lowest=min(scores)
print(third_lowest)
ordered_list=[x[0] for x in this_list if x[1]==second_lowest or x[1]==third_lowest]
ordered_list.sort()
for x in ordered_list:
    print(x)




