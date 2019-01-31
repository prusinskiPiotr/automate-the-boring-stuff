import csv
import numpy as np

dataFile = open('usproduction.csv')
dataReader = csv.reader(dataFile)
data = list(dataReader)

a = np.array(data, dtype=float)
print(a)

# for i in dataReader:
# maxEl = max(float(element[-1]) for element in data)
# for i in range(len(data)):
#     print(type(data[i][-1]))
#     maximum = 0
    # if data[i][-1] > maximum:
    #     maximum = data[i][-1]

# print(maximum)