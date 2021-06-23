import csv

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

def get_data(arr, column):
    with open("insurance.csv") as insurance:
        data_dict = csv.DictReader(insurance)
        for row in data_dict:
            arr.append(row[column])
    return arr

get_data(ages, 'age') 
print(ages)