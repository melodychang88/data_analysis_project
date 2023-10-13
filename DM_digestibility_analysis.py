#read csv
import csv

# fuction for reading csv
def read_csv(filename):
    all_rows = []
    
    # use encoding "utf-8-sig" read csv
    with open(filename, encoding='utf-8-sig') as csvfile:
        raw_data = csv.reader(csvfile)
        # read raw data in row
        for row in raw_data:
            # data is added into list "all_rows"
            all_rows.append(row)
    
    return all_rows

treatment1_raw= read_csv("sow1_CON_DM_digestibility.csv")
treatment2_raw= read_csv("sow1_0.1%_DM_digestibility.csv")
treatment3_raw= read_csv("sow1_0.2%_DM_digestibility.csv")


# function for transforming list to dictionary
def raw_data_to_dict(treatment):
    #第0列為各column名稱 
    col_names = treatment[0]
    all_data = []
    
    #第一列以下的data為dict的value
    for row in treatment[1:]:
        #一個key對一個value
        i = 0
        row_dict = {}
        for col_name in col_names:
            row_dict[col_name] = row[i]
            i += 1
        all_data.append(row_dict)
    
    return all_data

treatment1_dict= raw_data_to_dict(treatment1_raw)       
treatment2_dict=raw_data_to_dict(treatment2_raw)
treatment3_dict=raw_data_to_dict(treatment3_raw)

# function for multipling data 
def multiply_data(treatment_dict, new_key, key1, key2):
    data_multiplication = []
    # 從treatment_dict中一次取一個dict處理
    for data in treatment_dict:
        multiplication_dict = {}
        # built a new_key in multiplication_dict, value is key1*key2
        # the value of key1 and key2 is str, which needs to change to float
        #round(variable, n取幾位)
        multiplication_dict[new_key] = round(float(data[key1])*float(data[key2]), 4)
        # dict is added into list "data_multiplication"
        data_multiplication.append(multiplication_dict)

    return data_multiplication

# use "multiply_data" function to gain diet dry matter 
treatment1_diet_DM= multiply_data(treatment1_dict, 'Diet_DM', 'Diet_weight', 'Diet_DM_percentage')
treatment2_diet_DM= multiply_data(treatment2_dict, 'Diet_DM', 'Diet_weight', 'Diet_DM_percentage')
treatment3_diet_DM= multiply_data(treatment3_dict, 'Diet_DM', 'Diet_weight', 'Diet_DM_percentage')


# function for subtrcting data
def subtract_data(treatment_dict, new_key, key1, key2):
    data_subtraction = []
    # 從treatment_dict中一次取一個dict處理
    for data in treatment_dict:
        subtraction_dict = {}
        # built a new_key in subtraction_dict, value is key1-key2
        # the value of key1 and key2 is str, which needs to change to float
        #round(variable, n取幾位)
        subtraction_dict[new_key] = round(float(data[key1])-float(data[key2]), 4)
        # dict is added into list "data_subtraction"
        data_subtraction.append(subtraction_dict)
    
    return data_subtraction

# use "substract_data" function to gain digesta weight
treatment1_digesta_weight= subtract_data(treatment1_dict, 'Digesta_weight', 'Freeze_dry_weight', 'Tube_weight')
treatment2_digesta_weight= subtract_data(treatment2_dict, 'Digesta_weight', 'Freeze_dry_weight', 'Tube_weight')
treatment3_digesta_weight= subtract_data(treatment3_dict, 'Digesta_weight', 'Freeze_dry_weight', 'Tube_weight')


# calculate DM digestibility
def calculate_DM_digestibility(treatment_diet_DM, treatment_digesta_weight):
    dry_matter_digestibility = []
    for diet_data, digesta_data in zip(treatment_diet_DM, treatment_digesta_weight):
        DM_digestibility_dict = {}
        diet_DM = float(diet_data['Diet_DM'])
        digesta_wt = float(digesta_data['Digesta_weight'])
        DM_digestibility_dict['DM_digestibility'] = round((diet_DM - digesta_wt) / diet_DM * 100, 4)
        dry_matter_digestibility.append(DM_digestibility_dict)
    
    return dry_matter_digestibility

# use "calculate_DM_digestibility" function to gain DM digestibility
treatment1_DM_digestibility= calculate_DM_digestibility(treatment1_diet_DM, treatment1_digesta_weight)
treatment2_DM_digestibility= calculate_DM_digestibility(treatment2_diet_DM, treatment2_digesta_weight)
treatment3_DM_digestibility= calculate_DM_digestibility(treatment3_diet_DM, treatment3_digesta_weight)

# sort data from the smallest to the largest
def sort_data(treatment_data, data_key):
    data_sequence= []
    for data in treatment_data:
        data_sequence.append(float(data[data_key]))
    
    data_sequence.sort()
    return data_sequence

# use "sort_data" function to sort data
treatment1_DM_digestibility_sequence= sort_data(treatment1_DM_digestibility, 'DM_digestibility')
treatment2_DM_digestibility_sequence= sort_data(treatment2_DM_digestibility, 'DM_digestibility')
treatment3_DM_digestibility_sequence= sort_data(treatment3_DM_digestibility, 'DM_digestibility')

 
 
 