#Prompt user to enter their citizenship and age
citizenship = input("Enter Citizenship:")
age = int(input("Enter Age:"))
#check if the user qualifies for voting 
if (citizenship == "Kenyan" or citizenship == "Ugandan" or citizenship == "Tanzanian"and age>=18):
    print("You are eligible to vote!")
else:
    print("You are NOT eligible to vote!")
