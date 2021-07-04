from datetime import date
def testcal(y, m, d):
    try:
        date (y, m, d)
        return True
    except:
        return False
print (testcal(2021, 2, 29))
