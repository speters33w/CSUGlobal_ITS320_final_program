# returns True if string contains alphanumeric [0-9A-Za-z] characters
def contains_alphanumeric(s):
    return any(char.isalnum() for char in s)


# returns True if string contains alphabetic [A-Za-z] characters
def contains_alphabetic(s):
    return any(char.isalpha() for char in s)


# returns True if string contains numeric [0-9] characters
def contains_digit(s):
    return any(char.isdigit() for char in s)


# returns True if string contains lower case [a-z] characters
def contains_lowercase(s):
    return any(char.islower() for char in s)


# returns True if string contains upper case [A-Z] characters
def contains_uppercase(s):
    return any(char.isupper() for char in s)


def main():
    string = input('Enter a string: ')
    if len(string) <= 50:
        print('Input contains AlphaNumeric characters? ' + str(contains_alphanumeric(string)))
        print('Input contains Alphabetical characters? ' + str(contains_alphabetic(string)))
        print('Input contains Digits? ' + str(contains_digit(string)))
        print('Input contains Lowercase characters? ' + str(contains_lowercase(string)))
        print('Input contains Uppercase characters? ' + str(contains_uppercase(string)))
    else:
        print('Input must be less than 50 characters. ')


if __name__ == '__main__':
    main()
