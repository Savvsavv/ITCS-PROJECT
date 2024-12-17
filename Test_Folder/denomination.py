name= input("Enter your name here --> ")
dep= eval(input("Enter your deposit here --> "))

libo= dep // 1000
sukli_lib= dep % 1000

five= sukli_lib // 500
sukli_five= sukli_lib % 500

two= sukli_five // 200
sukli_two= sukli_five % 200

one= sukli_two // 100
sukli_one= sukli_two % 100

fifty= sukli_one // 50
sukli_fifty= sukli_one % 50

twenty= sukli_fifty // 20
sukli_twenty= sukli_fifty % 20

ten= sukli_twenty // 10
sukli_ten= sukli_twenty % 10

fives= sukli_ten // 5
sukli_fives= sukli_ten % 5

one= sukli_fives // 1
sukli_one= sukli_fives % 1


print ("===============================================")
print ("\n     " +name,"your deposit are the following: ")
print ("\n\t " ,libo, "=1000")
print ("\t " ,five, "=500")
print ("\t " ,two, "=200")
print ("\t " ,one, "=100")
print ("\t " ,fifty, "=50")
print ("\t " ,twenty, "=20")
print ("\t " ,ten, "=10")
print ("\t " ,fives, "=5")
print ("\t " ,one, "=1")
print("\n ==============================================")