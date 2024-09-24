print("Welcome to SriSatya grocery store")
print("Available items in my store:\n 1.rice \n2.sugar \n3.cornflour \n4.wheatflour \n5.wheat \n6.cashewm \n7.almond")
x={"rice":50,"sugar":35,"cornflour":55,"wheatflour":60,"wheat":70,"cashew":300,"almond":650}
amount=0

for i in range(7):
    y=str(input("enter the item you required:"))

    if(y=="rice"):
       a=x.get("rice")
       print("The cost of onekg rice is:",a)
       amount+=a
       print("Do you want to buy more items")
       z=str(input("Enter Yes or NO:"))
       if(z=="yes"):
          continue
       else:
          break
   
    elif(y=="sugar"):
       b=x.get("sugar")
       print("The cost of onekg sugar is:",b)
       amount+=b
       print("Do you want to buy more items")
       z=str(input("Enter Yes or NO:"))
       if(z=="yes"):
          continue
       else:
          break
     

    elif(y=="cornflour"):
       c=x.get("cornflour")
       print("The cost of onekg cornflour is:",c)
       amount+=c
       print("Do you want to buy more items")
       z=str(input("Enter Yes or NO:"))
       if(z=="yes"):
          continue
       else:
          break
     

    elif(y=="wheatflour"):
      d=x.get("wheatflour")
      print("The cost of onekg wheatflour is:",d)
      amount+=d
      print("Do you want to buy more items")
      z=str(input("Enter Yes or NO:"))
      if(z=="yes"):
          continue
      else:
          break
  

    elif(y=="wheat"):
      e=x.get("wheat")
      print("The cost of onekg wheat is:",e)
      amount+=e
      print("Do you want to buy more items")
      z=str(input("Enter Yes or NO:"))
      if(z=="yes"):
          continue
      else:
          break
  

    elif(y=="cashew"):
      f=x.get("cashew")
      print("The cost of onekg cashew is:",f)
      amount+=f
      print("Do you want to buy more items")
      z=str(input("Enter Yes or NO:"))
      if(z=="yes"):
          continue
      else:
          break
    

    else:
       g=x.get("almond")
       print("The cost of onekg almond is:",g)
       amount+=g
       print("Do you want to buy more items")
       z=str(input("Enter Yes or NO:"))
       if(z=="yes"):
          continue
       else:
          break
      

sum=amount
print("total cost is",sum)

   



