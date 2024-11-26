def age():
    try:
        num1 = float(input("Enter your age:"))
        result = num1
        if result > 18:
            raise Exception("Sorry, you are not of age")


    except:
        print("welcome to the system")
age()