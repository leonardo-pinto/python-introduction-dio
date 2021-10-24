class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        num = int(input('Insert a number between 0 and 30: '))
        if num > 30:
            raise InputError('Number must be lower than 30!')
        elif num < 0:
            raise InputError('Number must be greater than 0!')
        break
    except ValueError:
        print('Must insert a number between 0 and 30')
    except InputError as ex:
        print(ex)

while True:
    try:
        num = int(input('Insert a number between 0 and 30: '))
        if 0 <= num <= 30:
            break
    except ValueError:
        print('Must insert a number between 0 and 30')

list = [1, 2, 3]

try:
    division = 50 / 0
    invalid_index = list[1]
except ZeroDivisionError:
    print('It is not possible to divide a number by zero!')
except IndexError:
    print('Index is out of range')
except Exception as ex:
    print('The following error was found: {}'.format(ex))
else:
    print('This line is only executed if no exceptions are triggered')
finally:
    print('This line is always executed')
