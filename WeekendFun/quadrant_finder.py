integer_x = int(input("Enter your second integer: "))
integer_y = int(input("Enter your second interger: "))

if (integer_x > 0) and (integer_y > 0):
    print("Q1")

elif(integer_x < 0) and (integer_y > 0):
    print("Q2")

elif(integer_x < 0) and (integer_y < 0):
    print("Q3")

elif(integer_x > 0) and (integer_y < 0): 
    print("Q4")

elif(integer_x == 0) and (integer_y == 0 ):
    print("Origin")

elif(integer_y == 0) and (integer_x != 0):
    print("X-axis")

elif(integer_x == 0) and (integer_y !=0):
    print("Y-axis")
