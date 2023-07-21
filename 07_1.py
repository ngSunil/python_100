print(ord('A'), ord('Z'))
numbers = [str(x) for x in range(0, 9)]
lowercase = [chr(x) for x in range(97, 122)]
uppercase = [chr(x) for x in range(65, 90)]
while True:
    password = input('Please enter your password: ')
    num_present, lower_present, upper_present, numflag = 0, 0, 0, 0
    for x in password:
        if x in numbers:
            num_present = 1
        if x in lowercase:
            lower_present = 1
        if x in uppercase:
            upper_present = 1
    if (num_present == 1 and lower_present == 1 and upper_present == 1):
        print('Yay! the password is perfect')
    else:
        x = input('Do you want to retry? ')
        if x == 'n':
            break
        elif x == 'y':
            continue
        else:
            print('Please enter a correct choice!')
            continue
