n=5
for i in range(1,n+1):
  for s in range(n-i):
    print(" ",end="")
  print(1,end="")
  if i>1 and i<n:
     for j in range(2*i - 3):
       print(" ",end="")
     print(1,end="")
  
  if i==n:
    for j in range(2,i+1):
      print(j,end="")
    for j in range(i-1,0,-1):
      print(j,end="")
  print()

  