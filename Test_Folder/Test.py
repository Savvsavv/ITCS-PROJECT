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

        < 1 > - Activity_Project
        < 2 > - Code_Challenges_Project
        < 0 > - Terminate
        """)
        try:
            number = int(input("Choose what you want to open: "))
            if number == 1:
                Activities()
            elif number == 2:
                Code_Challenge()
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
        print("""
        ******** -Compiled Projects- **********
                     CODE CHALLENGES

         [1] - Code_Challenge#1      [2] - Code_Challenge#2
         [3] - Code_Challenge#3      [4] - Code_Challenge#4
         [5] - Code_Challenge#5      [6] - Code_Challenge#6
         [7] - Code_Challenge#7      [8] - Code_Challenge#8
         [9] - Code_Challenge#9      [10] - Code_Challenge#10
         [11] - Code_Challenge#11    [12] - Code_Challenge#12
         [13] - Code_Challenge#13    [14] - Code_Challenge#14
         [15] - Code_Challenge#15    [16] - Code_Challenge#16
         [0] - Return to Main Menu
        """)
        try:
            num = int(input("Please choose a number: "))
            if num == 1:
                code_challenge1()
            elif num == 2:
                Code_Challenge2()
            # Add other elif cases here as needed
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
        print("""
        ******** -Compiled Projects- **********
                     ACTIVITIES

         [1] - Activity#1          [2] - Activity#2
         [3] - Activity#3          [4] - Activity#4
         [5] - Activity#5          [6] - Activity#6
         [7] - Activity#7          [8] - Activity#8
         [9] - Activity#9          [10] - Activity#10
         [11] - Activity#11        [12] - Activity#12
         [13] - Activity#13        [14] - Activity#14
         [15] - Activity#15        [16] - Activity#16
         [17] - Activity#17        [18] - Activity#18
         [19] - Activity#19        [20] - Activity#20
         [21] - Activity#21        [22] - Activity#22
         [23] - Activity#23        [24] - Activity#24
         [25] - Activity#25        [0] - Return to Main Menu
        """)
        try:
            num = int(input("Please choose a number: "))
            if num == 1:
                Activity1()
            elif num == 2:
                Activity2()
            # Add other elif cases here as needed
            elif num == 0:
                print("\nReturning to Main Menu...")
                break
            else:
                print("\n[Error: Please choose a valid option.]")
        except ValueError:
            print("\n[Error: Invalid input. Please enter a number.]")

# Start the program
if __name__ == "__main__":
    M_Menu()
