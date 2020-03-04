"""
Name: Liam Hovey
SN: 040774944
Exercise 3
"""

import csv

import rowOBJ

"""open the file of the name 13100262"""
filename = "13100262.csv"
fieldnames = ['REF_DATE', 'GEO', 'DGUID', 'Sex', 'Age group', 'Student response', 'UOM', 'UOM_ID', 'SCALAR_FACTOR',
              'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS']
# the array
arrayOfRows = []
print("REF_DATE, GEO, DGUID, Sex, Age group, Student response, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID, VECTOR, "
      "COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED, DECIMALS")


# takes all rows from the csv and places them in the array
def load_all_from_csv():
    del arrayOfRows[:]
    with open(filename) as csv_file:
        """create a reader object out of the csv file"""
        csv_reader = csv.reader(csv_file)
        rowCount = 0

        """append each of the rows onto the array so that we have an array of our custom object"""
        for row in csv_reader:
            if rowCount != 0:
                rowCount += 1
                arrayOfRows.append(
                    rowOBJ.RowObj(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                  row[10],
                                  row[11], row[12], row[13], row[14], row[15], row[16]))
            else:
                rowCount += 1
    print("this program made by Liam Hovey SN 040774944")


def read_first_x(x):
    i = 0
    """loop through the array that wee mad and use the str function to print them out"""
    while i < x:
        print(arrayOfRows[i])
        i += 1
    print("this program made by Liam Hovey SN 040774944")


def delete_row(x):
    del arrayOfRows[x]
    print("this program made by Liam Hovey SN 040774944")


def read_all():
    """loop through the array that wee mad and use the str function to print them out"""
    for i in range(len(arrayOfRows)):
        print(arrayOfRows[i])
    print("this program made by Liam Hovey SN 040774944")


def read_raw():
    reader = csv.DictReader(open(filename))
    for raw in reader:
        print(raw)
    print("this program made by Liam Hovey SN 040774944")


def read_x(x):
    print(arrayOfRows[x])
    print("this program made by Liam Hovey SN 040774944")


def persist():
    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL, delimiter=',')
        for i in range(len(arrayOfRows)):
            csv_writer.writerow(
                [arrayOfRows[i].REF_DATE, arrayOfRows[i].GEO, arrayOfRows[i].DGUID, arrayOfRows[i].SEX,
                 arrayOfRows[i].AGE, arrayOfRows[i].STUDENT, arrayOfRows[i].UOM, arrayOfRows[i].UOM_ID,
                 arrayOfRows[i].SCALAR_FACTOR, arrayOfRows[i].SCALAR_ID, arrayOfRows[i].VECTOR,
                 arrayOfRows[i].COORDINATE, arrayOfRows[i].VALUE, arrayOfRows[i].STATUS, arrayOfRows[i].SYMBOL,
                 arrayOfRows[i].TERMINATED, arrayOfRows[i].DECIMALS])
    print("this program made by Liam Hovey SN 040774944")


def add(a, b, c, d, e, f, g, h, i, j, k, ll, m, n, o, p, q):
    arrayOfRows.append(rowOBJ.RowObj(a, b, c, d, e, f, g, h, i, j, k, ll, m, n, o, p, q))
    print("this program made by Liam Hovey SN 040774944")


def update(row, column, value):
    if column == 1:
        arrayOfRows[row].REF_DATE = value
    if column == 2:
        arrayOfRows[row].GEO = value
    if column == 3:
        arrayOfRows[row].DGUID = value
    if column == 4:
        arrayOfRows[row].SEX = value
    if column == 4:
        arrayOfRows[row].AGE = value
    if column == 5:
        arrayOfRows[row].STUDENT = value
    if column == 6:
        arrayOfRows[row].UOM = value
    if column == 7:
        arrayOfRows[row].UOM_ID = value
    if column == 8:
        arrayOfRows[row].SCALAR_FACTOR = value
    if column == 9:
        arrayOfRows[row].SCALAR_ID = value
    if column == 10:
        arrayOfRows[row].VECTOR = value
    if column == 11:
        arrayOfRows[row].COORDINATE = value
    if column == 12:
        arrayOfRows[row].VALUE = value
    if column == 13:
        arrayOfRows[row].STATUS = value
    if column == 14:
        arrayOfRows[row].SYMBOL = value
    if column == 15:
        arrayOfRows[row].TERMINATED = value
    if column == 16:
        arrayOfRows[row].DECIMALS = value
    print("this program made by Liam Hovey SN 040774944")
