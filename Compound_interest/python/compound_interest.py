# -*- coding: utf-8 -*-

# Estimate interest
print('')
print('')

print('Welcome to the compound interest calculator!')

# print('Select [1] As USD')
# print('Select [2] As EUR')
# print('Select [3] As GBP')
# print('Select [4] As BTC')
# print('')
#
# try:
#     choice = int(input('Please Select Currnecy: '))
# except:
#     print('Invalid Choice')
#
# if choice == 1:
#     print('$' + final_output)
# if choice == 2:
#     print('€' + final_output)
# if choice == 3:
#     print('£' + final_output)
# if choice == 4:
#     print('₿' + final_output)

# TODO: figure out a way to put this ^^ in use in the print of final_output
# TODO: Add average inflation rate of each Currnecy to ^^ to final_output


# ex:
def calcWeeklyWages(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime for hours over 40.
    '''
    if totalHours <= 40:
        totalWages = hourlyWage*totalHours
    else:
        overtime = totalHours - 40
        totalWages = hourlyWage*40 + (1.5*hourlyWage)*overtime
    return totalWages #  returns function when it's called




print('')

print('Enter period of interest (years)')
years = int(raw_input('Enter years: '))

print('What is the initial principal?')
principal = float(raw_input('Enter principal: '))

print('What are the monthly contributions?')
contributions = float(raw_input('Enter amount: '))

print('What is the ARP (in decimal format)?')
ARP = float(raw_input('Enter percentage: '))

print(' ')

contributions = contributions * 12
final_amount = 0

for i in range(0, years):
    if final_amount == 0 :
        final_amount = principal

    final_amount = (final_amount + contributions) * (1 + ARP)
    final_output = 'Final amount gained after {} years: '.format(years) + '{:,}'.format(round(final_amount, 2)) + ' at a {:.2%} ARP '.format(ARP)
# display avg inflation rate in final output

print('')
