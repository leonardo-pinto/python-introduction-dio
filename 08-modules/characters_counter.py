## in a given array, count the number of characters of each string

def characters_counter(list):
    counter = []
    for index in list:
        characters_numbers = len(index)
        counter.append(characters_numbers)
    return counter

if (__name__ == '__main__'):
    list = ['xablau', 'casa', 'cachorro']
    print(characters_counter((list)))