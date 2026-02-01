import math
radius=int(input("Enter the radius of the circle: "))
print(f'Radius of the circle: {(math.pi*radius*radius):.2f}')
triangle=input("Enter base and height: ")
base,height=map(float,triangle.split(","))
print(f'Aria of triangle:{base*height*0.5}')
