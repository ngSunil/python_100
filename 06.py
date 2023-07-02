# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12


print(ord('0'), ord('9'))
# print('a' < 'F')
lower_case = [chr(x) for x in range(97, 123)]
upper_case = [chr(x) for x in range(65, 90)]
numbers = [chr(x) for x in range(48, 57)]


def haslower(pwd):
    for x in pwd:
        if x in lower_case:
            return True
    print('A Lowercase letter is required')
    return False


def hasUpper(pwd):
    for x in pwd:
        if x in lower_case:
            return True
    print('A Uppercase letter is required')

    return False


def hasNumber(pwd):
    for x in pwd:
        if x in numbers:
            return True
    print('A Number is required')

    return False


def hasSpecial(pwd):
    for x in pwd:
        if x in ['$', '#', '@']:
            return True
    print('A special letter is required')

    return False


while True:
    password = input('Please enter your password to validate>>>>>>')
    if len(password) >= 6 and len(password) <= 12:
        if haslower(password) and hasUpper(password) and hasNumber(password) and hasSpecial(password):
            print('Password is accepted')
            break
        else:
            print('Password has missing requried characters')
    else:
        print('Please enter password length between 6 and 12 characeters')
