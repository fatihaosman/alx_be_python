
  
def perform_operation(num1, num2, operation):
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
      if num2 == 0:
          return "Error: Division by zero"
        # do division
      else: 
           return num1 / num2
    else:
        # invalid input
        return "Invalid operation"
      
    
