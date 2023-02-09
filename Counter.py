import datetime
x = datetime.datetime.now()
wday = x.strftime("%j")
day = int(wday)
print("this is the", day, "th day of the year")

if day < 365:
    print("Total to save today is KSH", day)


