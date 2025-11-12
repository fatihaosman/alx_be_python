# Python pass Statement

# ython pass statement is used when a statement is required syntactically but you do not want any command or code to execute. It is a null which means nothing happens when it executes. This is also useful in places where piece of code will be added later, but a placeholder is required to ensure the program runs without errors.

# For instance, in a function or class definition where the implementation is yet to be written, pass statement can be used to avoid the SyntaxError. Additionally, it can also serve as a placeholder in control flow statements like for and while loops.


# Using Ellipses (...) as pass Statement Alternative
# Python 3.X allows ellipses (coded as three consecutive dots ...) to be used in place of pass statement. Both serve as placeholders for code that are going to be written later.

# Example
# For example if we create a function which does not do anything especially for code to be filled in later, then we can make use of ...


def func1():
   # Alternative to pass
   ...                   

# Works on same line too
def func2(): ...          
 # Does nothing if called
func1()                  
func2() 