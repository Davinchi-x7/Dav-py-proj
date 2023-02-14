class Car():
    def __init__(self, brand, model,body, drivetrain):
        self.brand = brand
        self.model = model
        self.body = body
        self.drivetrain = drivetrain

owner_one = Car("Mercedes-Benz", "S-class 600", "sedan", "AWD")
print(owner_one.brand)
print(owner_one.model)
print(owner_one.body)
print(owner_one.drivetrain)

print("----------End of owner 1------------")

owner_two = Car("BMW", "X7", "SUV", "4WD")
print(owner_two.brand)
print(owner_two.model)
print(owner_two.body)
print(owner_two.drivetrain)

print("---End of owner 2---")

owner_three = Car("Audi", "A8", "Sedan", "AWD")
print(owner_three.brand)
print(owner_three.model)
print(owner_three.body)
print(owner_three.drivetrain)

print("---End of owner 3---")

owner_four = Car("Volkswagen", "Touareg", "SUV", "4WD")
print(owner_four.brand)
print(owner_four.model)
print(owner_four.body)
print(owner_four.drivetrain)