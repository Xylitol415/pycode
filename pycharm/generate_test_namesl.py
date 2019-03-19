import random


def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "F:/pycode/forenames.txt"),
        (surnames, "F:/pycode/surnames.txt")):
        for name in open(filename, encoding="utf8"):
            names.append(name.rstrip())
        return forenames, surnames

forename, surname = get_forenames_and_surnames()
fh = open("test-name1.txt", "w", encoding="utf8")
for i in range(100):
    line = "{0} {1}\n".format(random.choice(forename),
                             random.choice(surname))
    fh.write(line)
limit = 100
years = list(range(1970,2013))*3
for year, fore_name, sur_name in zip(
    random.sample(years, limit),
    random.sample(years, limit),
    random.sample(forename, limit),
    random.sample(surname, limit)):
    name = "{0}{1}".format(fore_name, sur_name)
fh.write("{0:.<25}.{1}\n".format(name,year))