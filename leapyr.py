print("Hello this is a Leap Year Determiner.")
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That is a leap year.")
        else:
            print("That is not a leap year.")
    else:
        print("That is a leap year.")
else: 
    print("That is not a leap year.")