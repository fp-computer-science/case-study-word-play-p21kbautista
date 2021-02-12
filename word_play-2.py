# Kyle B, Joshua P (AMDG) 2/12/2021

def no_e(word):
    if "e" not in word:
        return True

with open('words.txt') as infile, open('words_without_e.txt', 'w') as outfile:
    for line in infile.readlines():
        if no_e(line):
            outfile.write(line)

with open('words.txt') as all_words, open('words_without_e.txt') as no_e_words:
    num_total = len(all_words.readlines())
    num_no_e = len(no_e_words.readlines())

    percent_no_e_words = num_no_e/num_total * 100

    print("{0:.2f} percent of the words in 'words.txt' don't contain the letter 'e'.".format(percent_no_e_words))
