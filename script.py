import csv
from smoker_class import AnalizeSmokers

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
get_data(sexes, 'sex')
get_data(bmis, 'bmi')
get_data(smoker_statuses, 'smoker')
get_data(num_children, 'children')
get_data(regions, 'region')
get_data(insurance_charges, 'charges')

smoker_data = AnalizeSmokers(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)
smoker_data.analize_ages()
smoker_data.analize_sexes()
smoker_data.analize_bmis()
smoker_data.analize_charges()
smoker_data.analize_children()