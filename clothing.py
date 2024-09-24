print("Welcome to KLM shopping Mall")
print("Mens,Womens,Kids")
a=["Mens,Womens,Kids"]
sum=0
m=["Jeans,Shirts,Tshirts,Trousers,Shorts"]
w=["Jeans,Tops,kurthis,duppatas,Shirts,Nightwares"]
k=["frocks,shirts,Tshirts,Jeans,nightware"]
print("Menswear:",m)
print("Womenswear:",w)
print("Kidswear:",k)
x=str(input("Enter the catogery you required:"))
for i in range(5):
   if(x=="mens"): 
        c=int(input("Mention how many items you want to purchase in menswear:"))
        for j in range(c):
           print("Select the reuired items from Menswear")
           y=str(input("Enter the iteam from Menswear:"))
           if(y=="jean"):
             print("The cost of jean is",800)
             sum+=800
           elif(y=="shirt"):
             print("The cost of Shirt is",700)
             sum+=700
           elif(y=="Tshirt"):
             print("The cost of TShirt is",400)
             sum+=400
           elif(y=="trousers"):
             print("The cost of Trousers is",900)
             sum+=900
           elif(y=="shorts"):
             print("The cost of Shorts is",300)
             sum+=300
           else:
             print("Item not recognized. Please try again.")


amount=sum
print("total amount to be paid:",amount)

             
x=str(input("Enter the catogery you required:"))
for i in range(6):
   if(x=="women"): 
        c=int(input("Mention how many items you want to purchase in womenswear:"))
        for j in range(c):
          print("Select the reuired item from womenswear")
          y=str(input("Enter the iteam from womenswear:"))
          if(y=="Jean"):
            print("The cost of jean is",800)
            sum+=800
          elif(y=="tops"):
            print("The cost of tops is",500)
            sum+=500
          elif(y=="kurthis"):
            print("The cost of kurthis is",1200)
            sum+=1200
          elif(y=="duppatas"):
            print("The cost of duppatas is",200)
            sum+=200
          elif(y=="shirts"):
            print("The cost of Shirts is",500)
            sum+=500
          elif(y=="nightware"):
            print("The cost of nightware is",450)
            sum+=450
          else:
            print("Item not recognized. Please try again.")

amount=sum
print("total amount to be paid:",amount)

x=str(input("Enter the catogery you required:"))
for i in range(5):
   if(x=="kids"):
        c=int(input("Mention how many items you want to purchase in kidswear:"))
        for j in range(c):
           print("Select the reuired item from kidswear")
           y=str(input("Enter the iteam from kidswear:"))
           if(y=="frock"):
             print("The cost of frock is",750)
             sum+=750
           elif(y=="shirt"):
            print("The cost of shirt is",500)
            sum+=500
           elif(y=="Tshirt"):
            print("The cost of Tshirt is",600)
            sum+=600
           elif(y=="jean"):
            print("The cost of jean is",700)
            sum+=700
           elif(y=="nightware"):
            print("The cost of nightware is",400)
            sum+=400
           else:
            print("Item not recognized. Please try again.")
      
amount=sum
print("total amount to be paid:",amount)



