"""
1. Write a python program for the following:

– Input the string “Python” as a list of characters from console,
  delete at least 2 characters, reverse the resultant string and print it.

    Sample input:
        python

    Sample output:
        ntyp

– Take two numbers from user and perform at least 4 arithmetic operations on them.
"""


def problem_1_a():
    # Take user input
    user_input = input("Please enter the string python: ")
    # Covert string to list of characters
    user_input_list = list(user_input)
    # Delete characters
    del user_input_list[3:5]
    # Convert to string
    output_string = ''.join(user_input_list)
    # Reverse the string
    output_string = output_string[::-1]
    # print output
    print(output_string)


def problem_1_b():
    # Take two numbers as input
    x = int(input("Please enter first number: "))
    y = int(input("Please enter second number: "))
    # Perform arithmetic operations - addition, subtraction, multiplication, division
    addition_output = x + y
    subtraction_output = x - y
    multiplication_output = x * y
    if y != 0:
        division_output = x / y
    else:
        division_output = "Invalid"
        print('Division by 0 is invalid. Please enter valid input for second number.')
    # Print result
    print("{} + {} = {}".format(x, y, addition_output))
    print("{} - {} = {}".format(x, y, subtraction_output))
    print("{} * {} = {}".format(x, y, multiplication_output))
    print("{} / {} = {}".format(x, y, division_output))


# Call problem_1_a
problem_1_a()

# Call problem_1_b
problem_1_b()
