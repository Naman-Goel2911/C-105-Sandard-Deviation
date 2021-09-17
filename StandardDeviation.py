import pandas as pd
import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def meanCalculator(data):
    n = len(data)
    total = 0

    for number in data:
        total += int(number)
    
    mean = total/n

    return mean

squaredList = []

for number in data:
    a = int(number) - meanCalculator(data)
    a = a**2
    squaredList.append(a)

sum = 0

for i in squaredList:
    sum+=i

result = sum/(len(data)-1)

standardDeviation = math.sqrt(result)

print(standardDeviation)