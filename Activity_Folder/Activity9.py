def Activity9():
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
Activity9()
