"""
Name: Liam Hovey
SN: 040774944
Assignment 3
"""
import CSVfileControl


CSVfileControl.load_all_from_csv()
z = 0
while z == 0:
    print("press 1 if you want to read all rows")
    print("press 2 if you want remove a row")
    print("press 3 if you want to update a row")
    print("press 4 if you want to read the first x rows")
    print("press 5 to read one row")
    print("press 6 to add new row")
    print("press 7 to refresh")
    print("press 8 to persist")
    print("press 9 to exit")
    while True:
        try:
            x = input()
            break
        except NameError:
            print("please enter a number")
    if x == 1:
        CSVfileControl.read_all()
    if x == 2:
        print("enter the number of the row you wish to remove")
        y = input()
        CSVfileControl.delete_row(y)
    if x == 3:
        while True:
            try:
                i = input("What Row do you want to update?")
                break
            except NameError:
                print("please enter a number")
        while True:
            try:
                j = input("what column do you want to update?")
                break
            except NameError:
                print("please enter a number")

        k = raw_input("what is the new value that you want use?")
        CSVfileControl.update(i, j, k)
    if x == 4:
        print("how many rows do you want to read?")
        y = input()
        CSVfileControl.read_first_x(y)
    if x == 5:
        print("what row do you want to read?")
        y = input()
        CSVfileControl.read_x(y)
    if x == 6:
        print ("enter the fallowing as they come up.")
        a = raw_input("REF_DATE? : ")
        b = raw_input("GEO? : ")
        c = raw_input("DGUID? : ")
        d = raw_input("SEX? : ")
        e = raw_input("Age Group? : ")
        f = raw_input("Student Response? : ")
        g = raw_input("UOM? : ")
        h = raw_input("UOM_ID? : ")
        i = raw_input("SCALAR_FACTOR? : ")
        j = raw_input("SCALAR_ID? : ")
        k = raw_input("VECTOR? : ")
        ll = raw_input("COORDINATE? : ")
        m = raw_input("VALUE? : ")
        n = raw_input("STATUS? : ")
        o = raw_input("SYMBOL? : ")
        p = raw_input("TERMINATED? : ")
        q = raw_input("DECIMALS? : ")
        CSVfileControl.add(
            a, b, c, d, e, f, g, h, i, j, k, ll, m, n, o, p, q
        )
    if x == 7:
        CSVfileControl.load_all_from_csv()
    if x == 8:
        CSVfileControl.persist()
    if x == 9:
        exit()
