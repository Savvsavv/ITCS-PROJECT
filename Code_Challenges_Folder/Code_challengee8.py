def Code_Challenge8():
	# random numbers and getting the summation of it

	sum =0
	for x in range (1,11):
		num = eval(input(f"Enter #{x} : "))
		sum +=num

	print(f"The sum of all the numbers given is {sum} ")

