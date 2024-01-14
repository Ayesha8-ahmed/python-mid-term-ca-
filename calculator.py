print("****SIMPLE CALCULATOR****")

num1=int(input("Enter first number:\n"))
num2=int(input("Enter second number:\n"))

print("Select operation")
print("press 1 for addition:")
print ("press 2 for subtraction:")
print ("press 2 for multiplication:")
print ("press 2 for division:")

choice=int(input("enter your choice(1-4):"))

if choice == 1:
    print("The addition of given two numbers is :\n ",num1 + num2)
elif choice == 2:
    print("The subtraction of given two numbers is :\n ",num1 - num2)
elif choice == 3:
    print("The multiplication of given two numbers is :\n ",num1 * num2)
elif choice == 4:
    print("The division of given two numbers is :\n",num1 / num2)
else:
    print("Invalid input")

