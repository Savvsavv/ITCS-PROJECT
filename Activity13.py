def Activity13():
  factorial = 1

  factor= eval(input(f"Enter a number: "))
  for x in range(factor, 0,-1):
    factor *= x

  print(factor)

Activity13()
