'''
Author: Edward Drobnis
Date: March 8, 2024
Title: HST
Description: Calculates the HST of a product and the total cost (the original price with the HST)
'''

cost = float(input('Price of item: $'))

hst = 0.13 * cost
total_cost = cost + hst

print('-------------------------')
print('|{0:>12}  $ {1:6.2f} |'.format('Cost', cost))
print('|{0:>12}  $ {1:6.2f} |'.format('HST', hst))
print('-------------------------')
print('|{0:>12}  $ {1:6.2f} |'.format('Total Cost', total_cost))
print('-------------------------')