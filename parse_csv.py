import csv

with open('names.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file) #takes each line in the file and splits the values in the string seperated by commas into a list of values

    with open('new_names.csv','w') as new_file:
        csv_writer=csv.writer(new_file,delimiter='\t')  #will convert each list back into a string with values spaced by tabs instead of commas
        #next(csv_reader)    skips over the first list in the reader file

        for line in csv_reader: #iterates over the lists of values in our reader file
            #print(line[2])  only prints the third element of the list i.e. email
            csv_writer.writerow(line)