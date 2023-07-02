# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program
input_string = input('Please enter comma seperated numbers: ')
is_tolist = input_string.split(sep=',')
result = [str(int(x)**2) for x in is_tolist if int(x) % 2 != 0]
print(",".join(result))
