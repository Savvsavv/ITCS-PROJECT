def Code_Challenge11():
    #diamond pointed
    #arrow up
    for x in range (1,7):
        for y in range (7, x,-1):
            print (" " , end= " ")
        for z in range (x ,1,-1):
            print ("*", end= " ")
        for a in range ( 1, x+1):
            print ("*", end= " ")
        print ()
    #arrow down
    for x in range (7,0,-1):
        for y in range (7, x, -1):
            print (" " , end= " ")
        for z in range (x, 1, -1):
            print ("*", end= " ")
        for a in range (1,x+1):
            print ("*" , end= " ")
        print ()
Code_Challenge11()
