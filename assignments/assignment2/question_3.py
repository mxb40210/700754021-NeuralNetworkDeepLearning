"""
Write a program, which reads heights (inches.) of customers into a list and convert these
heights to centimeters in a separate list using:
1) Nested Interactive loop.
2) List comprehensions

    Example: L1: [150,155, 145, 148]

    Output: [68.03, 70.3, 65.77, 67.13]
"""


def inches_to_cms_converter(height_inches):
    # return height_inches * 2.54
    return height_inches * 0.45


def inches_to_cm_nested_interactive_loop(height_inches_list):
    height_cms_list = []
    for height_inches in height_inches_list:
        height_cms = inches_to_cms_converter(height_inches)
        height_cms_list.append(round(height_cms, 2))
    print('Inches to cms (Nested Interactive loop): {}'.format(height_cms_list))


def inches_to_cm_list_comprehension(height_inches_list):
    height_cms_list = [round(inches_to_cms_converter(height_inches), 2) for height_inches in height_inches_list]
    print('Inches to cms (List comprehension): {}'.format(height_cms_list))


def problem_3():
    # Input array
    height_inches_list = []
    while True:
        input_height = input("Please enter height (inches). Enter ok to exit input.")
        if input_height == "ok":
            print('User entered ok. Exiting input and commencing height conversion')
            break
        height_inches = float(input_height)
        height_inches_list.append(height_inches)

    # Approach 1 : Using Nested Interactive Loop
    inches_to_cm_nested_interactive_loop(height_inches_list)

    # Approach 2 : Using List Comprehension
    inches_to_cm_list_comprehension(height_inches_list)


# Call the method
problem_3()
