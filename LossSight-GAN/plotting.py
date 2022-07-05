import csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('result.csv')

df = pd.DataFrame(data)

x = list(df.iloc[:, 0])
y = list(df.iloc[:, 0])

plt.bar(x, y, color='b')
plt.title("DDDDD")
plt.xlabel("AAAAA")
plt.ylabel("BBBBB")

plt.show()

"""
with open('result.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    
    row = next(csv_reader)
    
    for row in csv_reader:
        print(row)
        
        #teste git
        #TTATTT
        #teste 3
"""
