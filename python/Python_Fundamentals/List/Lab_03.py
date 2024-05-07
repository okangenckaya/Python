
# Take a sentence from the user.
# Create a new list and this list contents vowels and consonant.
# Distinguish vowels and consonant inside the sentence.
# If input taken by the user involves a number or numbers, remove number(s).
# Punctutations must be eliminated automatically from the sentence.
# Create a counter that enables to count blankes inside the sentence.

from string import punctuation

vowels = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
caught_wovels = []
caught_consonants = []
counted_blanks = 0

sentence = input('Please enter a sentence. ')

for character in sentence:
    if character in vowels:
        if character not in caught_wovels:
            caught_wovels.append(character)
    elif character == ' ':
        counted_blanks += 1
    elif character.isdigit() or character in punctuation:
        pass
    else:
        caught_consonants.append(character)

print(f'Wovels in the sentence you have typed : {caught_wovels}')
print(f'Consonants in the sentence you have typed : {caught_consonants}')
print(f'Counted blanks in the sentence you have typed : {counted_blanks}')



