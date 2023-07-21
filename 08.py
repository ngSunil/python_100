# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
sentence = input('Please enter your sentence?.. ')
sorted_sentence_list = sorted(set(sentence.split(" ")))
original_sentence = sentence.split(" ")
print([i])
for word in sorted_sentence_list:
    print(f'{word}: {sentence.count(word)}')

float
int
complex