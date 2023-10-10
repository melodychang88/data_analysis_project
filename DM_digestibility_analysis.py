#read csv
import csv
all_rows = []
with open("sow1_CON_DM_digestibility.csv", encoding='utf-8-sig') as csvfile :
    raw_data = csv.reader(csvfile)
    for row in raw_data:
        all_rows.append(row)


# transform list to dictionary 
col_names = all_rows[0]
all_data = []
for row in all_rows[1:]:
    i = 0
    row_dict = {}
    for col_name in col_names:
        row_dict[col_name] = row[i]
        i += 1
    all_data.append(row_dict)
           
all_data

#calculate diet dry matter
diet_dry_matter= []
#從all_data中一次取一個dict
for data in all_data[0:]:
    dm_dict = {}
    dm_dict['Diet_DM'] = float(data['Diet weight'])*float(data['Diet_DM_percentage'])
    diet_dry_matter.append(dm_dict)

diet_dry_matter




sample_1 = all_rows[1]
diet_dry_matter = float(sample_1[2])* float(sample_1[3])
print(diet_dry_matter)
