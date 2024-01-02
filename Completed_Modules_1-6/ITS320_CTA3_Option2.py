"""

    Create a program that will calculate the weekly average tax withholding for a customer,
        given the following weekly income guidelines:
    Income less than $500: tax rate 10%
    Incomes greater than/equal to $500 and less than $1500: tax rate 15%
    Incomes greater than/equal to $1500 and less than $2500: tax rate 20%
    Incomes greater than/equal to $2500: tax rate 30%

    Store the income brackets and rates in a dictionary.
    Write a statement that prompts the user for an income
        and then looks up the tax rate from the dictionary and prints the income, tax rate, and tax.
    Develop Python code that implements the program requirements.

"""


def compute_tax(income, tax_rate):
    for key in tax_rate:
        if income > key:
            tax_rate_percentage = str(tax_rate[key] * 100)
            tax = income * tax_rate[key]
            return 'Income: ' + str('{0:.2f}'.format(income)) \
                   + ', Tax rate: ' + tax_rate_percentage + '%' \
                   + ', Tax: ' + str('{0:.2f}'.format(tax))


tax_rate = {2500: .3, 1500: .2, 500: .15, 0: .1}
income = float(input('Enter an income: '))
income = 0 if income < 0 else income
print(compute_tax(income, tax_rate))
