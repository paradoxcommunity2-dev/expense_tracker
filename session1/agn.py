from datetime import datetime

eletric_bill = float(input("enter the the amount of electric bill paid: "))   #this is the electricity bill
water_bill = float(input("enter the the amount of water bill paid: "))  #this is the water  bill
date_paid = datetime.now().date()  #the date these bills were paid 
total_bill = eletric_bill + water_bill 


print(f"This is the electrical bill {eletric_bill}")
print(f"This is the electrical bill {water_bill}")
print(f"The total amount paid is {total_bill}rwf paid at {date_paid}")

