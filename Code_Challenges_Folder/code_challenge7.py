def Code_Challenge7():
	#age discount system

	wc= input("Good Morning Customer! Welcome to Morning Grocery store where it's always good and it's always cheap \b.")
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
Code_Challenge7()
