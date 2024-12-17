
def Activity22():

    def panghello():
        print("\nHello IT1A")
    is_continue = True

    while is_continue:
      print("\nSelect from the following code:")
      print("1 - PANGHELLO")
      print("2 - Exit")
      
      ask = input("Which would you like to run? Select from the options above: ")
      
      if ask == "1":
            panghello()
      elif ask == "2":
            print("Exiting The Program")
            is_continue = False
      else:
            print("Invalid. Please try again.")

