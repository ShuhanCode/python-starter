import csv

#   Open the file
data = open('example.csv')

# print(data)

#  csv.reader   
csv_data = csv.reader(data)

# print(csv_data)

#  reformat it into a python object list of lists

data_lines = list(csv_data)

# print(data_lines[0])

# print(len(data_lines))

for line in data_lines[:5]:
    # print(line)
    ...    
    
# print(data_lines[10][3])    

all_emails = []

for line in data_lines[1:15]:
    all_emails.append(line[3])
    
# print(all_emails)

# print(data_lines[10])    

full_names = []

for line in data_lines[1:]:
    full_names.append(line[1] + ' ' + line[2])
    
# print(full_names)

# Writing to CSV Files - New File Mode:

file_to_output = open('to_save_file.csv', mode='w', newline='')

csv_writer = csv.writer(file_to_output, delimiter=',')

csv_writer.writerow(['a','b','c'])

csv_writer.writerows([['1','2','3'],['4','5','6']])

file_to_output.close()

# Writing to CSV Files - Existing File:

f = open('to_save_file.csv','a',newline='')

csv_writer = csv.writer(f)

csv_writer.writerow(['new','new','new'])

f.close()