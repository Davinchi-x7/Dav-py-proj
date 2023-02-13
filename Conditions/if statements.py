number = int(input("Ener pompt commnad:"))
if number == 544:
    print("Select desired plan:")
    print("1: Daily bundles")
    print("2: Data deals")
    print("3: Tunukiwa")
    print("4: fuliza")
    print("5: Mpesa")
else:
    print("invalid entry please try again")

num = int(input("Select plan:"))
if num == 1:
    print("You have selected daily bundles")
elif num == 2:
    print("You have selected data deals")
elif num == 3:
    print("You have selected Tunukiwa")
elif num == 4:
    print("You have selected fuliza")
elif num == 5:
    print("You have selected Mpesa")
else:
    print("invalid entry please try again")

