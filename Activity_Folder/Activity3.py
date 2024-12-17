def Activity3():
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
    print("\t\t\t Hi, my name is " + fullname +
     " and I'm " , age , " years old, " 
     + gender + ". My birthday is on " + birthDate + 
     ". I was born in " + birthPlace + ". I am a " + citizenship + 
     ". " + civil_stat + " with a height of " ,(height) , " meters and a weight of " ,
      (weight) ," kilograms. I am a " + religion + " and I live in " + address + " with a zipcode of "
       + zipcode + ". My number is " ,number , " and as for my email it is " + email + 
       ". I am enrolled and currently studying at " + school + " and a BSIT student")


