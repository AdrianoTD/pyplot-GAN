import csv
import numpy as np
from matplotlib import pyplot as plt

with open('result.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    
    row = next(csv_reader)
    
    for row in csv_reader:
        print(row)
        
        #teste git
        #TTATTT
        #teste 3
