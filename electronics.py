print("Welcome to mystore electronics")
print("Get flat discounts on any electronic product")
x={"smart lcd tv":45000,"refridgerator":60000,"washing machine":20000,"mixer":5000,"water purifier":9999,"AC":60000,"geyser":5500}
amount=0

for i in range(7):
    y=str(input("enter the item you required:"))

    if(y=="smart lcd tv"):
       a=x.get("smart lcd tv")
       print("The cost of smart lcd tv is:",a)
       amount+=a
       print("Do you want to buy more items")
       z=str(input("Enter Yes or NO:"))
       if(z=="yes"):
          continue
       else:
          break
   
    elif(y=="refridgerator"):
       b=x.get("refridgerator")
       print("The cost of refridgerator is:",b)
       amount+=b
       print("Do you want to buy more items")
       z=str(input("Enter Yes or NO:"))
       if(z=="yes"):
          continue
       else:
          break
     

    elif(y=="washing machine"):
       c=x.get("washing machine")
       print("The cost of washing machine is:",c)
       amount+=c
       print("Do you want to buy more items")
       z=str(input("Enter Yes or NO:"))
       if(z=="yes"):
          continue
       else:
          break
     

    elif(y=="mixer"):
      d=x.get("mixer")
      print("The cost of mixer is:",d)
      amount+=d
      print("Do you want to buy more items")
      z=str(input("Enter Yes or NO:"))
      if(z=="yes"):
          continue
      else:
          break
  

    elif(y=="water purifier"):
      e=x.get("water purifier")
      print("The cost of water purifier is:",e)
      amount+=e
      print("Do you want to buy more items")
      z=str(input("Enter Yes or NO:"))
      if(z=="yes"):
          continue
      else:
          break
  

    elif(y=="AC"):
      f=x.get("AC")
      print("The cost of AC is:",f)
      amount+=f
      print("Do you want to buy more items")
      z=str(input("Enter Yes or NO:"))
      if(z=="yes"):
          continue
      else:
          break
    

    else:
       g=x.get("geyser")
       print("The cost of geyser is:",g)
       amount+=g
       print("Do you want to buy more items")
       z=str(input("Enter Yes or NO:"))
       if(z=="yes"):
          continue
       else:
          break
      
print("For electronics purchasing greater then 50000 will get a discount of 30%")
print("For electronics purchasing greater then 80000 will get a discount of 50%")
print("For electronics purchasing greater then 100000 will get a discount of 70%")
sum=amount
print("total cost is",sum)


if(sum>50000 and sum<=80000):
    sum=sum*(1-(30/100))
    print("The total amount you should pay after applying discount",sum)
elif(sum>80001 and sum<=10000):
    sum=sum*(1-(50/100))
    print("The total amount you should pay after applying discount",sum)
elif(sum>10001):
    sum=sum*(1-(70/100))
    print("The total amount you should pay after applying discount",sum)

   



