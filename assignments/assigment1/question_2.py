"""
2. Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’.

    Sample input:
        I love playing with python

    Sample output:
        I love playing with pythons
"""


def problem_2():
    """
        Takes user input and replaces occurrences of python
        with pythons in the user provided input.
    """
    # declare constants
    word_to_replace = "python"
    word_to_replace_with = "pythons"
    # Read user input
    user_input = input("Please enter your input: ")
    # Replace python with pythons
    output = user_input.replace(word_to_replace, word_to_replace_with)
    # Print the output
    print(output)


# Call the method
problem_2()
