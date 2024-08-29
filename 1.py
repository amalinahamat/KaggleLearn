# Printing
print("Hello World!")

# Arithmetic
print(1 + 2)    # Addition
print(9 - 5)    # Subtraction
print(9 * 3)    # Multiplication
print(9 / 3)    # Division
print(3 ** 2)   # Exponent

print(((1+3) * (9 - 2) / 2) ** 2)
# PEMDAS RULE
# P -> Parentheses first
# E -> Exponent ( Powers and Square Roots, etc)
# MD -> Multiplication and Division(left to right)
# AS -> Addition and Subtraction(left to right)

# Variables ->  create variable called test
test = 4 + 5
print(test)

# Variable names are ideally short and descriptive. They also need to satisfy several requirements:
# They can't have spaces (e.g., test var is not allowed)
# They can only include letters, numbers, and underscores (e.g., test_var! is not allowed)
# They have to start with a letter or underscore (e.g., 1_var is not allowed)
# Then, to create the variable, you need to use = to assign the value that you want it to have.


# Manipualting variable
my_test = 3
print(my_test)

my_test = 100
print(my_test)

print(test)
print(my_test)

# Increase the value of my_test
my_test = my_test + 3
print(my_test)


# Using multiple variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs) # seconds in 4 years

birth_per_min = 250
birth_per_day = birth_per_min * mins_per_hour * hours_per_day
print(birth_per_day)


import pandas as pd
titanic_data = pd.read_csv("../input/titanic/train.csv")