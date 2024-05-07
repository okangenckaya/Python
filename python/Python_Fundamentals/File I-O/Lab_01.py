
# How to open a new file ?
file = open(file='new_file.txt', mode='w', encoding='utf-8')

file.write('Full Name: Okan Gençkaya\nOccupation: Jobeless\n')
file.close()

# How to add any information to existed file ?

file = open(file='new_file.txt', mode='a', encoding='utf-8')
file.write('Programing Language: Python(learning)\n')
file.close()

file = open(file='new_file.txt', mode='a', encoding='utf-8')
file.write('Age: 24\n')
file.close()

# How to read information here ?

file = open(file='new_file.txt', mode='r', encoding='utf-8')
for sentence in file.readlines():
    print(sentence)


