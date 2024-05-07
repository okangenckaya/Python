

def sorting_sentence(sentence: str) -> None:
    words = [word.lower() for word in sentence.split(' ')]
    words.sort()
    for i in words:
        print(i)


sentence_taken_by_user = input('Please type something: ')
sorting_sentence(sentence_taken_by_user)

