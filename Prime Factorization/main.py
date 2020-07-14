import math
factors = []
num = int(input("Enter in a number: "))
numMax = num
product = 1
for divisor in range(2, numMax):
    while num / divisor == round((num / divisor), 0):
            factors.append(divisor)
            num /= divisor
            print(factors)
if factors == []:
    factors = [num]
for factor in factors:
    product *= factor    
print(product)
