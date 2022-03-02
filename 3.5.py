word_1 = input('Iinserisci una stringa: ')
print(word_1[0],word_1[-1])

while word_1.isalpha() == False or word_1.islower() == False:
    word_1 = input('Iinserisci una stringa: ')
    print(word_1[0],word_1[-1])



