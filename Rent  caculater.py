##  Input we need from the user
##  Total  rent
##  Total  food ordered for snacking
##  Electricity units spend
##  Charge per unit
 
     ## output
##   total amount you"ve to pay is

rent  =    int(input("Enter your hostel/flat rent =  "))
food  =    int(input("Enter the amount of food ordered =  "))
electricity_spend  = int(input( "Enter the total electricity  spend=  "))
charge_per_unit  =  int(input("Enter the charge pr unit =  "))
person =int(input("Enter the number of person  living in room /flat = "))
    
toatal_bill =  electricity_spend *charge_per_unit

output=(food + rent + toatal_bill)
print("Each person will pay" ,output)
