first = float(input("Enter first number "))
signh = input("Which operatin you want to do with the numbers \n+ \n- \n* \n/ \n")
second = float(input("Enter second number "))
def calculator(first,signh,second):
    if signh == "+":
        return first+second
    elif signh == "-":
        return first - second
    elif signh == "*":
        return first * second
    else:
        return "You have entered wrong operatin"
print(f"the result of {first} {signh} {second} is : {calculator(first,signh,second)}")

result = calculator(first,signh,second)

calculation = True
ask = input("'Yes' to perform another calculation \n'No' to exit the program \n ")
if ask == "No":
    calculation = False
    
while calculation:       
    new = float(input("Enter new number: "))
    new_signh = input("Which operatin you want to do with the numbers \n+ \n- \n* \n/ \n")
    new_result = calculator(result,new_signh,new)
    print(f"the result of {result} {new_signh} {new} is : {new_result}")
    result = new_result
    ask = input("'Yes' to perform another calculation \n'No' to exit the program \n")
    if ask == "No":
        calculation = False

    
    


