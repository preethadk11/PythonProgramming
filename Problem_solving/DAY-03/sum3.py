#when all sides are known [heron's formula]
import math
a,b,c=3,4,7
s=float((a+b+c)/2)
A=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(A)
#answer is 0 because the sum of two side is 3rd side