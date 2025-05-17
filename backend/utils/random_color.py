from random import randrange

def random_color():
    letters = '0123456789ABCDEF'
    color = '#'

    for letter in range(6):
        color += letters[randrange(0,15)]

    return color