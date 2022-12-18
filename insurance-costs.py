import csv

# empty lists for the attributes in insurance.csv

ages = []
sexes = []
bmis = []
number_of_children = []
smoker_status = []
regions = []
insurance_charges = []


# function to load csv file
def load_list_data(lst, csv_file, column_name):
    with open(csv_file) as insurance_info:
        # reading the data of the csv
        insurance_dict = csv.DictReader(insurance_info)
        # looping through each row of the csv
        for row in insurance_dict:
            # adding data of each row to a list
            lst.append(row[column_name])
        return lst 

load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(number_of_children, 'insurance.csv', 'children')
load_list_data(smoker_status, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


class PatientInfo:
    # init method that takes in each list parameter
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_status,
                patients_regions, patients_insurance_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_numb_of_children = patients_num_children
        self.patients_smoker_status = patients_smoker_status
        self.patients_regions = patients_regions
        self.patients_insurance_charges = patients_insurance_charges

    # method that calculates the average ages of the patients in insurance.csv
    def analyze_ages(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
        # returning total age divided by the length of 'patients_age' list  
        print('Average Paitient Age: ' + str(round(total_age/len(self.patients_ages), 2)) + ' years')

    # method that calculates the number of males and females in insurance.csv
    def analyze_sexes(self):
        males = 0 
        females = 0
        # iterating through each sex in sexes list
        for sex in self.patients_sexes:
            if sex == 'male':
                males += 1 
            elif sex == 'female':
                females +=1
        #printing out the number of each 
        print(f'Number of males in the list: {males}')
        print(f'Number of females in the list: {females}')
    
    def costs_difference(self):
        # converting two lists into a dictionary
        insurance_zipped = dict(zip(self.patients_smoker_status, self.patients_insurance_charges))
        # initializing empty variables
        smokers_total_insurance = 0
        nonsmokers_total_insurance = 0
        total_smokers = 0
        total_nonsmokers = 0
        # iterating through each key in the dictionary
        for key, value in insurance_zipped.items():
            # if it's a smoker add values to total insurance and increasing number of smokers by 1 
            if key == 'yes':
                smokers_total_insurance += float(value)
                total_smokers += 1 
            # if it's not a smoker add values to non-smokers total insurance and increasing number of non-smokers by 1 
            elif key == 'no':
                nonsmokers_total_insurance += float(value)
                total_nonsmokers += 1
        
        print('Average Insurance Cost For Smokers: $' + (str(round(smokers_total_insurance/total_smokers))) + ' dollars.')
        print('Average Insurance Cost For Non-smokers: $' + (str(round(nonsmokers_total_insurance/total_nonsmokers))) + ' dollars.')

    # method to find each unique region patiens are from
    def unique_regions(self):
        unique_region = []
        # iterate through each region in regions list
        for region in self.patients_regions:
            # if the region is not already in the unique regions list
            # then add it to the unique regions list
            if region not in unique_region:
                unique_region.append(region)
        print('Unique Regions: ' + str(unique_region))

    # method that calculates the average ages for patients who have at least one child in dataset
    def parents_age(self):
        # converting two lists into a dictionary
        parents_zip = dict(zip(self.patients_numb_of_children, self.patients_ages))
        parents_age = 0
        total_parents = 0 
        for key, values in parents_zip.items():
            if int(key) > 0:
                parents_age += int(values)
                total_parents += 1
        print('Average patients age who have at least one child: ' + str(round(parents_age/total_parents)))
        
    # method to find average yearly medical charges for patients in insurance.csv
    def average_charges(self):
        # initialize total_charges variable
        total_charges = 0
        # iterate through charges in patients charges list
        # add each charge to total_charge
        for charge in self.patients_insurance_charges:
            total_charges += float(charge)
        # return the average charges rounded to the hundredths place
        print ("Average Yearly Medical Insurance Charges: " +  
                str(round(total_charges/len(self.patients_insurance_charges), 2)) + " dollars.")

patient_info_instance = PatientInfo(ages, sexes, bmis, number_of_children, smoker_status, regions, insurance_charges)
patient_info_instance.analyze_ages()
patient_info_instance.analyze_sexes()
patient_info_instance.unique_regions()
patient_info_instance.costs_difference()
patient_info_instance.parents_age()
patient_info_instance.average_charges()