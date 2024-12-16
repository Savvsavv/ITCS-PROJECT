def Activity21():
   go=True
   count=0
   while go ==True:
      name =input("Please enter a name:")
      if name.lower() =="stop":
         print("Loop has now stopped")
         print(f"you have entered {count} number of name")
         break
         go==False
      else:
         count+=1
         continue
Activity21()
