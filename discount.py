print("Welcome to SriSatya grocery store")
print("We are providing huge discounts on this festival sale")
print("Purchasing items above 2000 rupees will get a discount of 10%")
print("Purchasing items above 4000 rupees will get a discount of 15%")
print("Purchasing items above 5000 rupees will get a discount of 20%")
print("These are the items available in our store:\n1.rice \n2.sugar \n3.wheatflour \n4.gramflour \n5.cornflour \n6.salt \n7.oil \n8.almond \n9.cashew \n10.tamarind")
amount=0

for i in range(10):
    x=str(input("Enter the item you want to purchase:"))
    if(x=="rice"):
            print("The cost of ricebag is",1800)
            amount+=1800
            print("Do you want to buy more items")
            z=str(input("Enter Yes or NO:"))
            if(z=="yes"):
              continue
            else:
              break
    elif(x=="sugar"):
            print("The cost of sugar is",45)
            amount+=45
            print("Do you want to buy more items")
            z=str(input("Enter Yes or NO:"))
            if(z=="yes"):
              continue
            else:
              break
    elif(x=="Wheatflour"):
            print("The cost of Wheatflour is",85)
            amount+=85
            print("Do you want to buy more items")
            z=str(input("Enter Yes or NO:"))
            if(z=="yes"):
              continue
            else:
              break
    elif(x=="gramflour"):
            print("The cost of gramflour is",65)
            amount+=65
            print("Do you want to buy more items")
            z=str(input("Enter Yes or NO:"))
            if(z=="yes"):
              continue
            else:
              break
    elif(x=="cornflour"):
            print("The cost of cornflour is",36)
            amount+=36
            print("Do you want to buy more items")
            z=str(input("Enter Yes or NO:"))
            if(z=="yes"):
              continue
            else:
              break
    elif(x=="salt"):
            print("The cost of salt packet is",13)
            amount+=13
            print("Do you want to buy more items")
            z=str(input("Enter Yes or NO:"))
            if(z=="yes"):
              continue
            else:
              break
    elif(x=="oil"):
            print("The cost of Oil packet is",185)
            amount+=185
            print("Do you want to buy more items")
            z=str(input("Enter Yes or NO:"))
            if(z=="yes"):
              continue
            else:
              break
    elif(x=="almond"):
            print("The cost of almond is",800)
            amount+=800
            print("Do you want to buy more items")
            z=str(input("Enter Yes or NO:"))
            if(z=="yes"):
              continue
            else:
              break
    elif(x=="cashew"):
            print("The cost of cashew is",680)
            amount+=680
            print("Do you want to buy more items")
            z=str(input("Enter Yes or NO:"))
            if(z=="yes"):
              continue
            else:
              break
    else:
            print("The cost of tamarind is",115)
            amount+=115
            print("Do you want to buy more items")
            z=str(input("Enter Yes or NO:"))
            if(z=="yes"):
              continue
            else:
              break

sum=amount
print("total cost is",sum)

if(sum>2000 and sum<=4000):
    sum=sum*(1-(10/100))
    print("The total amount you should pay after applying discount",sum)
elif(sum>4001 and sum<=5000):
    sum=sum*(1-(15/100))
    print("The total amount you should pay after applying discount",sum)
elif(sum>5001):
    sum=sum*(1-(20/100))
    print("The total amount you should pay after applying discount",sum)
