citizenship = input("Enter Citizenship:")
age = int(input("Enter Age:"))
if (citizenship == "Kenyan" or citizenship == "Ugandan" or citizenship == "Tanzanian"and age>=18):
    print("You are eligible to vote!")
else:
    print("You are NOT eligible to vote!")