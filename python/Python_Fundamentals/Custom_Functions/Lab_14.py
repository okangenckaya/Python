
def removing_dublicates(sentence: str) -> str:
    lst = []
    result = ''
    for i in sentence.split(' '):
        if i not in lst:
            lst.append(i)

    result = ' '.join(lst)
    return result


sentence_taken_by_user = input('Please type your sentence: ')
result = removing_dublicates(sentence_taken_by_user)
print(result)



