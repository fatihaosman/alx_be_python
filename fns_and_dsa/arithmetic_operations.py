
  
def perform_operation(num1,num2,operation):
    if operation == "add":
        # do addition
        return num1 + num2
    elif operation == "subtract":
        # do subtraction
        return num1 - num2
    elif operation == "multiply":
        # do multiplication
        return num1 * num2
    elif operation == "divide":
        # do division
        return num1 / num2
    else:
        # invalid input
        return "Invalid operation"
      
    
