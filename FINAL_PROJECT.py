#FINAL PROJECT

import os
from Activity_Folder import( Activity1, Activity2, Activity3,Activity4,Activity5,Activity6,Activity7, Activity8, 
                            Activity9, Activity10, Activity11, Activity12, Activity13, Activity14, Activity15,Activity16,
                            Activity17, Activity18, Activity19, Activity20, Activity21, Activity22, Activity23,
                            Activity24, Activity25)
from Code_Challenges_Folder import (code_challenge1, Code_Challenge2, code_challenge4, code_challenge5, 
                                    code_challenge6, code_challenge7, Code_challengee8, code_challenge9, 
                                    code_challenge10, code_challenge11, code_challenge12, code_challenge13,
                                    code_challenge14,code_challenge15,code_challenge16)
#Main Menu
def Main_Menu():
    while True:
            print(" ~~~~~~~~~~~~ PROJECT COMPILATION ~~~~~~~~~~~~~"
                  "~~~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~~"
                  
                  "<1> - ACTIVITY_FOLDER"
                  "<2> - CODE_CHALLENGES_FOLDER"
                  "<0> - TERMINATE")
            
            try:
                number = int(input("Choose what you want to open:"))
                if number ==1:
                        pass
                elif number ==2:
                        pass
                elif number ==0:
                    print("\n\tPROGRAM TERMINATED. THANK YOU FOR USING THIS PROGRAM FOR A SHORT TIME")
                    break
                else:
                    print("\n\tERROR!!! PLEASE CHOOSSE ONE OPTION ABOVE THAT IS NOT IN THE OPTION.")
            except ValueError:
                  print("\n\t ERROR. ERROR. ERROR. INVALID INPUT")

Activity1.Activity1()