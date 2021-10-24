# characters_counter = lambda list: [len(i) for i in list]

list = ['cachorro', 'gato', 'girafa']
print(characters_counter(list))

sum = lambda a, b: a + b
print(sum(15, 85))

## calculator function - lambda dictionary

calculator = {
    'sum': lambda a, b: a + b,
    'subtraction': lambda a, b: a - b,
    'multiplication': lambda a, b: a * b,
    'division': lambda a, b: a / b,
}

print(type(calculator))
sum = calculator['sum']
subtraction = calculator['subtraction']
print(sum(56, 74))
print(subtraction(85, 62))

