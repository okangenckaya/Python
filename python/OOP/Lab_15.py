#Decoration

def upper(function):
    def inner_funct(*args):
        f = function(*args)
        making_upper = f.upper()
        return making_upper

    return inner_funct


@upper
def full_name(name: str) -> str:
    return name


print(full_name('Okan'))

