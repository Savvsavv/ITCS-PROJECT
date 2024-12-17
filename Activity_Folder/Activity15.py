def Activity15():
  for x in range (0,11):
    print(x,"\t", end=" ")
    for y in range (0,x):
      print ("*",end=" ")
    print ()
  for x in range (10,0,-1):
    for y in range (0,x):
      print(" * ",end=" ")
    print()

