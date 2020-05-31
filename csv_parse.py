import csv

#  List to hold all our data
data_list = []
#  Open the CSV
with open('data.csv', 'r') as data:
    reader = csv.reader(data)
    for row in reader:
        data_list.append(row)

# data_list now has a list of lists
# The state is stored in slot 1
#  Open write channel to our parsed_data file
#  Cases in slot 3
with open('parsed_data2.csv', 'w') as parsed_data:
    data_writer = csv.writer(parsed_data, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(data_list[0])
    print(data_list[0])
    prev_i = 0
    for i in range(1, len(data_list)):
        if(data_list[i][1] == 'Washington'):
            data_writer.writerow(data_list[i])
            print(data_list[i])
