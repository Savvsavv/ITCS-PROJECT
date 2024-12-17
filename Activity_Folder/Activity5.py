def Activity5():
    
    temp=int(input("Enter temperature in Farenheit: "))

    cel = (temp-32)*5/9
    rounds =(round(cel,2))

    print(f"The conversion of {temp} degrees farenheit is {rounds} degrees celcius")

