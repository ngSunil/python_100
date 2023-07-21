# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program
string = input('Please enter the string separated by commas: ')
list_string = string.split(',')
print([int(x)**2 for x in list_string])
