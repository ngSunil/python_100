# Write a program that accepts a sequence of whitespace separated words as
# input and prints the words after removing all duplicate words and sorting them alphanumerically.
x = input('enter your sentence')
sorted_list = sorted(list(set(x.split(' '))))
# sentence = ''
# for word in sorted_list:
#     sentence += ' ' + word
# print(sentence)
print(' '.join(sorted_list))

print('-'.join(['a', 'b', 'c']))
print('sunil'.split())
print([x for x in 'sunil'])
print([*'sunil'])
