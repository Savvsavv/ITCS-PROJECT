#demo of doc string
def factorial (number):
  """This function's purpose is to compute /calculate the factorial of any number given """
    fact =1
    for x in range (number, 0,-1):
       fact *=x
#print(f"the factorial of 13 is (factorial(13)")

help (factorial)
help(print)
