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