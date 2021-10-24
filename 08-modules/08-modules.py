from module_example import Television
from characters_counter import characters_counter

if __name__ == '__main__':
    television = Television()
    print(television.is_on)
    television.power()
    print(television.is_on)
    list = ['cachorro', 'gato', 'ornitorrinco']
    print(characters_counter(list))

