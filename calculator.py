#imports
from functools import reduce # for multiplication counting
import operator # for multiplication counting
from collections import Counter # for mode counting
import numpy as np # for percentiles
import pandas as pd # for skewness

numbersinput = input("Enter the numbers you want to calculate: ")
calculate = True
even = False
numbers_str_list = numbersinput.split()
numbers = [int(num) for num in numbers_str_list]
sortednumbers = sorted(numbers)
numberamount = len(numbers)

if len(numbers) > 10:
    calculate = False
    print("You can only calculate 10 or less numbers!")

if numberamount % 2 == 0:
    even = True

#calculations:

#addition
addition = sum(numbers)
#subtraction
subtraction = numbers[0]
for num in numbers[1:]:
    subtraction -= num
#multiplication
multiplication = reduce(operator.mul, numbers, 1)
#division
division = numbers[0]
for num in numbers[1:]:
    division /= num
#average
average = addition / numberamount
#median
mid = numberamount // 2

if even == True:
    median = (numbers[mid - 1] + numbers[mid]) / 2
else:
    median = numbers[mid]
#mode
mode_data = Counter(numbers)
mode = mode_data.most_common(1)[0][0]
#first number
firstnumber = numbers[0]
#last number
lastnumber = numbers[-1]
#sorted first number
sortedfirstnumber = sortednumbers[0]
#sorted last number
sortedlastnumber = sortednumbers[-1]
#percentiles
Q1 = np.percentile(sortednumbers, 25)
Q2 = np.percentile(sortednumbers, 50)
Q3 = np.percentile(sortednumbers, 75)
#range, highest subtracted by lowest numbers
range = max(numbers) - min(numbers)
#skewness
data_series = pd.Series(numbers)
skewness = data_series.skew()




#number printing
print("--- Checks")
print("- Numbers are calculable:          ", calculate)
print("- Amount of numbers:               ", numberamount)
print("- Amount of numbers is even:       ", even)
print("- Selected numbers are:            ", numbers)
print("- Sorted selected numbers are:     ", sortednumbers)
print(" ")
print("- first number is:                 ", firstnumber)
print("- last number is:                  ", lastnumber)
print("- first sorted number is:          ", sortedfirstnumber)
print("- last sorted number is:           ", sortedlastnumber)
print(" ")
print("--- Basic Calculations")
print("- Addition using all numbers:      ", addition)
print("- Subtraction using all numbers:   ", subtraction)
print("- Multiplication using all numbers:", multiplication)
print("- Disivision using all numbers:    ", division)
print(" ")
print("--- Calculations")
print("- The range of all the numbers:    ", range)
print("- The skewness of all the numbers: ", skewness)
print(" ")
print("--- Percentiles")
print("- Q1 or 25%:                       ", Q1)
print("- Q2 or 50%:                       ", Q2)
print("- Q3 or 75%:                       ", Q3)