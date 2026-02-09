n=5
for i in range(1,n+1):
  for s in range(i-1):
      print(" ",end="")
  print("*",end="")
  if i==1:
    for j in range(2*n-2):
      print("*",end="")
  if i>1 and i<5:
    for j in range(2*n-(2*i+1)):
      print(" ",end="")
    print("*",end="")
  print()