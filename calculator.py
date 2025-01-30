print("SIMPLE CALCULATOR PYTHON")

result = 0

while True:
     numOne = float(input("Enter first number : "))
     numTwo = float(input("Enter second number : "))

     print("Select an operator : ")
     print("+ Add")
     print("- Subtract")
     print("* Multiply")
     print("/ Divide")
     print("X Exit")

     operator = input("Select an operator : ")  

     if operator == "+":
       result = numOne + numTwo
     elif operator == "-":
       result = numOne - numTwo
     elif operator == "*":
       result = numOne * numTwo
     elif operator == "/":
       result = numOne / numTwo
     elif operator == "X":
       print("Exiting...")
       break
     else:
        print("Operator not found")

     print("Result : ", result)

