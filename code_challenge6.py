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