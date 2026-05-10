#collect first input
#collect second input
#use your operator
#print your answer

integer_one = float(input("Enter first number: "))
integer_two = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = integer_one + integer_two
    print("Answer =", result)

elif operator == "-":
    result = integer_one - integer_two
    print("Answer =", result)

elif operator == "*":
    result = integer_one * integer_two
    print("Answer =", result)

elif operator == "/":
    if integer_two != 0:
        result = integer_one / integer_two
        print("Answer =", result)
    else:
        print("Undefined")

else:
    print("Invalid operator")
