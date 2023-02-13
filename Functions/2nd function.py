try:
    def calc_age_months():
        age = int(input("Enter age:"))
        age_months = age * 12
        print(f"You have lived for {age_months} months")

    calc_age_months()
except:
    print("Not a number")
