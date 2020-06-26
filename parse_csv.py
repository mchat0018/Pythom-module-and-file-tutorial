import csv

with open('names.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)     #reads each line as a dictionary with the field names as keys

    with open('new_names.csv','w') as new_file:
        field_names=['first_name','last_name','email']
        csv_writer=csv.DictWriter(new_file,fieldnames=field_names,delimiter='\t')   #writes the dictionary back as a string with values seperated by tabs
        csv_writer.writeheader()    #fieldnames added  

        for line in csv_reader: #iterates over the lists of values in our reader file
            #print(line["email"])  only prints the 'email' keys of the dictionary
            csv_writer.writerow(line)