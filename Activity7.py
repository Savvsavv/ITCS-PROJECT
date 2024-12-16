def Activity7(): #ACTIVITY 7 CODE
    #conditional statements
    gold=0
    miner=input("Hola! Please enter your name here --> ")

    #answerable by yes or no

    isminer= input("Did you mine gold today???")
                
    #introduction to decision structure and relational operators

    if isminer.lower() =="yes":
        gold+=1
        print(f"Hi {miner}, today you have a total of {gold} gold")
    else:
        print(f"Hi {miner}, today you have a total of {gold} gold")
Activity7()
