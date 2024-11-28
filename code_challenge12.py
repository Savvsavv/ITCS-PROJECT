#arrow

#arrow up
for x in range (1, 11):
	for y in range ( 11, x, -1):
	    print (" ", end =" ")
	for z in range (x, 1, -1):
	    print ("^", end= " ")
	for a in range ( 1, x+1):
	    print ("^", end= " ")
	print ()

#square down 
for a in range (1, 11):
	for c in range (1, 8):
	       print (" ", end= " ")
	for d in range (1, 8):
	       print ("^", end= " ")
	print ()
