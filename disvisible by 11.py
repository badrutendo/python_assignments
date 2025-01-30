#prompts the user to enter a number 
number=int(input("Enter a number:"))
#check if the number is divisible by 11 
if (number%11 ==0):
    print(str(number) +" is divisible by 11")
else:
    print(str(number) +" is not divisible by 11")
