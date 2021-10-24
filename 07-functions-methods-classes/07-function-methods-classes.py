## classes

class Television:
    def __init__(self):
        self.is_on = False
        self.channel = 1

    def power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def increase_channel(self):
        if self.is_on:
            self.channel += 1

    def decrease_channel(self):
        if self.is_on:
            self.channel -= 1

television = Television()
print('Television is on: {}'.format(television.is_on))
television.power()
print('Television is on: {}'.format(television.is_on))

television.increase_channel()
print('Channel selected: {}'.format(television.channel))


# television.power()
# print('Television is on: {}'.format(television.is_on))

## start with upper case letter
# class Calculator:
    ## alternative:
    # def __init__self:
    #     pass
    # def soma(self, num1, num2):
    #     return num1 + num2
    # print(calculator.sum(1, 2))

#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def sum(self):
#         return self.num1 + self.num2
#
#     def subtraction(self):
#         return self.num1 - self.num2
#
#     def div(self):
#         return self.num1 / self.num2
#
#     def multi(self):
#         return self.num1 * self.num2
#

# creating class instance
# calculator = Calculator(8, 15)


# print(calculator.sum())
# print(calculator.subtraction())
# print(calculator.div())
# print(calculator.multi())

## functions and methods
## snake_case syntax

# def sum(a, b):
#     return a + b
#
# def subtraction(a, b):
#     return a - b
#
# def div(a, b):
#     return a / b
#
# def multi(a, b):
#     return a * b
#
# print('Sum', sum(5, 7))
# print('Subtraction', subtraction(5, 7))
# print('Division', div(5, 7))
# print('Multiplication', multi(5, 7))