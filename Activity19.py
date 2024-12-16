def Activity19():
  import os
  tuloy=True
  os.system('cls')

  while tuloy ==True:
    name =input("Please enter a name-->")

    if name.lower() =="stop":
      print("Program Terminated ")
      break 
      tuloy=False
    else:
      continue
      
Activity19()
