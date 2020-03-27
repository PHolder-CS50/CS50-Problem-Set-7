# print the names and birth years of students from a house name
# supplied as the command line parameter


from cs50 import SQL
from sys import argv, exit


# Check that the command line parameter is correct and then
# print the roster for the house
def main():
    if len(argv) != 2:
        print("usage: python roster.py Gryffindor")
        exit(1)

    rosterHouse = argv[1]
    # print(f"rosterHouse={rosterHouse}")
    printRosterForHouse(rosterHouse)


# Print a roster of students for the specified house
def printRosterForHouse(house):
    db = SQL("sqlite:///students.db")
    roster = db.execute("select * from students where house = ? order by last, first;", house)
    # print(roster)

    for student in roster:
        # print(student)
        first = student["first"]
        middle = student["middle"]
        last = student["last"]
        if middle == None:
            fullName = first + " " + last
        else:
            fullName = first + " " + middle + " " + last
        # print(fullName)
        born = student["birth"]
        print(f"{fullName}, born {born}")


# Run the program
main()
