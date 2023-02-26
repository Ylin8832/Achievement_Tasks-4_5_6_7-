
# Name:                     Task 6: Prime Numbers
# Author:                   Yunfeng Lin (Ylin8832)
# Date Created:             February 25, 2023
# Date Last Modified:       February 26, 2023

print("\n{0:-^64s}".format("Welcome to prime number checking Program".upper()))


numbers = input("\nPlease enter a comma-separated list of whole numbers: ") # Prompt user to input any number of integers.

numberList = [int(num.strip()) for num in numbers.split(",")] # Save the input numbers using string split() method and change type to integer.

import math

primeNums = []
non_primeNums = []

for num in numberList: 
    prime = True   # Check if prime is true
    if num < 2:
        prime = False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prime = False
                break
    if prime:
        primeNums.append(num) # Append numbers to the list
    else:
        non_primeNums.append(num) # Append numbers to the list

print("Prime numbers: " + ", ".join(str(num) for num in primeNums))
print("Non-prime numbers: " + ", ".join(str(num) for num in non_primeNums))