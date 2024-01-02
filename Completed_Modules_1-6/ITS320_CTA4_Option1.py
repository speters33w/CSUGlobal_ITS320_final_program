# Write a program that utilizes a loop to read a set of five floating-point values from user input.
# Ask the user to enter the values, then print the following data:
#
#     Total
#     Average
#     Maximum
#     Minimum
#     Interest at 20% for each original value entered by the user.
#     Use the formula: Interest_Value = Original_value + Original_value*0.2

from statistics import mean

print('\nThis program takes five values and computes the total of all the values, the average value, '
      'the maximum value, the minimum value, and interest at 20% for each original value.\n')
value1: float = float(input('Enter the first value: '))
value2: float = float(input('Enter the second value: '))
value3: float = float(input('Enter the third value: '))
value4: float = float(input('Enter the fourth value: '))
value5: float = float(input('Enter the fifth value: '))
values = (value1, value2, value3, value4, value5)
print('\nYou entered:', values)
print('\nThe total of all the values you entered is', '{0:.2f}'.format(sum(values)))
print('\nThe average of the values you entered is', '{0:.2f}'.format(mean(values)))
print('\nThe maximum value of the values you entered is', '{0:.2f}'.format(max(values)))
print('\nThe minimum value of the values you entered is', '{0:.2f}'.format(min(values)))
print('')
for value in values:
    print('{0:.2f}'.format(value), "with 20% interest is", '{0:.2f}'.format(value + (value * .2)))
