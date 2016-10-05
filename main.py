import csv
import re

csv.register_dialect(
    'CSV_reader',
    delimiter=',',
    quotechar='"',
    doublequote=True,
    skipinitialspace=True,
    lineterminator='\r\n',
    quoting=csv.QUOTE_MINIMAL)


def print_csv(func):
    def func_wrapper(file):
        content = func(file)
        for line in content:
            print(line)

    return func_wrapper


@print_csv
def csv_reader(file):
    with open(file, 'r') as f:
        reader = csv.DictReader(f, dialect='CSV_reader')
        word_char_pattern = re.compile(r'\w|@|\s+', re.IGNORECASE)
        clean_up = lambda x: ''.join([c for c in x["name"].title()
                                      + "\t \t"
                                      + x["surname"].title()
                                      + "\t \t"
                                      + x["email"].lower() if bool(word_char_pattern.match(c))])

        content = list(map(clean_up, reader))
        return content


if __name__ == "__main__":
    csv_reader('data/users.csv')
