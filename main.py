import csv

"""
Read CSV file
"""

import csv

csv.register_dialect(
    'CSV_reader',
    delimiter=',',
    quotechar='"',
    doublequote=True,
    skipinitialspace=True,
    lineterminator='\r\n',
    quoting=csv.QUOTE_MINIMAL)

with open('data/users.csv') as csvfile:
    input_file = csv.reader(csvfile, dialect='CSV_reader')
    next(input_file, None)
    names = []
    surnames = []
    emails = []
    for column in input_file:
        name = column[0].replace('!', '').strip().title()
        surname = column[1].replace('!', '').strip().title()
        email = column[2].replace('!', '').strip().lower()

        names.append(name)
        surnames.append(surname)
        emails.append(email)

        output = name + "\t \t" + surname + "\t \t" + email

        print(output)
