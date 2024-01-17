"""
Write a program that takes two strings from the user: first_name, last_name. Pass these variables to
fullname function that should return the (full name).

    o For example:
    ▪ First_name = “your first name”, last_name = “your last name”
    ▪ Full_name = “your full name”

Write function named “string_alternative” that returns every other char in the full_name string.
Str = “Good evening”
Output: Go vnn
Note: You need to create a function named “string_alternative” for this program and call it from
main function.
"""


def full_name(first_name, last_name):
    return "Your fullname is: {} {}".format(first_name, last_name)


def problem_1_a():
    # Take first and last name as input from the user
    first_name = input("Please enter first name: ")
    last_name = input("Please enter last name: ")
    # Call the method that combines first and last name
    output = full_name(first_name, last_name)
    # Print the output
    print(output)


# call method
problem_1_a()


def string_alternative(fullname):
    # Variable to store the output
    output = ""
    # Loop every char in the string
    for i in range(len(fullname)):
        # Skip alternate characters (skip the odd places)
        if i % 2 == 0:
            output = output + fullname[i]
    return output


def problem_1_b():
    fullname = input("Please enter fullname: ")
    output = string_alternative(fullname)
    print('string_alternative: {}'.format(output))


# call method
problem_1_b()
