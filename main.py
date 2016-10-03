import csv

"""
Read CSV file
"""


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))


if __name__ == "__main__":
    csv_path = 'data/users.csv'
    with open(csv_path) as f_obj:
        csv_reader(f_obj)
