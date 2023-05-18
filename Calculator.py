import numpy as np;
def add(number1 ,number2):
    return number1 + number2

def sub(number1 ,number2):
    return number1 - number2
def pro(number1 ,number2):
    return number1 * number2
def rem(number1 ,number2):
    return number1 % number2
def quo(number1,number2):
    return number1 / number2
def power(number1,number2):
    return np.float_power(number1,number2)
def sqrut(number):
    return np.sqrt(number)

try:
    print("Basic python calcualtor!")
    operation = input("Enter your operation method: ")
    first_number = float(input("Enter your first number: "))
    second_number = float(input("Enter your second number: "))
    if operation == '+':
        result = add(first_number,second_number)
        print("Answer: ",result)
    elif operation == '-':
        result = sub(first_number,second_number)
        print("Answer: ",result)
    elif operation == '*':
        result = pro(first_number,second_number)
        print("Answer: ", result)
    elif operation == "/":
        result_quo = quo(first_number,second_number)
        result_rem = rem(first_number,second_number)
        print("Answer: ",result_quo," as quotient ",result_rem," as remainder")
    elif operation == "p":
        result = power(first_number,second_number)
        print("Answer: ",result)
    elif operation == "s":
        result = sqrut(first_number)
        result_ = sqrut(second_number)
        print("Square root of ",first_number," is ",result)
        print("Square root of ",second_number," is ",result)
    elif operation == "a":
        print(f"{first_number} +  {second_number} = {add(first_number,second_number)}\n{first_number} - {second_number} = {sub(first_number,second_number)}\n{first_number} * {second_number} = {pro(first_number,second_number)}\n{first_number} / {second_number} = {quo(first_number,second_number)} as quotient and {rem(first_number,second_number)} as reminader\n{first_number} ^ {second_number} is {power(first_number,second_number)}\nSquare root of {first_number} is {sqrut(first_number)}\nSquare root of {second_number} is {sqrut(second_number)}")
    else:
        print("Invalid operation method was provided")
except Exception as e:
    print("Invalid input was given.Error: ",e)
