arr=[1,2,4,5,6]
ser=int(input())
for i in range(len(arr)):
    if arr[i]==ser:
        print(f'Search element {ser} found at index {i} position')
        break
else:
    print("Search element is not found")