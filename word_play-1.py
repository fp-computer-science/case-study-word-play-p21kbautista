# Kyle B, Joshua P (AMDG) 2/12/2021

my_file = open("words.txt", 'r')
while True:
    line = my_file.readline()
    if len(line) < 20:
        with open('greater_than_20.txt', 'a') as afile:
            afile.write(line)
    else:
        continue
my_file.close()
