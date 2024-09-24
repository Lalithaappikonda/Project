
username="lalitha"
password="601191"
Total=10000
x=str(input("enter the username:"))
y=str(input("enter the password:"))

if(x==username and y==password):
    print("1.desposite \n2.withdraw\n3.verify bank balance\n4.Any Query")
    z=int(input("Enter the option which you want to know:"))
    if(z==1):
       a=int(input("enter the amount you want to deposite:"))
       Total+=a
       print("Total amount in your bank :",Total)

    elif(z==2):
       a=int(input("enter the amount you want to withdraw:"))
       Total-=a
       print("Total amount in your bank :",Total)

    elif(z==3):
       print("Total amount in your account:",Total)

    else:
       print("Contact to your nearest bank brach")

else:
   print("Invalid username and password")


        