def Code_Challenge6():
	#grades
	prelim = int(input("Enter your Prelim Grade: "))
	midterm = int(input("Enter your Midterm Grade: "))
	sfinals = int(input("Enter your Semi Finals Grade: "))
	finals = int(input("Enter your Finals Grade: "))
	quiz = int(input("Enter your Quiz Grade: "))
	project = int(input("Enter your Project Grade: "))

	if (0 <= prelim <= 100) and (0 <= midterm <= 100) and (0 <= sfinals <= 100) and (0 <= finals <= 100) and (0 <= quiz <= 100) and (0 <= project <= 100):
		fg = (prelim * 0.15) + (midterm * 0.15) + (sfinals * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)

		if fg >= 75:
				print("Congratulations, you passed!")
		else:
				print("Sorry, you failed.")
	else:
		print("Error: All grades must be between 0 and 100.")
Code_Challenge6()
