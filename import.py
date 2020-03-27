# Import the characters in a csv file into the database
# Handle characters with or without middle names


import csv
import re
from cs50 import SQL
from sys import argv, exit


# Check the command line parameter and then do the import
def main():
    if len(argv) != 2:
        print("usage: python import.py {csvFile}")
        exit(1)

    csvFileName = argv[1]
    # print(f"csvFileName={csvFileName}")

    db = SQL("sqlite:///students.db")
    # remove any previous data in the students table
    # presumably from failed imports
    db.execute("delete from students;")

    doImport(csvFileName, db)


# The import process reads the students as csv dictionary
# then breaks apart the parts of the name and then inserts
# into the database
def doImport(csvFileName, db):
    with open(csvFileName) as src:
        reader = csv.DictReader(src)
        for row in reader:
            # print(row)
            first, middle, last = extractNameParts(row["name"])
            house = row["house"]
            birth = int(row["birth"])
            # print(f"first={first} middle={middle}, last={last}")
            # print(f"house={house}")
            # print(f"birth={birth}")
            if middle == "":
                db.execute("insert into students(first,last,house,birth) values (?,?,?,?);", first, last, house, birth)
            else:
                db.execute("insert into students(first,middle,last,house,birth) values (?,?,?,?,?);", first, middle, last, house, birth)


# Use a regular expression to break apart a name into 2 or 3
# parts depending on whether there is a middle name or not
def extractNameParts(name):
    # print(name)
    parts = re.search("(\w+) (?:(\w+) )?([-\w]+)", name)
    if parts.group(2) == None:
        return parts.group(1), "", parts.group(3)
    else:
        return parts.group(1), parts.group(2), parts.group(3)


# Run the program
main()
