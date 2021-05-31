# Challenge #1 - Print text to screen

print("\nDay 1 - Python Print Function")
print("The function is declared like this:")
print("print( 'what to print')")

# Challenge #2 - Debugging coding issues

print("\nDay 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Challenge #3 - Prompt the user for an input

print("Hello " + input("What is your name?") + "!")

# Challenge #4 - Count how many characters are in the user provided input

print("Your name has " + str(len(input("What is your name?"))) + " characters in it!")

# Challenge #5 - How to switch variables 
a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)