import csv

data = []

with open("insurance.csv", "w") as insurance:
    fields = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
    
