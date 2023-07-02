# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
sentence = input('Please enter your sentence? ')
upperNo, lowerNo = 0, 0
for x in sentence:
    if x.isupper():
        upperNo += 1
    elif x.islower():
        lowerNo += 1
print(f'UPPER CASE {upperNo}')
print(f'LOWER CASE {lowerNo}')
