import datetime
x = datetime.datetime.now()
day = x.strftime("%j")
print("this is the", day, "th day of the year")

while day < 365:
    print("Total to save today is KSH", day)


