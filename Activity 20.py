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
