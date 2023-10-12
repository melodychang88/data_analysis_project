#read csv
import csv
all_rows = []
with open("sow1_CON_DM_digestibility.csv", encoding='utf-8-sig') as csvfile :
    raw_data = csv.reader(csvfile)
    #預設以列讀取data
    for row in raw_data:
        #把數據加進去空list裡
        all_rows.append(row)


# transform list to dictionary
#第0列為各column名稱 
col_names = all_rows[0]
all_data = []
#第一列以下的data為dict的value
for row in all_rows[1:]:
    #一個key對一個value
    i = 0
    row_dict = {}
    for col_name in col_names:
        row_dict[col_name] = row[i]
        i += 1
    all_data.append(row_dict)
           
all_data

#calculate diet dry matter
diet_dry_matter = []
#從all_data中一次取一個dict
for data in all_data:
    dm_dict = {}
    dm_dict['Diet_DM'] = round(float(data['Diet_weight'])*float(data['Diet_DM_percentage']), 4)
    diet_dry_matter.append(dm_dict)

diet_dry_matter

#calculate digesta weight
digesta_weight = []
#從all_data中一次取一個dict
for data in all_data:
    digesta_dict = {}
    #round(X變數, n取幾位)
    digesta_dict['Digesta_weight'] = round(float(data['Freeze_dry_weight'])-float(data['Tube_weight']), 4)
    digesta_weight.append(digesta_dict)

digesta_weight

#calculate DM digestibility
dry_matter_digestibility = []
for diet_data, digesta_data in zip(diet_dry_matter, digesta_weight):
    DM_digestibility_dict = {}
    diet_DM = float(diet_data['Diet_DM'])
    digesta_wt = float(digesta_data['Digesta_weight'])
    DM_digestibility_dict['DM_digestibility'] = round((diet_DM - digesta_wt) / diet_DM * 100, 4)
    dry_matter_digestibility.append(DM_digestibility_dict)
    
dry_matter_digestibility

# put the digestibility in sequence
digestibility_sequence = []
for digest_data in dry_matter_digestibility:
    digestibility_sequence.append(digest_data['DM_digestibility'])

digestibility_sequence.sort()
print(digestibility_sequence)

# delete extreme value
def filter_extremes(data, lower_threshold, upper_threshold):
    filtered_data = [x for x in data if lower_threshold <= x <= upper_threshold]
    return filtered_data
 
 
 
 