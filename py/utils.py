from texttable import Texttable
import random
import string

def printTable(rows):
    t = Texttable()
    t.add_rows(rows)
    print(t.draw())

def generateRandomId(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))