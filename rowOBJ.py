"""
Name: Liam Hovey
SN: 040774944
Exercise 3
"""


class RowObj:
    """all objects will be created with all of the attributes found in a row"""

    def __init__(self, ref_date, geo, dguid, sex, age, student, uom, uom_id, factor, scalar_id, vector, coord, value, stat,
                 sym, terminated, decimals):
        self.REF_DATE = ref_date
        self.GEO = geo
        self.DGUID = dguid
        self.SEX = sex
        self.AGE = age
        self.STUDENT = student
        self.UOM = uom
        self.UOM_ID = uom_id
        self.SCALAR_FACTOR = factor
        self.SCALAR_ID = scalar_id
        self.VECTOR = vector
        self.COORDINATE = coord
        self.VALUE = value
        self.STATUS = stat
        self.SYMBOL = sym
        self.TERMINATED = terminated
        self.DECIMALS = decimals
    """toString method equivalent in python"""

    def __str__(self):
        return self.REF_DATE + ", " + self.GEO + self.DGUID + ", " + self.SEX + ", " + self.AGE + ", " + self.STUDENT +\
               ", " + self.UOM + ", " + self.UOM_ID + ", " + self.SCALAR_FACTOR + ", " + self.SCALAR_ID + ", " + \
               self.VECTOR + ", " + self.COORDINATE + ", " + self.VALUE + ", " + self.STATUS + ", " + self.SYMBOL + \
               ", " + self.TERMINATED + ", " + self.DECIMALS
