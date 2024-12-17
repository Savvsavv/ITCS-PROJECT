# FINAL PROJECT
import os

# Importing activities and challenges
from Activity_Folder import( Activity1, Activity2, Activity3,Activity4,Activity5,Activity6,Activity7, Activity8, 
                            Activity9, Activity10, Activity11, Activity12, Activity13, Activity14, Activity15,Activity16,
                            Activity17, Activity18, Activity19, Activity20, Activity21, Activity22, Activity23,
                            Activity24, Activity25)
from Code_Challenges_Folder import (code_challenge1, Code_Challenge2, code_challenge4, code_challenge5, 
                                    code_challenge6, code_challenge7, Code_challengee8, code_challenge9, 
                                    code_challenge10, code_challenge11, code_challenge12, code_challenge13,
                                    code_challenge14,code_challenge15,code_challenge16)
# Function to clear the screen
def Clear():
    os.system("cls" if os.name == "nt" else "clear")

# Main Menu
def M_Menu():
    while True:
        print("""
        ******** -Compiled Projects- **********
                       MENU

        < 1 > - Code_Challenges_Project
        < 2 > - Activity_Folder
        < 3 > - Python Fundamentals
        < 0 > - Terminate
        """)
        try:
            number = int(input("Choose what you want to open: "))
            if number == 1:
                Code_Challenge()
            elif number == 2:
                Activities()
            elif number==3:
                pass
            elif number == 0:
                print("\nProgram Terminated.")
                break
            else:
                print("\n[Error: Please choose a valid option.]")
        except ValueError:
            print("\n[Error: Invalid input. Please enter a number.]")

# Code Challenge Menu
def Code_Challenge():
    while True:
        print("\n\t     POJECTS COMPILED "
        "\n\t=========CODE CHALLENGE MENU========"
        
        "\n\t [1] -Code_Challenge#1     \t [2] -Code_Challenge#2    \t [3] -Code_Challenge#3"
        "\n\t [4] -Code_Challenge#4     \t [5] -Code_Challenge#5    \t [6] -Code_Challenge#6"
        "\n\t [7] -Code_Challenge#7     \t [8] -Code_Challenge#8    \t [9] -Code_Challenge#9"
        "\n\t [10] -Code_Challenge#10   \t[11] -Code_Challenge#11   \t[12] -Code_Challenge#12"
        "\n\t [13] -Code_Challenge#13   \t[14] -Code_Challenge#14   \t[14] -Code_Challenge#15"
        "\n\t [16] -Code_Challenge#16   \t[0] -Program Terminated")
        
        try:
            num = int(input("Please choose a number: "))
            os.system('cls')
            if num == 1:
                code_challenge1.Code_Challenge1()
            elif num== 2:
                Code_Challenge2.Code_Challenge2()
            elif num ==3:
                pass
            elif num ==4:
                code_challenge4.Code_Challenge4()
            elif num ==5:
                code_challenge5.Code_Challenge5()
            elif num ==6:
                code_challenge6.Code_Challenge6()
            elif num ==7:
                code_challenge7.Code_Challenge7()
            elif num ==8:
                Code_challengee8.Code_Challenge8()
            elif num ==9:
                code_challenge9.Code_Challenge9()
            elif num ==10:
                code_challenge10.Code_Challenge10()
            elif num == 11:
                code_challenge11.Code_Challenge11()
            elif num ==12:
                code_challenge12.Code_Challenge12()
            elif num == 13:
                code_challenge13.Code_Challenge13()
            elif num ==14:
                code_challenge14.Code_Challenge14()
            elif num ==15:
                code_challenge15.Code_Challenge15()
            elif num ==16:
                code_challenge16.Code_Challenge16()
            elif num == 0:
                print("\nReturning to Main Menu...")
                break
            else:
                print("\n[Error: Please choose a valid option.]")
        except ValueError:
            print("\n[Error: Invalid input. Please enter a number.]")



# Activities Menu
def Activities():
    while True:
        print("\n\t PROJECTS COMPILED "
        "\n\t=========ACTIVITY MENU========"
        
        "\n\t [1] -Activity#1       \t [2] -Activity#2          \t [3] -Activity#3"
        "\n\t [4] -Activity#4       \t [5] -Activity#5          \t [6] -Activity#6"
        "\n\t [7] -Activity#7       \t [8] -Activity#8          \t [9] -Activity#9"
        "\n\t [10] -Activity#10     \t[11] -Activity#11         \t[12] -Activity#12"
        "\n\t [13] -Activity#13     \t[14] -Activity#14         \t[14] -Activity#15"
        "\n\t [16] -Activity#16     \t[17] -Activity#17         \t[18] -Activity#18"
        "\n\t [19] -Activity#19     \t[20] -Activity#20         \t[21] -Activity#21"
        "\n\t [22] -Activity#22     \t[23] -Activity#23         \t[24] -Activity#24"
        "\n\t [25] -Activity#25     \t [0] -Program Terminated")
        
        try:
            num = int(input("Please choose a number: "))
            os.system('cls')
            if num == 1:
                Activity1.Activity1()
            elif num== 2:
                Activity2.Activity2()
            elif num ==3:
                Activity3.Activity3()
            elif num ==4:
                Activity4.Activity4()
            elif num ==5:
                Activity5.Activity5()
            elif num ==6:
                Activity6.Activity6()
            elif num ==7:
                Activity7.Activity7()
            elif num ==8:
                Activity8.Activity8()
            elif num ==9:
                Activity9.Activity9()
            elif num ==10:
                Activity10.Activity10()
            elif num == 11:
                Activity11.Activity11()
            elif num ==12:
                Activity12.Activity12()
            elif num == 13:
                Activity13.Activity13()
            elif num ==14:
                Activity14.Activity14()
            elif num ==15:
                Activity15.Activity15()
            elif num ==16:
                Activity16.Activity16()
            elif num ==17:
                Activity17.Activity17()
            elif num ==18:
                Activity18.Activity18()
            elif num ==19:
                Activity19.Activity19()
            elif num ==20:
                Activity20.Activity20()
            elif num ==21:
                Activity21.Activity21()
            elif num ==22:
                Activity22.Activity22()
            elif num ==23:
                Activity23.Activity23()
            elif num ==24:
                Activity24.Activity24()
            elif num ==25:
                Activity25.Activity25()
            elif num == 0:
                print("\nReturning to Main Menu...")
                break
            else:
                print("\n[Error: Please choose a valid option.]")
        except ValueError:
            print("\n[Error: Invalid input. Please enter a number.]")

def Python_Fundamentals():
    while True:
        try:
            print()
# Start the program
if __name__ == "__main__":
    M_Menu()
