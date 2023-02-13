import datetime
x = datetime.datetime.now()
wyear = x.strftime("%y")

wday = x.strftime("%j")
day = int(wday)
print(f"this is the {day}th day of the year {wyear}")
def calc():
    sav = day / 2*(2 + (day - 1) * 1)
    print(f"Total savings till today is KSH {sav}")


if day < 365:
    print(f"Total to save today is KSH {day}")
    calc()

