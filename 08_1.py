sentence = input('Please enter your sentence: ')
removed_duplicates_array = list(set(sentence.split(' ')))
for word in removed_duplicates_array:
    print(f'{word} : {sentence.count(word)}')
