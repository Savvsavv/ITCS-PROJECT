
# FINAL PROJECT -
import os

# Password Check 
password = input('Enter your top-secret password (Hint: I like greetings and self-love): ')

if password.lower() == "hello":
    print("\nAccess Granted! 🤝 Friendly as always~")
elif password.lower() == "cuteako":
    print("\nAccess Granted! 🐥 Confidence is key!")
else:
    print("\nAccess Denied! 🚫 Are you trying to sneak in? Nice try.")
    print("\nW E L C O M E!!! ... to the rejection party. Bye.")
    exit()

print("\n\t🌟 Welcome to My First Interactive Program 🌟")
print("Prepare to explore Python like never before. Fun + Fundamentals = FUNdamentals! 🎉")

# Importing activities and challenges
from Activity_Folder import (Activity1, Activity2, Activity3, Activity4, Activity5, Activity6, Activity7, 
                             Activity8, Activity9, Activity10, Activity11, Activity12, Activity13, Activity14, 
                             Activity15, Activity16, Activity17, Activity18, Activity19, Activity20, Activity21, 
                             Activity22, Activity23, Activity24, Activity25)

from Code_Challenges_Folder import (code_challenge1, Code_Challenge2, code_challenge4, code_challenge5, 
                                    code_challenge6, code_challenge7, Code_challengee8, code_challenge9, 
                                    code_challenge10, code_challenge11, code_challenge12, code_challenge13, 
                                    code_challenge14, code_challenge15, code_challenge16)

# Main Menu - 🍵
def M_Menu():
    while True:
        print("""
        **************************************
                  🤖 - Compiled Projects - 🤖
                            MENU
        **************************************

        < 1 > - Code Challenges Project 💻
        < 2 > - Activity Folder 📁
        < 3 > - Python Fundamentals 🐍
        < 0 > - Terminate Program 🛑
        """)
        try:
            number = int(input("\nChoose your adventure (1-3 or 0 to quit): "))
            if number == 1:
                Code_Challenge()
            elif number == 2:
                Activities()
            elif number == 3:
                python_fundamentals()
            elif number == 0:
                print("\n👋 Program Terminated. You shall return.")
                break
            else:
                print("\n[💥 ERROR 💥] That's not a valid choice!")
        except ValueError:
            print("\n[🤯 ERROR 🤯] Numbers only!")

# Code Challenge Menu - Because bugs are challenges too 🐛
def Code_Challenge():
    while True:
        print("""
        **************************************
                 ⚡ - Compiled Projects - ⚡
                        CODE CHALLENGE
        ************************************** 
        \n\t [1] -Code_Challenge#1     \t [2] -Code_Challenge#2    \t [3] -Code_Challenge#3
        \n\t [4] -Code_Challenge#4     \t [5] -Code_Challenge#5    \t [6] -Code_Challenge#6
        \n\t [7] -Code_Challenge#7     \t [8] -Code_Challenge#8    \t [9] -Code_Challenge#9
        \n\t [10] -Code_Challenge#10   \t[11] -Code_Challenge#11   \t[12] -Code_Challenge#12
        \n\t [13] -Code_Challenge#13   \t[14] -Code_Challenge#14   \t[14] -Code_Challenge#15
        \n\t [16] -Code_Challenge#16   \t[0] -Program Terminated """)
        try:
            num = int(input("\nPick a code challenge number (or 0 to escape): "))
            os.system('cls')
            if num == 1:
                code_challenge1.Code_Challenge1()
            elif num == 2:
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
                print("\n⏪ Returning to the Main Menu.")
                break
            else:
                print("\n[🙄 ERROR 🙄] Invalid choice! Stick to the script, please.")
        except ValueError:
            print("\n[🚫 ERROR 🚫] Numbers only! ")

# Activities Menu - Where learning happens 😎
def Activities():
    while True:
        print("""
        **************************************
                 📚 - Compiled Projects - 📚
                         ACTIVITIES
        ************************************** 
        \n\t [1] -Activity#1       \t [2] -Activity#2          \t [3] -Activity#3
        \n\t [4] -Activity#4       \t [5] -Activity#5          \t [6] -Activity#6
        \n\t [7] -Activity#7       \t [8] -Activity#8          \t [9] -Activity#9
        \n\t [10] -Activity#10     \t[11] -Activity#11         \t[12] -Activity#12
        \n\t [13] -Activity#13     \t[14] -Activity#14         \t[14] -Activity#15
        \n\t [16] -Activity#16     \t[17] -Activity#17         \t[18] -Activity#18
        \n\t [19] -Activity#19     \t[20] -Activity#20         \t[21] -Activity#21
        \n\t [22] -Activity#22     \t[23] -Activity#23         \t[24] -Activity#24
        \n\t [25] -Activity#25     \t [0] -Program Terminated""")

        try:
            num = int(input("\nSelect the activity you want to open (0 to exit): "))
            os.system('cls')
            if num == 1:
                Activity1.Activity1()
            elif num == 2:
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
                print("\n⏪ Returning to Main Menu. ")
                break
            else:
                print("\n[🙃 ERROR 🙃] That wasn't a valid option!")
        except ValueError:
            print("\n[🧮 ERROR 🧮] Input a number. It's not that hard!")

def python_fundamentals():
    while True:
        print("""
        **************************************
                    🤖 WELCOME TO 🤖
              ~~~ PYTHON FUNDAMENTALS ~~~
        **************************************
         
        Choose your destiny... I mean topic:
        \t [A] Print Statements   \t [E] Functions          
        \t [B] Variables          \t [F] Conditionals         
        \t [C] Operators          \t [G] Loops
        \t [D] Lists              \t [H] Exit (Escape Room)
        """)
        
        pick = input("👉 Enter your choice (A-H): ").upper().strip()

        if pick == "A":
            statements()
        elif pick == "B":
            variables()
        elif pick == "C":
            operators()
        elif pick == "D":
            lists()
        elif pick == "E":
            functions()
        elif pick == "F":
            conditionals()
        elif pick == "G":
            loops()
        elif pick == "H":
                print("\n💔 Sad to see you go. Remember, Python is love! 🐍")
                break
        else:
            print("\n❌ Invalid input! Please choose a valid letter (A-H).")

# Function 
def statements():
    while True:
        print("\n🖨️ PRINT STATEMENTS:")
        print("You can use 'print()' to display things on the screen.\n")
        choice = input("👉 Do you want a (DESCRIPTION/EXAMPLE) or 'STOP' to go back? ").upper()
        
        if choice == "DESCRIPTION":
            print("\n'print()' displays text, numbers, or results on the screen. Simple, yet powerful!\n")
        elif choice == "EXAMPLE":
            print("\nExample:")
            print("print('Hello, World!')  --> Hello, World!")
            print("print(42)  --> 42\n")
        elif choice == "STOP":
            print("\nGoing back to the main menu... 🏃‍♂️")
            break
        else:
            print("\n❌ Invalid input! DESCRIPTION, EXAMPLE, or STOP only.")

# Function to explain Variables
def variables():
    while True:
        print("\n📦 VARIABLES:")
        choice = input("👉 Do you want a (DESCRIPTION/EXAMPLE) or 'STOP' to go back? ").upper()
        
        if choice == "DESCRIPTION":
            print("\nVariables are containers for storing data, like numbers, text, or even lists!")
        elif choice == "EXAMPLE":
            print("\nExample:")
            print("x = 10")
            print("name = Jerome'")
            print("print(x, name)  --> 10 Jerome\n")
        elif choice == "STOP":
            print("\nBack to safety... Main menu it is! 🏃‍♀️")
            break
        else:
            print("\n❌ Invalid choice! DESCRIPTION, EXAMPLE, or STOP only.")

# Function to explain Operators
def operators():
    while True:
        print("\n➗ OPERATORS (Math Ninjas 🥷):")
        choice = input("👉 DESCRIPTION/EXAMPLE or 'STOP': ").upper()
        
        if choice == "DESCRIPTION":
            print("\nOperators are symbols that perform actions: math (+, -, *), comparisons (> <), and more!")
        elif choice == "EXAMPLE":
            print("\nExamples:")
            print("Addition: 2 + 3  --> 5")
            print("Comparison: 5 > 3  --> True")
            print("Modulus (remainder): 10 % 3  --> 1\n")
        elif choice == "STOP":
            print("\nEnough math for today. Heading back... 🏠")
            break
        else:
            print("\n❌ Enter DESCRIPTION, EXAMPLE, or STOP!")

# Function to explain Lists
def lists():
    while True:
        print("\n📋 LISTS (The Python backpack 🎒):")
        choice = input("👉 DESCRIPTION/EXAMPLE or 'STOP': ").upper()
        
        if choice == "DESCRIPTION":
            print("\nA list is like a backpack where you can store multiple items (values) in order.")
        elif choice == "EXAMPLE":
            print("\nExample:")
            print("my_list = [1, 2, 3, 'Python']")
            print("print(my_list[0])  --> 1")
            print("print(my_list[-1])  --> Python\n")
        elif choice == "STOP":
            print("\nLeaving the list world... Back to the menu! 🚀")
            break
        else:
            print("\n❌ Invalid choice!")

# Functions for Functions, Conditionals, Loops
def functions():
    while True:
        print("\n🛠️ FUNCTIONS :")
        choice = input("👉 DESCRIPTION/EXAMPLE or 'STOP': ").upper()
        
        if choice == "DESCRIPTION":
            print("\nFUNCTIONS are like magic spells. You cast them when needed!")
        elif choice == "EXAMPLE":
            print("\nExample:")
            print("def greet():")
            print("    print('Hello, Wizard!')\ngreet() --> Hello, Wizard!")
        elif choice == "STOP":
            print("\nLeaving function... Back to the menu! 🚀")
            break
        else:
            print("\n❌ Invalid choice!")

def conditionals():
    while True:
        print("\n🧠 CONDITIONALS :")
        choice = input("👉 DESCRIPTION/EXAMPLE or 'STOP': ").upper()
        
        if choice == "DESCRIPTION":
            print("\n CONDITIONALS help you make decisions.")
        elif choice == "EXAMPLE":
            print("Example:")
            print("age = 18")
            print("if age >= 18:")
            print("    print('You are an adult.')\n--> You are an adult.")
        elif choice == "STOP":
            print("\nLeaving conditionals... Back to the menu! 🚀")
            break
        else:
            print("\n❌ Invalid choice!")
            
def loops():
    while True:
        print("\n🔄 LOOPS :")
        choice = input("👉 DESCRIPTION/EXAMPLE or 'STOP': ").upper()
        
        if choice == "DESCRIPTION":
            print("\n LOOPS help you repeat yourself without being annoying.")
        elif choice == "EXAMPLE":
            print("Example:")
            print("for i in range(3):")
            print("    print('Python is fun!')\n--> Python is fun! (3 times)")
        elif choice == "STOP":
            print("\nLeaving Loops.. Back to the menu! 🚀")
            break
        else:
            print("\n❌ Invalid choice!")

# Start the program
M_Menu()
