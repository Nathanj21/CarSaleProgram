price = input("do you like cars? \n")
if price == "yes":
    print("yay!")
else:
    print("understood")

MP = input("what is your max price? \n")

price1 = 10000
car1 = "car 310: 2006 mustang. price is 10,000"
price2 = 15000
car2 = "car 449: 2011 odyssey. Price is 15,000"
price3 = 40000
car3 = "car 000: 2020 Tesla model y. price is 40,000"
if int(MP) > 10000:
    print(car1)
if int(MP) > 15000:
    print(car2)
if int(MP) > 40000:
    print(car3)

selection = input("which car do you want? enter the car's number \n")
if selection == "310":
    print("great! we will get the mustang ready for you.")
elif selection == "449":
    print("great! we will get the odyssey ready for you.")
elif selection == "000":
    print(" great! we will get the tesla ready for you.")
