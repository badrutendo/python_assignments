#electricity bill
#prompt user for input
customer_id=input("Enter Customer ID:")
customer_name=input("Enter Customer Name:")
units_consumed=float(input("Enter Units Consumed:"))
#determine charge per unit
if units_consumed<=199:
    charge_per_unit=1.20
elif 200 <=units_consumed<400:
    charge_per_unit=1.50
elif 400<=units_consumed<600:
    charge_per_unit=1.80
else:
    charge_per_unit=2.00
#calculate total bill before surcharge
total_bill=units_consumed*charge_per_unit
#if it exceeds 400
if total_bill>400:
  surcharge=total_bill*0.5
  total_bill+=surcharge
else:
    surcharge=0
#ensure minimum bill is kshs.100
if total_bill<100:
    total_bill=100

#display the bill details
print("\nElecricity bill")
print("Customer ID        :",customer_id)
print("Customer Name      :",customer_name)
print("Units Consumed     :",round(units_consumed,2))
print("Charge per unit    :kshs.",round(charge_per_unit,2))
print("Surcharge          :kshs.",round(surcharge,2))
print("Total Amount to pay:kshs.",round(total_bill,2))
