# Check if a given grade is greater than 10 using a while loop

grade = int(input('Insert your grade: '))

while grade > 10:
    grade = int(input('Grade must be between 0 and 10. Please insert a valid grade: '))

if grade > 5:
    print('Student approved')
else:
    print('Student is not approved')

# Check which numbers in a given range are prime numbers using a for loop
# numberRange = 100
#
# for number in range(1, numberRange+1):
#     div = 0
#     for index in range(1, number+1):
#         r = number % index
#         if r == 0:
#             div += 1
#     if div == 2:
#         print('{} is a prime number!'.format(number))

# Check if a given number is a prime number
# number = int(input('Insert a number: '))
#
# div = 0
#
# for index in range(1, number+1):
#     r = number % index
#     if r == 0:
#         div += 1
# if div == 2:
#     print('{} is a prime number!'.format((number)))
# else:
#     print('{} is not a prime number!'.format(number))
