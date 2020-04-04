'''
    Author: regi18

    Convert ISTAT CSV files to SQL data:

    https://www.istat.it/storage/codici-unita-amministrative/Codici-statistici-e-denominazioni-delle-ripartizioni-sovracomunali.zip
    https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv
'''
import csv
import sys
import codecs


f = codecs.open(r"istat_data.sql","w+", "utf-8")



f.write("-- regions\n")

# regions
with open('Codici statistici e denominazioni delle ripartizioni sovracomunali .csv') as csv_file:
    regions = []
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count > 1:
            if (row[14] != 'Unità non amministrativa' and row[14] != 'Provincia soppressa'):
                # id, name, region (id),
                regions.append(f'INSERT INTO region VALUES({int(row[5])}, `{row[7]}`);\n')
        line_count += 1
    print(f'Regions: Processed {line_count} lines.')
    for region in list(dict.fromkeys(regions)):
        f.write(region)



f.write("\n-- province\n")

# province
with open('Codici statistici e denominazioni delle ripartizioni sovracomunali .csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count > 1:
            if (row[14] != 'Unità non amministrativa' and row[14] != 'Provincia soppressa'):
                # id, name, region (id),
                f.write(f'INSERT INTO province VALUES(`{row[15]}`, `{row[12]}`, {int(row[5])});\n')
        line_count += 1
    print(f'Province: Processed {line_count} lines.')



# cities
f.write("\n-- cities\n")

with open('Elenco-comuni-italiani.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count > 1:
            f.write(f'INSERT INTO city VALUES({int(row[14])}, `{row[6]}`, `{row[13]}`);\n')
        line_count += 1
    print(f'Cities: Processed {line_count} lines.')
