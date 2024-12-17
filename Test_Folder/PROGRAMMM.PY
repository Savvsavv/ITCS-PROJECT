#final project compilation

import os

#==============ACTIVITIES==================================================================
def Activity1():#ACTIVITY 1 CODE
    print("\t\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\t\b"
    "    *   *   * \n\t\t\t\t\t\t\t\t\t\t\b        *   *   *   *   * "
    "\n\t\t\t\t\t\t\t\t\t\t\b    *   *   *   *   *   *   * \n\t\t\t\t\t\t\t\t\t\t\b"
    "        *   *   *   *   * \n\t\t\t\t\t\t\t\t\t\t\t\b    *   *   * \n\t\t\t\t\t\t\t\t\t\t\t*")

def Activity2():#ACTIVITY 2 CODE
    num1= eval (input("\nPlease input a number here --> "))
    num2= eval(input("Please input another number --> "))

    print("\n", num1, "Floor divided to " num1, " = ", num1 // num2)

def Activity3():#ACTIVITY 3 CODE
    fullname = input("Please input your FULLNAME: ")
    age = input ("Please input your AGE: ")
    gender = input("Please input your GENDER: ")
    birthDate = input ("Please input your DATE OF BIRTH: ")
    birthPlace = input ("Please input your BIRTH PLACE: ")

    citizenship = input ("Please input your CITIZENSHIP: ")

    civil_stat = input("Please input your CIVIL STATUS: ")

    height = float (input("Please input your HEIGHT (in meters) : "))
    weight = float (input("Please input your WEIGHT (in kilograms): "))

    religion = input("Please input you RELIGION: ")
    address = input("Please input your address: ")
    zipcode = input("Please input your ZIPCODE: ")

    number = input("Please input your NUMBER: ")
    email = input("Please input your EMAIL: ")

    school = "Dalubhasaan ng Lungsod ng Lucena"
    BSIT = True

    print("\n\t\t")
    print("\t\t\t Hi, my name is " + fullname + " and I'm " , age , " years old, " + gender + 
    ". My birthday is on " + birthDate + ". I was born in " + birthPlace + ". I am a " 
    + citizenship + ". " + civil_stat + " with a height of " ,(height) , " meters and a weight of " , 
    (weight) ," kilograms. I am a " + religion + " and I live in " + address + " with a zipcode of " 
    + zipcode + ". My number is " ,number , " and as for my email it is " + email + 
    ". I am enrolled and currently studying at " + school + " and a BSIT student")

def Activity4(): #ACTIVITY 4 CODE
    num1 = eval(input("Enter a number--> "))

    num2 =eval(input("Enter another number --> "))

    add= num1+num2
    minus = num1 - num2
    times= num1 *num2 
    divide= num1 /num2 

    print("The sum of", num1, "and ", num2, "is " ,add )
    print("The difference of", num1, "and ", num2, "is " ,minus )
    print("The product of", num1, "and ", num2, "is " ,times )
    print("The dqquotient of", num1, "and ", num2, "is " ,divide )


def Activity5(): #ACTIVITY 5 CODE
    temp=int(input("Enter temperature in Farenheit: "))

    cel = (temp-32)*5/9
    round =(round(cel,2))

    print(f"The conversion of {temp} degrees farenheit is {round} degrees celcius")

def Activity6(): #ACTIVITY 6 CODE
    x=5
    print(x)

    x=x+10

    print(x)

    x=x+20
    print(x)

    x=x+30
    print(x)

def Activity7(): #ACTIVITY 7 CODE
    #conditional statements
    gold=0
    miner=input("Hola! Please enter your name here --> ")

    #answerable by yes or no

    isminer= input("Did you mine gold today???)
                
    #introduction to decision structure and relational operators

    if isminer.lower() =="yes":
        gold+=1
        print(f"Hi {miner}, today you have a total of {gold} gold")
    else:
        print(f"Hi {miner}, today you have a total of {gold} gold")
               

def Activity8(): #ACTIVITY 8 CODE
    password= input("Enter you secret pssword: ")

    if password.lower()=="ahele":
        print("Access Granted")
        print("Enjoy using the System ^_^")

    elif password.lower() =="coding":
        print("Access Granted")
        print("Welcome Back, Master")

    elif passwod.lower()=="graduate":
        print("Access Granted")
        print("Hello Once Again")

    else:
        print("Access Denied")
    print("System Exit")

def Activity9(): #ACTIVITY 9 CODE
    age =eval(input("Enter your age here --> "))

    if age >=1 and age <=7:
        print("Your a toddler")
    elif age >=8 and age <=13:
        print("Your a Pre-teen")
    elif age >=14 and age <=18:
        print("Your a Teenager")
    elif age >=19 and age <=31:
        print("Your in Early Adulthood")
    elif age >=32 and age <=45:
        print("Your in Mid Adulthood")
    elif age >=46 and age <=59:
        print("Your in Post Adulthood")
    elif age >= 60 and age <= 130:
        print("You are a Senior")
    elif age >= 131:
        print("Are you a vampire?")
    else:
        print("Invalid age")

def Activity10(): #ACTIVITY 10 CODE
    DLL =input("Are you a current student of DLL [yes/no] ")

    if DLL.lower()=="yes":
    print("Welcome to Dalubhasaan ng Lungsod ng Lucena")
    isBSIT=input("Are you currently enrolled in Bachelor of Science in Infomation Technology [yes/no]")
    
    if isBSIT.lower()=="yes":
        print("What a Beautiful Day! Glad to have you in the department of BSIT")
        print("Please fill up the second form")

        isLevel= input("What current year level are right now in DLL? \n F-FRESHMEN \n S-SOPHOMORE"
        " \n J-JUNIOR \n SS-SENIOR \n Please input your answer here --> ")
        if isLevel.lower() =="f":
        print("WELCOME ABOARD FRESHMEN!! HOPE YOU ENJOY YOUR STAY")
        elif isLevel.lower() =="s":
        print("WELCOME SOPHOMORE! ARE YOU STILL ENJOYING YOUR STAY? ")
        elif isLevel.lower() =="j":
        print("WELCOME JUNIOR! THERE'S NO TURNING BACK")
        elif isLevel.lower() =="ss":
        print("WELCOME SENIO ONE LAST YEAR PUSH THROUGH")
    else:
        print("Sorry you are not welcome here")

    else:
    print("Thanks for stopping by ^_^")
  

def Activity11(): #ACTIVITY 11 CODE
    #print Marvelous 10 times 

    for x in range (1,20):
        print("Marvelous")
        print("HI")
        print("HELLO")

def Activity12(): #ACTIVITY 12 CODE
    for x in range (10,1,-1)
        print(x)

def Activity13(): #ACTIVITY 13 CODE
    factorial = 1

    factor= eval(input(f"Enter a number: "))
    for x in range(factor, 0,-1):
        factor *= x

    print(factor)

def Activity14(): #ACTIVITY 14 CODE
    for x in range(1,15):
        print(x, end= "")
        for y in range (1,15):
            print("*",end="")
        print("\n")

    for x in range (0,10):
        print("@",end="")
        for y in range (0,10):
            print(x,end="")
        print("")
  

def Activity15(): #ACTIVITY 15 CODE
    for x in range (0,11):
        print(x,"\t", end=" ")
        for y in range (0,x):
            print ("*",end=" ")
        print ()
    for x in range (10,0,-1):
        for y in range (0,x):
            print(" * ",end=" ")
        print()

def Activity16(): #ACTIVITY 16 CODE
    for x in range (1,6):
        for y in range(1,x+1):
            print(" ",end=" ")
        for z in range(6,x,-1):
            print("*",end=" ")
        for a in range (6,x,-1):
            print("*", end=" ")
        print()

def Activity17(): #ACTIVITY 17 CODE
    #create a multiplication table

    column =eval(input("Enter number of columns -->" ))
    for x in range (1,11):
        for y in range(1, column+1):
            print(f"{x} x {y} = {x*y}", end ="\t")
        print()

def Activity18(): #ACTIVITY 18 CODE
    #repeated triangle

    nt= eval(input("Enter number of triangle-->"))
    for x in range (1,5):
        for r in range (1,nt+1):
            for y in range (1,x+1):
                print("*",end =" ")
            for z in range (5,x,-1):
                print(" "),end=" ")
        print()

def Activity19(): #ACTIVITY 19 CODE
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

def Activity20(): #ACTIVITY 20 CODE
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
                        print("*", end=" ")
                    for a in range (5,x,-1):
                        print (" ", end=" ")
                    print (end= " ")
                print()
            continue

    else:  
        print ("TRY AGAIN")
        continue

def Activity21(): #ACTIVITY 21 CODE
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

def Activity22(): #ACTIVITY 22 CODE
    import os

    def panghello():
        print("\nHello IT1A")

    iscontinue =True

    while isContinue:
        print("\nSelect from the following code \n1-PANGHELLO")

    ask= input("Which would you like to run?elect from the options above")

    if ask 1 =="1":
        panghello()

def Activity23(): #ACTIVITY 23 CODE
    #demo of doc string
    def factorial (number):
    """This function's purpose is to compute /calculate the factorial of any number given """
        fact =1
        for x in range (number, 0,-1):
        fact *=x
    #print(f"the factorial of 13 is (factorial(13)")

    help (factorial)
    help(print)

def Activity24(): #ACTIVITY 24 CODE
    #modules
    from Activity23 import factorial
    #from other_folder imoort Math_Module

    print(f"thr factorial of 7 is {factorial(7)}")
def Activity25(): #ACTIVITY 25 CODE
    #LIST

    fruit1="apples"
    fruit2="orange"
    fruit3="starapple"
    fruit4="duha"

    fruits= ["apples","orange","starapple","duha"]
    print("fruits")

    #access individuality item
    print(f"my favorite fruit growing up is {fruits[3]}")
    #add more item to the list
    fruits.append("longgan")
    fruits.insert(3,"banana")
    print(fruits)

#================================================CODE CHALLENGE ==================================================
def Code_challenge1():#code challenge 1 code
    print("\t\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\t\b"
    "    *   *   * \n\t\t\t\t\t\t\t\t\t\t\b        *   *   *   *   * "
    "\n\t\t\t\t\t\t\t\t\t\t\b    *   *   *   *   *   *   * \n\t\t\t\t\t\t\t\t\t\t\b"
    "        *   *   *   *   * \n\t\t\t\t\t\t\t\t\t\t\t\b    *   *   * \n\t\t\t\t\t\t\t\t\t\t\t*")

def Code_challenge2():#code challenge 2 code
    name=input("Please input your name here -->")

    print("\t\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\t\b"
    "    *   *   * \n\t\t\t\t\t\t\t\t\t\t\b        *   *   *   *   * \n\t\t\t\t\t\t\t\t\t\t\b 
    "   *   *  Hi "+ name," *   * \n\t\t\t\t\t\t\t\t\t\t\b        *   *   *   *   * 
    "\n\t\t\t\t\t\t\t\t\t\t\t\b    *   *   * \n\t\t\t\t\t\t\t\t\t\t\t*")

def Code_challenge3():#code challenge 3 code
pass

def Code_challenge4():#code challenge 4 code
    print("\n\t|~~~~~~~~~~~~~|\n\t|By: Savannah | \n\t|~~~~~~~~~~~~~|")

    n1 =eval(input ("\n  enter the First Number --> "))
    n2 =eval(input("  enter the Second Number --> "))
    ans1 = n1 + n2
    ans2 = n1 - n2
    ans3 = n1 * n2
    ans4 = n1 / n2
    ans5 = n1 ** n2
    ans6 = n1 // n2
    ans7 = n1 % n2

    print ("\n\t The sum of" ,n1 ,"and" ,n2 , "is " ,ans1 ,"\b.")
    print ("\n\t The difference of" ,n1 , "and" ,n2 , "is " ,ans2 , "\b.")
    print ("\n\t The product of" ,n1 , "and" ,n2 , "is " ,ans3 , "\b.")
    print ("\n\t The quotient of" ,n1 , "and" ,n2 , "is ",ans4 , "\b.")
    print("\n\t",n1 , "exponent by" ,n2 , "is " ,ans5 , "\b.")
    print ("\n\t The remainder of" ,n1 , "and" ,n2 , "is ",ans7 , "\b.")
    print ("\n\t The floor division of" ,n1 , "and" ,n2 , "is ",ans6 , "\b.")

def Code_challenge5():#code challenge 5 code
    print ("FAHRENHEIT TO CELSIUS CONVERTER PROGRAM")
    print("-------------------------------------------")
    fahrenheit = eval(input("Enter temperature in farenheit --> "))

    celsius = ((fahrenheit -32) *5)/9
    
    print("\n" ,fahrenheit, "degrees Fahrenheit converted to celsius is" , celsius, "degrees")

    print (f"\n {fahrenheit} degress Farenheit converted to celsius is {round(celsius, 2)} degrees")

    print("---------------------------------------------")

def Code_challenge6():#code challenge 6 code
    #grades

    prelim =eval(input(" Enter your Prelim Grade : "))
    midterm = eval(input("Enter your Midterm Grade : "))
    sfinals =eval(input("Enter your Semi Finals Grade : "))
    finals =eval(input(" Enter your Finals Grade : "))
    quiz =eval(input(" Enter your Quiz Grade : "))
    project =eval(input(" Enter your Project Grade : "))


    if (prelim >= 65 and prelim <=100) and (midterm >= 65 and midterm <=100) and (sfinals >= 65 and sfinals <=100) and (finals >= 65 and finals <=100) and (quiz >= 65 and quiz <=100) and (project >= 65 and project <=100):
        fg =(prelim *0.15) + (midterm *0.15)  + (sfinals *0.15) + (finals *0.15) + (quiz *0.25) + (project *0.15) 
        if fg >=75:
            print("Congratulations, you passed!")
        else:
            print("Sorry, you failed")

def Code_challenge7():#code challenge 7 code
    #age discount system

    wc= input("Good Mornning Customer! Welcome to Morning Grocery store where it's always good and it's always cheap \b.")
    name= input ("What is your name? ")
    age =int(input( "How old are you? "))
    item_name= input( "What would you like to buy? ")
    item_price= eval(input("Please Enter the price of your item --> "))
    amount =eval(input("Please enter the amount you gave --> "))
    buy= input("Did you buy a grocery (yes/no):  ")

    tax = item_price*0.123
    total =tax+item_price
    discount= total * 0.052
    change = amount -total

    if buy.lower() == "yes":
        print(f"\nHi {name} you purchased a {item_name} with a price of {item_price} Php plus the", round(tax, 2)," Php tax")
        if age >= 60:
            total=total-discount
            change_w_discount = change + discount
            print(f"\nYou have a discount of", round(discount, 2))
            print(f"Your total price item is", round(total, 2))
            print(f"Your change would be",round(change_w_discount, 2))
        else:
            print("\nYou mumst be a senior citizen to have a discount")
            print(f"Your total price item is", round(total, 2))
            print(f"Your change would be", round(change, 2))
        
    else:
        print("Thank you and Have a nice day") 

def Code_challenge8():#code challenge 8 code
    # random numbers and getting the summation of it

    sum =0
    for x in range (1,11):
        num = eval(input(f"Enter #{x} : "))
        sum +=num

    print(f"The sum of all the numbers given is {sum} ")

def Code_challenge9():#code challenge 9 code
    #inverted half pyramid 
    for x in range (10):
        for y in range (2*x):
            print (" " , end= "")
        for space in range (10-x):
            print ("* ", end= "")
        print ()

def Code_challenge10():#code challenge 10 code
    #diamond na hindi pointed
    #arrow up
    for x in range (1,6):
        for y in range (6, x,-1):
            print (" " , end= " ")
        for z in range (1,x+1):
            print ("*", end= " ")
        for a in range ( 1, x+1):
            print ("*", end= " ")
        print ()
    #arrow down
    for x in range (1,6):
        for y in range (1, x+1):
            print (" " , end= " ")
        for z in range (6,x,-1):
            print ("*", end= " ")
        for a in range (6, x,-1):
            print ("*" , end= " ")
        print ()

def Code_challenge11():#code challenge 11 code
    #diamond pointed
    #arrow up
    for x in range (1,7):
        for y in range (7, x,-1):
            print (" " , end= " ")
        for z in range (x ,1,-1):
            print ("*", end= " ")
        for a in range ( 1, x+1):
            print ("*", end= " ")
        print ()
    #arrow down
    for x in range (7,0,-1):
        for y in range (7, x, -1):
            print (" " , end= " ")
        for z in range (x, 1, -1):
            print ("*", end= " ")
        for a in range (1,x+1):
            print ("*" , end= " ")
        print ()
def Code_challenge12():#code challenge 12 code
    #arrow

    #arrow up
    for x in range (1, 11):
        for y in range ( 11, x, -1):
            print (" ", end =" ")
        for z in range (x, 1, -1):
            print ("^", end= " ")
        for a in range ( 1, x+1):
            print ("^", end= " ")
        print ()

    #square down 
    for a in range (1, 11):
        for c in range (1, 8):
            print (" ", end= " ")
        for d in range (1, 8):
            print ("^", end= " ")
        print ()

def Code_challenge13():#code challenge 13 code
    #diamond number
    #arrow up
    for x in range(1,6):
        for y in range (6,x,-1):
            print (" ", end= " ")
        for z in range(x, 1, -1):
            print(z, end=" ")
        for a in range (1, x+1):
            print(a, end=" ")
        print ()

    #arrow down
    for x in range(6,0,-1):
        for y in range (6,x,-1):
            print (" ", end= " ")
        for z in range(x, 1, -1):
            print(z, end=" ")
        for a in range (1, x+1):
            print(a, end=" ")
        print ()

def Code_challenge14():#code challenge 14 code
    # ask user for  number
    total_sum = 0

    # Loop to get numbers from user
    while True:
        number = int(input("Enter a number --> "))
        
        # If the entered number is 0, terminate the loop
        if number == 0:
            print("Loop terminated")
            break
        
        # Add the number to the total sum
        total_sum += number

    # Print total sum
    print(f"The sum of all the numbers given is {total_sum}")

def Code_challenge15():#code challenge 15 code

    #HYBRID LOOP
    import os

    no=0

    tuloy=True
    while tuloy:
        ask= input("Do you wish to create a new triangle(yes or no)-->")
        if ask.lower ()=="no":
            print("program/loop terminated")
            break
        elif ask.lower()== "yes":
            os.system ("cls")
            no+= 1
            for x in range (1, 6):
                for r in range (1, no +1):
                    for y in range (1,x+1):
                        print("^", end=" ")
                    for z in range (6,x,-1):
                        print(" ", end=" ")
                print()
            continue
        else:
            os.system ("cls")
            print("Invalid answer, please only answer 'yes or 'no")
            continue
		
def Code_challenge16():#code challenge 16 code
    # create a function that will breakdown a filipino denomination and then print it
    # Create a python program that can create banking accounts, with the ff. information initial deposit, name 
    #user can deposit, withdraw, and every deposit program should be able to deposit, current balance
    #program will only terminate if user choose to terminate the program

    # Banking System Program
    print ("\n Made by: Savannah Mari De Mesa")

    # Banking System Functions

    def breakdown_denominations(amount):
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        breakdown = {}
        for deno in denominations:
            if amount >= deno:
                breakdown[deno] = amount // deno
                amount %= deno
        return breakdown

    # Function to display denomination breakdown
    def print_breakdown(amount):
        print(f"\nBreakdown of PHP {amount}:")
        breakdown = breakdown_denominations(amount)
        for deno, count in breakdown.items():
            print(f"PHP {deno}: {count} piece")

    accounts = {}

    def create_account():
        name = input("Enter your name: ").strip()

        while True:

            try:
                initial_deposit = float(input("Enter initial deposit: "))
                if initial_deposit < 0:
                    print("Initial deposit cannot be negative. Try again.")
                    continue
                accounts[name] = initial_deposit
                print(f"Account created successfully for {name} with balance PHP {initial_deposit:.2f}!")
                print_breakdown(initial_deposit)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def deposit(name):
        if name in accounts:

            while True:

                try:
                    amount = float(input("Enter amount to deposit: "))
                    if amount < 0:
                        print("Amount cannot be negative. Try again.")
                        continue
                    accounts[name] += amount
                    print(f"Deposited PHP {amount:.2f}. Current balance: PHP {accounts[name]:.2f}")
                    print_breakdown(amount)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
        else:
            print(f"Account with name {name} does not exist.")

    def withdraw(name):
        if name in accounts:

            while True:

                try:
                    amount = float(input("Enter amount to withdraw: "))
                    if amount < 0:
                        print("Amount cannot be negative. Try again.")
                        continue
                    if amount > accounts[name]:
                        print("Insufficient funds. Try a smaller amount.")
                        continue
                    accounts[name] -= amount
                    print(f"Withdrew PHP {amount:.2f}. Current balance: PHP {accounts[name]:.2f}")
                    print_breakdown(amount)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
        else:
            print(f"Account with name {name} does not exist.")

    def view_balance(name):
        if name in accounts:
            print(f"{name}'s Current Balance: PHP {accounts[name]:.2f}")
        else:
            print(f"Account with name {name} does not exist.")

    # Main Program
    while True:
        print("\n--- Banking System ---")
        print("\nPlease Select An Option")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. Exit")
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                create_account()
            elif choice == 2:
                name = input("Enter your name: ")
                deposit(name)
            elif choice == 3:
                name = input("Enter your name: ")
                withdraw(name)
            elif choice == 4:
                name = input("Enter your name: ")
                view_balance(name)
            elif choice == 5:
                print("Thank you for using the Banking System. Goodbye and See You Again!\nProgram Terminated")
                break
            else:
                print("Invalid choice! Please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")

 
def MENU():
    while True:
        print("\n\t =COMPILATION OF PROJECTS="
            "\n\t ==========MAIN MENU============"
            
            "\n\n\t <1> - Activity:
            "n\n\t <2> -Code_Challenge:
            "n\n\t <0> - Exit: ")
        
        no=int(input("\n\n\t Please choose a number you want to open:"))

        if no == 0:
            print("Exited the Program")
            break
        elif no ==1:
            Activities()
        elif no ==2:
            code()

        elif num <0: 
            print("Error.Error.Error")
        else:
            print("Wrong input.Please try again")

def Activities():
    try:
        while True:
            print("\n\t POJECTS COMPILED "
            "\n\t=========ACTIVITY MENU========"
            
            "\n\t [1] -Activity#1  \t [2] -Activity#2  \t [3] -Activity#3"
            "\n\t [4] -Activity#4  \t [5] -Activity#5  \t [6] -Activity#6"
            "\n\t [7] -Activity#7  \t [8] -Activity#8  \t [9] -Activity#9"
            "\n\t [10] -Activity#10\t[11] -Activity#11 \t[12] -Activity#12"
            "\n\t [13] -Activity#13\t[14] -Activity#14 \t[14] -Activity#15"
            "\n]t [16] -Activity#16\t[17] -Activity#17 \t[18] -Activity#18"
            "\n\t [19] -Activity#19\t[20] -Activity#20 \t[21] -Activity#21"
            "\n\t [22] -Activity#22\t[23] -Activity#23 \t[24] -Activity#24"
            "\n\t [25] -Activity#25\t [0] -Program Terminated")

            num= int(input("\n\n\t Pease choose a number : "))
            if num == 1:
                Activity1()
            elif num== 2:
                Activity2()
            elif num ==3:
                Activity3()
            elif num ==4:
                Activity4()
            elif num ==5:
                Activity5()
            elif num ==6:
                Activity6()
            elif num ==7:
                Activity7()
            elif num ==8:
                Activity8()
            elif num ==9:
                Activity9()
            elif num ==10:
                Activity10()
            elif num == 11:
                Activity11()
            elif num ==12:
                Activity12()
            elif num == 13:
                Activity13()
            elif num ==14:
                Activity14()
            elif num ==15:
                Activity15()
            elif num ==16:
                Activity16()
            elif num ==17:
                Activity17()
            elif num ==18:
                Activity18()
            elif num ==19:
                Activity19()
            elif num ==20:
                Activity20()
            elif num ==21:
                Activity21()
            elif num ==22:
                Activity22()
            elif num ==23:
                Activity23()
            elif num ==24:
                Activity24()
            elif num ==25:
                Activity25()
            elif num ==0:
                print("Exit Program")        

def code():
    try:
        while True:
            print("\n\t POJECTS COMPILED "
            "\n\t=========CODE CHALLENGE MENU========"
            
            "\n\t [1] -Code_Challenge#1  \t [2] -Code_Challenge#2  \t [3] -Code_Challenge#3"
            "\n\t [4] -Code_Challenge#4  \t [5] -Code_Challenge#5  \t [6] -Code_Challenge#6"
            "\n\t [7] -Code_Challenge#7  \t [8] -Code_Challenge#8  \t [9] -Code_Challenge#9"
            "\n\t [10] -Code_Challenge#10\t[11] -Code_Challenge#11 \t[12] -Code_Challenge#12"
            "\n\t [13] -Code_Challenge#13\t[14] -Code_Challenge#14 \t[14] -Code_Challenge#15"
            "\n]t [16] -Code_Challenge#16\t[0] -Program Terminated")


            num= int(input("\n\n\t Pease choose a number : "))
            if num == 1:
                Code_challenge1()
            elif num== 2:
                Code_challenge2()
            elif num ==3:
                Code_challenge3()
            elif num ==4:
                Code_challenge4()
            elif num ==5:
                Code_challenge5()
            elif num ==6:
                Code_challenge6()
            elif num ==7:
                Code_challenge7()
            elif num ==8:
                Code_challenge8()
            elif num ==9:
                Code_challenge9()
            elif num ==10:
                Code_challenge10()
            elif num == 11:
                Code_challenge11()
            elif num ==12:
                Code_challenge12()
            elif num == 13:
                Code_challenge13()
            elif num ==14:
                Code_challenge14()
            elif num ==15:
                Code_challenge15()
            elif num ==16:
                Code_challenge16()
            elif num ==0:
                print("Exit Program")        





            











