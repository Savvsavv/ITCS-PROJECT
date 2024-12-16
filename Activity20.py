isContinue=True
nt=0
import os
while isContinue ==True:
  ask= input("WOULD YOU LIKE TO ADD ANOTHER TRIANGLE [y/n] -->")
  if ask.lower()=="no":
    print("Program Terminated ")
    break
    isContinue =False
  elif ask.lower()=="yes":
    os.system('cls')
    nt+=1
    for x in range (1,5):
      for y in range (1,nt +1):
        for z in range (1,x+1):
          print("*",end=" )
        for a in range (5,x,-1):
          print (" ", end=" ")
        print (end= " ")
      print()
    continue

  else:  
    print ("TRY AGAIN")
    continue
