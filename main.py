import csv

csv.register_dialect(
    'CSV_reader',
    delimiter=',',
    quotechar='"',
    doublequote=True,
    skipinitialspace=True,
    lineterminator='\r\n',
    quoting=csv.QUOTE_MINIMAL)


def csv_reader(file):
    reader = csv.DictReader(file, dialect='CSV_reader')
    for line in reader:
        print(''.join(c for c in
                      line["name"].title() + "\t \t" +
                      line["surname"].title() + "\t \t" +
                      line["email"].lower()
                      if c not in '/><=+-?!#"  "$%^&*""()" "_+:;'))


if __name__ == "__main__":
    with open('data/users.csv') as f:
        csv_reader(f)
