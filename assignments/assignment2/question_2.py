"""
Write a python program to find the wordcount in a file (input.txt) for each line and then print the output.
o Finally store the output in output.txt file.
    Example:
    Input: a file includes two lines:
    Python Course
    Deep Learning Course

    Output:
    Python Course
    Deep Learning Course
    Word_Count:
    Python: 1
    Course: 2
    Deep: 1
    Learning: 1
"""


def problem_2():
    # Map storing word and count
    word_counts = {}
    # Read the input file
    with open('input.txt', 'r') as words_file:
        lines = words_file.readlines()

    # For every line
    for line in lines:
        # Split and read every word
        words = line.strip().split()
        for word in words:
            # Store the word and count in a map (dict)
            word_counts[word] = word_counts.get(word, 0) + 1

    # Store the result in output file
    with open('output.txt', 'w') as output_file:
        # Iterate the map and write to the file each word and its count
        for word, count in word_counts.items():
            print('Word: {}. Count: {}'.format(word, count))
            output_file.write("{} \t {}\n".format(word, count))


# Call the method
problem_2()
