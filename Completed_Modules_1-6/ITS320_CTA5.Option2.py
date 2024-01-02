"""
Assignment Instructions
    Write a Python function that will work on three strings.
    The function will return a concatenation of the first two strings and will print the third string in reverse order.
    The function is to be called from the main program.
    In the main program, prompt the user for the three strings and pass these values to the function.
"""


# from typing import Tuple, Any


def concat_two_strings(first_string, second_string):
    return first_string + second_string


def reverse_string(string):
    string = list(string)
    string.reverse()
    return "".join(string)


def concat_two_reverse_1(first_string, second_string, third_string):
    return concat_two_strings(first_string, second_string), reverse_string(third_string)


if __name__ == '__main__':
    print('This program will return a concatenation of two strings and will print a third string in reverse order.')
    print('The function is to be called from the main program.\n')
    first_string: str = input('Enter the first string: ')
    second_string: str = input('Enter the second string: ')
    third_string: str = input('Enter the third string: ')
    #    strings: Tuple[Any, str] = concat_two_reverse_1(first_string, second_string, third_string)
    strings = concat_two_reverse_1(first_string, second_string, third_string)
    i = 0
    for string in strings:
        if i == 0:
            print('The first string + the second string is:', string)
        else:
            print('The third string reversed is:', string)
        i += 1
