def Code_Challenge13():
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
