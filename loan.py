#Get user input for age and income
age=int(input("Enter your age:"))
income=float(input("Enter your annual income in Ksh:"))
#Checks if user qualifies for a loan
if age>=21 and income >=21000:
    print("Congratulations,you qualify for a loan.")
else:
    print("unfortunately, we are unable to offer you a loan at this time.")
