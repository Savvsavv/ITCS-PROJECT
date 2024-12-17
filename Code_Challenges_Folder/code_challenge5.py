def Code_Challenge5():
    print ("FAHRENHEIT TO CELSIUS CONVERTER PROGRAM")
    print("-------------------------------------------")
    fahrenheit = eval(input("Enter temperature in farenheit --> "))

    celsius = ((fahrenheit -32) *5)/9
    
    print("\n" ,fahrenheit, "degrees Fahrenheit converted to celsius is" , celsius, "degrees")

    print (f"\n {fahrenheit} degress Farenheit converted to celsius is {round(celsius, 2)} degrees")

    print("---------------------------------------------")
Code_Challenge5()
