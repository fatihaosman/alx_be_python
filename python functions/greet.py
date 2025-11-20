def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
print(greet("Bob"))

def rectangle(length, width):
    area = length * width
    return f"The area of the rectangle is: {area}"
print(rectangle(5, 3))  

def number_check(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"
input_number = int(input("Enter a number: "))      
print(number_check(4))
print(number_check(7))
print(number_check(input_number))
