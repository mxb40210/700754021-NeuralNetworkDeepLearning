"""
3. Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the
grading scheme we are using in this class.
"""


def problem_3():
    """
    Takes class score and input and determines the grade based on the grading scale below.

    Grading Scale
    Percent (%) Grade
    90 - 100    A
    80 - 89     B
    70 - 79     C
    60 - 69     D
    0 - 60      F
    """
    # Read the class score as input
    try:
        class_score = int(input("Please enter class score (0 to 100): "))
    except Exception as e:
        print('Please enter valid class score. Exception: {}', e)
        return

    if 90 <= class_score <= 100:
        print("Class Score: {}, Grade: {}".format(class_score, 'A'))
    elif 80 <= class_score <= 89:
        print("Class Score: {}, Grade: {}".format(class_score, 'B'))
    elif 70 <= class_score <= 79:
        print("Class Score: {}, Grade: {}".format(class_score, 'C'))
    elif 60 <= class_score <= 69:
        print("Class Score: {}, Grade: {}".format(class_score, 'D'))
    elif 0 <= class_score <= 59:
        print("Class Score: {}, Grade: {}".format(class_score, 'F'))
    else:
        print("Invalid class score: {}. Please enter valid input.".format(class_score))


# Call the method
problem_3()
