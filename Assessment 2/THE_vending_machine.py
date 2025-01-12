balance = 0

#These dictionaries hold the contents of the products that would be displayed on the page
page1 = [ #Page 1's products
    {
        "ITEMID": 0,
        "ITEMNAME": "SigmaBar",
        'ITEMPRICE': 5,
    },{
        "ITEMID": 1,
        "ITEMNAME": "US Military Military Energy Gum",
        'ITEMPRICE': 35,
    },{
        "ITEMID": 2,
        "ITEMNAME": "SlimJim",
        'ITEMPRICE': 3,
    },{
        "ITEMID": 3,
        "ITEMNAME": "Mars Bar",
        'ITEMPRICE': 2,
    },{
        "ITEMID": 4,
        "ITEMNAME": "Lays Chips",
        'ITEMPRICE': 10,
    },
]
page2 = [ #Page 2's products
    {
        "ITEMID": 0,
        "ITEMNAME": "Rotisserie Chicken",
        'ITEMPRICE': 25,
    },{
        "ITEMID": 1,
        "ITEMNAME": "Lasagna",
        'ITEMPRICE': 25,
    },{
        "ITEMID": 2,
        "ITEMNAME": "12 inch Cheese Pizza",
        'ITEMPRICE': 30,
    },{
        "ITEMID": 3,
        "ITEMNAME": "12 PCs. Fried Chicken Bucket",
        'ITEMPRICE': 35,
    },{
        "ITEMID": 4,
        "ITEMNAME": "Microwavable Salisbury Steak",
        'ITEMPRICE': 15,
    },
]
page3 = [ #Page 3's products
    {
        "ITEMID": 0,
        "ITEMNAME": "Coca Cola",
        'ITEMPRICE': 2,
    },{
        "ITEMID": 1,
        "ITEMNAME": "Root Beer",
        'ITEMPRICE': 2,
    },{
        "ITEMID": 2,
        "ITEMNAME": "Water",
        'ITEMPRICE': 1,
    },{
        "ITEMID": 3,
        "ITEMNAME": "Bottled Milkshake",
        'ITEMPRICE': 67,
    },{
        "ITEMID": 4,
        "ITEMNAME": "Iced Frappe",
        'ITEMPRICE': 100,
    },
]
page4 = [ #Page 4's products
    {
        "ITEMID": 0,
        "ITEMNAME": "Coffee",
        'ITEMPRICE': 3,
    },{
        "ITEMID": 1,
        "ITEMNAME": "Tea",
        'ITEMPRICE': 3,
    },{
        "ITEMID": 2,
        "ITEMNAME": "Karak Chai",
        'ITEMPRICE': 1,
    },{
        "ITEMID": 3,
        "ITEMNAME": "Green Tea",
        'ITEMPRICE': 2,
    },{
        "ITEMID": 4,
        "ITEMNAME": "Hot Chocolate",
        'ITEMPRICE': 3,
    },
]
page5 = [ #Page 5's products
    {
        "ITEMID": 0,
        "ITEMNAME": "Sigma's Vanilla Ice Popsicle",
        'ITEMPRICE': 5,
    },{
        "ITEMID": 1,
        "ITEMNAME": "Butterscotch Ice Cone",
        'ITEMPRICE': 3,
    },{
        "ITEMID": 2,
        "ITEMNAME": "Sponge Man Ice Cone",
        'ITEMPRICE': 4,
    },{
        "ITEMID": 3,
        "ITEMNAME": "Ice Cream Sandwich",
        'ITEMPRICE': 5,
    },{
        "ITEMID": 4,
        "ITEMNAME": "Juice Cold Stick",
        'ITEMPRICE': 3,
    },
]
 
item = []
#Holds the layout of the receipt
receipt = """
\t--------- RECEIPT ---------- 
"""
run = True

#These functions hold the purchasing process of each items, they are all essentially the same except their
#Functions are intended for the different pages the vending machine offers.
def PAGE1PURCHASE(page1, run, item):
    cou = 0
    selection = str(input("Do you wish to purchase an item or change page (item/change): \n")) #This is an input script that asks if you wish to change the page or buy an item
    sel = selection.lower() #Sets the input above in lowercase for easier registering by the code
    if sel == "item": #If the user has given "item", in the input above then it proceeds with the purchasing
        while run: 
            purchaseit = int(input("\nEnter Item ID: ")) #The input for the item ID
            if purchaseit < len(page1):
                item.append(page1[purchaseit]) 
            else:
                print("INVALID ITEM ID") #Returns if the item id is false
            moreit = str(input("\nPurchase additional items? (Y/N)\n")) #The command will ask if you wish to purchase another item
            low = moreit.lower() #Sets the input above in lowercase for easier registering by the code
            if low == "n": 
                run = False  #If the user doesnt wish to purchase more, it will nullify the loop and proceed to receipt or sum
        receiptv = input(("\nReceipt or Total Sum (R/S): \n")) #Gives the user a choice whether to be given the receipt or the total sum from the transaction
        dec = receiptv.lower()
        if dec == "r":
            for i in item:
                if i['ITEMPRICE'] > balance:
                    cou = cou + 1 #This is a counter for ensuring the purchased items are atleast within the given budget's range. If it exceeds then this goes into work
                else:
                    print(creceipt(item, receipt)) # If there are sufficient funds then it returns the receipt and sum.
        if cou > 0: # If the purchase exceeds the budget then it prints "INSUFFICIENT FUNDS" and doesnt allow to show the receipt or sum.
            print ("INSUFFICIENT FUNDS")
        elif dec == "s":
            for i in item:
                if i['ITEMPRICE'] > balance:
                    cou = cou + 1
                else:
                    print(sumitall(item))
        if cou > 0:
            print ("INSUFFICIENT FUNDS")
    else:
        pageselection()
        
def PAGE2PURCHASE(page2, run, item):
    cou = 0
    selection = str(input("Do you wish to purchase an item or change page (item/change): \n"))
    sel = selection.lower()
    if sel == "item":
        while run:
            purchaseit = int(input("\nEnter Item ID: "))
            if purchaseit < len(page2):
                item.append(page2[purchaseit])
            else:
                print("INVALID ITEM ID")
            moreit = str(input("\nPurchase additional items? (Y/N)\n"))
            low = moreit.lower()
            if low == "n":
                run = False
        receiptv = input(("\nReceipt or Total Sum (R/S): \n"))
        dec = receiptv.lower()
        if dec == "r":
            for i in item:
                if i['ITEMPRICE'] > balance:
                    cou = cou + 1
                else:
                     print(creceipt(item, receipt))
        if cou > 0:
            print ("INSUFFICIENT FUNDS")
        elif dec == "s":
            for i in item:
                if i['ITEMPRICE'] > balance:
                    cou = cou + 1
                else:
                    print(sumitall(item))
        if cou > 0:
            print ("INSUFFICIENT FUNDS")
    else:
        pageselection()
        
def PAGE3PURCHASE(page3, run, item):
    cou = 0
    selection = str(input("Do you wish to purchase an item or change page (item/change): \n"))
    sel = selection.lower()
    if sel == "item":
        while run:
            purchaseit = int(input("\nEnter Item ID: "))
            if purchaseit < len(page3):
                item.append(page3[purchaseit])
            else:
                print("INVALID ITEM ID")
            moreit = str(input("\nPurchase additional items? (Y/N)\n"))
            low = moreit.lower()
            if low == "n":
                run = False
        receiptv = input(("\nReceipt or Total Sum (R/S): \n"))
        dec = receiptv.lower()
        if dec == "r":
            for i in item:
                if i['ITEMPRICE'] > balance:
                    cou = cou + 1
                else:
                     print(creceipt(item, receipt))
        if cou > 0:
            print ("INSUFFICIENT FUNDS")
        elif dec == "s":
            for i in item:
                if i['ITEMPRICE'] > balance:
                    cou = cou + 1
                else:
                    print(sumitall(item))
        if cou > 0:
            print ("INSUFFICIENT FUNDS")
    else:
        pageselection()
        
def PAGE4PURCHASE(page4, run, item):
    cou = 0
    selection = str(input("Do you wish to purchase an item or change page (item/change): \n"))
    sel = selection.lower()
    if sel == "item":
        while run:
            purchaseit = int(input("\nEnter Item ID: "))
            if purchaseit < len(page4):
                item.append(page4[purchaseit])
            else:
                print("INVALID ITEM ID")
            moreit = str(input("\nPurchase additional items? (Y/N)\n"))
            low = moreit.lower()
            if low == "n":
                run = False
        receiptv = input(("\nReceipt or Total Sum (R/S): \n"))
        dec = receiptv.lower()
        if dec == "r":
            for i in item:
                if i['ITEMPRICE'] > balance:
                    cou = cou + 1
                else:
                     print(creceipt(item, receipt))
        if cou > 0:
            print ("INSUFFICIENT FUNDS")
        elif dec == "s":
            for i in item:
                if i['ITEMPRICE'] > balance:
                    cou = cou + 1
                else:
                    print(sumitall(item))
        if cou > 0:
            print ("INSUFFICIENT FUNDS")
    else:
        pageselection()
        
def PAGE5PURCHASE(page5, run, item):
    cou = 0
    selection = str(input("Do you wish to purchase an item or change page (item/change): \n"))
    sel = selection.lower()
    if sel == "item":
        while run:
            purchaseit = int(input("\nEnter Item ID: "))
            if purchaseit < len(page5):
                item.append(page5[purchaseit])
            else:
                print("INVALID ITEM ID")
            moreit = str(input("\nPurchase additional items? (Y/N)\n"))
            low = moreit.lower()
            if low == "n":
                run = False
        receiptv = input(("\nReceipt or Total Sum (R/S): \n"))
        dec = receiptv.lower()
        if dec == "r":
            for i in item:
                if i['ITEMPRICE'] > balance:
                    cou = cou + 1
                else:
                     print(creceipt(item, receipt))
        if cou > 0:
            print ("INSUFFICIENT FUNDS")
        elif dec == "s":
            for i in item:
                if i['ITEMPRICE'] > balance:
                    cou = cou + 1
                else:
                    print(sumitall(item))
        if cou > 0:
            print ("INSUFFICIENT FUNDS")
    else:
        pageselection()

def sumitall(item): # This is the function for the sum of the purchase.
    sumitall = 0
    for i in item:
        sumitall += i["ITEMPRICE"] # How it works is it retrieves the price of the selected items from the dictionary.
    return sumitall                # It stacks depending on the amount of items purchased.

def creceipt(item, receipt): # This function is for the receipt
    for i in item: # This holds the whole layout of the receipt that would include all the purchased items
        receipt += f""" 
         \tITEM ID [{i["ITEMID"]}] - [ {i["ITEMNAME"]} -- {i['ITEMPRICE']} Credit(s) ]
        """
    receipt += f"""
        \tTOTAL PAYMENT --- {sumitall(item)} Credit(s) 
        
        You Currently have {balance - sumitall(item)} Credit(s)
       """
    return receipt #The features of the receipt includes the total payment and the balance you have left after the purchase.

def pageselection(): #This function holds the code for when the user selects a page.
   print ("""
\n[ -------------- [ PAGE  SELECTION ] -------------- ]
[  [PAGE 1] - Light Snacks -                        ]
[  [PAGE 2] - Readymade Meals -                     ]
[  [PAGE 3] - Cold Drinks -                         ]
[  [PAGE 4] - Hot Drinks -                          ]
[  [PAGE 5] - Dessert Snacks -                      ]
   """)       
   paslect = int(input("\n ---------- [ Select which page do you wish to change to: (1/2/3/4/5) ] ---------- \n")) #This is an input code for which page the user desires to change to
   if paslect == 1: # The following will show up depending on the user's choice. for example, if they select page 1 then this part of the if statement below triggers.
      print ("\n[ -------------- PAGE 1 = LIGHT SNACKS -------------- ]")
      for i in page1:
          print(
              f"\n[ [ITEM ID]: {i['ITEMID']}     [ITEM]: {i['ITEMNAME']}     [COST]: {i['ITEMPRICE']} Credit(s) ]") #The layout for the page
      PAGE1PURCHASE(page1, run, item) #The function that calls the page's purchasing process.
   elif paslect == 2:
      print ("\n[ -------------- PAGE 2 = READYMADE MEALS -------------- ]")
      for i in page2:
          print(
              f"\n[ [ITEM ID]: {i['ITEMID']}     [ITEM]: {i['ITEMNAME']}     [COST]: {i['ITEMPRICE']} Credit(s) ]")
      PAGE2PURCHASE(page2, run, item)
   elif paslect == 3:
      print ("\n[ -------------- PAGE 3 = COLD DRINKS -------------- ]")
      for i in page3:
          print(
              f"\n[ [ITEM ID]: {i['ITEMID']}     [ITEM]: {i['ITEMNAME']}     [COST]: {i['ITEMPRICE']} Credit(s) ]")
      PAGE3PURCHASE(page3, run, item)
   elif paslect == 4:
      print ("\n[ -------------- PAGE 4 = HOT DRINKS -------------- ]")
      for i in page4:
          print(
              f"\n[ [ITEM ID]: {i['ITEMID']}     [ITEM]: {i['ITEMNAME']}     [COST]: {i['ITEMPRICE']} Credit(s) ]")
      PAGE4PURCHASE(page4, run, item)
   elif paslect == 5:
      print ("\n[ -------------- PAGE 5 = DESSERT SNACKS -------------- ]")
      for i in page5:
          print(
              f"\n[ [ITEM ID]: {i['ITEMID']}     [ITEM]: {i['ITEMNAME']}     [COST]: {i['ITEMPRICE']} Credit(s) ]")
      PAGE5PURCHASE(page5, run, item)
   else:
      print ("Invalid") 

try: #This is the code that will ask for the user's budget, with a maximum.
    balinput = int(input("Insert your Budget (MAX. 2750)\n")) #balance input
    while balinput > 2750:
        print ("The amount inputted exceeds the limit.") #If the user inputs the maximum, it results in a while loop until the sufficient amount is given.
        balinput = int(input("Insert your Budget (MAX. 2750)\n"))
    else:
        print ("\n--------------- Welcome to THE Vending Machine! --------------- \n\n\tWe have a wide array of refreshments!") #else, if the sufficient amount is indeed given
        print ("\n[ -------------- PAGE 1 = LIGHT SNACKS -------------- ]")                                                     #it will proceed and defaults to page 1's contents
        for i in page1:
            print(
            f"\n[ [ITEM ID]: {i['ITEMID']}     [ITEM]: {i['ITEMNAME']}     [COST]: {i['ITEMPRICE']} Credits ]") #prints the layout for page 1's contents
    
        balance = balinput #this will hold the inputted budget's value
        print (f"\n\tYour balance is currently {balance} Credits")
        print ("\n[--------------- Select your Refreshments! ---------------] ")
        PAGE1PURCHASE(page1, run, item)     #calls the function for page 1's purchasing process.
except ValueError:
    print ("Invalid value, insert an integer.") #This is an error failsafe code that resorts to printing this instead of a python error.