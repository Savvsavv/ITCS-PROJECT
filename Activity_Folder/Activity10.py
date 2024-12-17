def Activity10():
  DLL =input("Are you a current student of DLL [yes/no] ")

  if DLL.lower()=="yes":
    print("Welcome to Dalubhasaan ng Lungsod ng Lucena")
    isBSIT=input("Are you currently enrolled in Bachelor of Science in Infomation Technology [yes/no]")
    
    if isBSIT.lower()=="yes":
      print("What a Beautiful Day! Glad to have you in the department of BSIT")
      print("Please fill up the second form")

      isLevel= input("What current year level are right now in DLL? \n F-FRESHMEN \n S-SOPHOMORE \n J-JUNIOR \n SS-SENIOR \n Please input your answer here --> ")
      if isLevel.lower() =="f":
        print("WELCOME ABOARD FRESHMEN!! HOPE YOU ENJOY YOUR STAY")
      elif isLevel.lower() =="s":
        print("WELCOME SOPHOMORE! ARE YOU STILL ENJOYING YOUR STAY? ")
      elif isLevel.lower() =="j":
        print("WELCOME JUNIOR! THERE'S NO TURNING BACK")
      elif isLevel.lower() =="ss":
        print("WELCOME SENIOr ONE LAST YEAR PUSH THROUGH")
    else:
      print("Sorry you are not welcome here")

  else:
    print("Thanks for stopping by ^_^")
    

