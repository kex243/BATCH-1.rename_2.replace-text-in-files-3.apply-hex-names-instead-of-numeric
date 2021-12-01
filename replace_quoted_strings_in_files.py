import os, csv
with open('replace/111.csv', 'r') as read_obj:

    csv_reader = csv.reader(read_obj)

    list_of_rows = list(csv_reader)


print (list_of_rows)

#all files
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    with open(f, 'r+') as file:
        content = file.read()
        for z in list_of_rows:
            content = content.replace('"'+z[0]+'"','"'+z[1]+'"') 
    with open("replaced/" + f, 'w') as file:
        file.write(content)
