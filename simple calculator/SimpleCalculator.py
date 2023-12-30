#Simple Python Calculator#

#multiple operations
print("Choose an operation: ")
print("a.Addition")
print("b.Subtraction")
print("c.Division")
print("d.Multiplication")

#nested if for each operator
operation = input()
if operation == "a": #addition
    digit1 = input("input first digit: ")
    digit2 = input("input second digit: ")
    print("the result is: " + str(int(digit1) + int(digit2))) #---> converting the int back to str so it concatenates
elif operation == "b": #subtraction
    digit1 = input("input first digit: ")
    digit2 = input("input second digit: ")
    print("the result is: " + str(int(digit1) - int(digit2))) #---> converting the int back to str so it concatenates
elif operation == "c": #division
    digit1 = input("input first digit: ")
    digit2 = input("input second digit: ")
    print("the result is: " + str(int(digit1) % int(digit2))) #---> converting the int back to str so it concatenates
elif operation == "d": #multiplication
   digit1 = input("input first digit: ")
   digit2 = input("input second digit:  ")
   print("the result is: " + str(int(digit1) * int(digit2))) #---> converting the int back to str so it concatenates
else:
    print ("invalid operatior")
