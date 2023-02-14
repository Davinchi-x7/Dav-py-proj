num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second Number:"))

for number in range(num1,num2):
    if(number%3==0 and number%5==0):
        print(f"{number}:FizzBuzz")
    elif(number%3 ==0):
        print(f"{number}:Fizz")
    elif(number%5==0):
        print(f"{number}buzz")
    else:
        print(number)