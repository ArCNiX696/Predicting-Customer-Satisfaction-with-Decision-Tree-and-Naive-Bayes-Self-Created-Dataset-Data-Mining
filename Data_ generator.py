import os
import pandas as pd
import random

# Create a list of items for the dataframe

items_list = [
    "T-shirt", "Jeans", "Sneakers", "Wristwatch", "Video Game", 
    "Pizza", "Burger", "Apple", "Tacos", "Toothpaste",
    "Shampoo", "Socks", "Jacket", "Dress", "Boots",
    "Baseball Cap", "Sunglasses", "Backpack", "Belt", "Scarf",
    "Laptop", "Smartphone", "Headphones", "Book", "Chair",
    "Table", "Lamp", "Bedding Set", "Towel", "Curtains",
    "Blender", "Microwave", "Frying Pan", "Plate", "Mug",
    "Yogurt", "Cheese", "Milk", "Bread", "Eggs",
    "Chicken", "Beef", "Fish", "Rice", "Pasta",
    "Notebook", "Pen", "Pencil", "Eraser", "Ruler"
]

#Assign a price to each item
item_price={"T-shirt":100, "Jeans":150, "Sneakers":1800, "Wristwatch":2700, "Video Game":1100, 
    "Pizza":300, "Burger":250, "Apple":30, "Tacos":150, "Toothpaste":120,
    "Shampoo":250, "Socks":55, "Jacket":130, "Dress":150, "Boots":2000,
    "Baseball Cap":120, "Sunglasses":130, "Backpack":140, "Belt":100, "Scarf":110,
    "Laptop":25000, "Smartphone":20000, "Headphones":2000, "Book":700, "Chair":2200,
    "Table":3400, "Lamp":900, "Bedding Set":2800, "Towel":180, "Curtains":1500,
    "Blender":2100, "Microwave":4000, "Frying Pan":1200, "Plate":200, "Mug":100,
    "Yogurt":150, "Cheese":160, "Milk":110, "Bread":80, "Eggs":90,
    "Chicken":90, "Beef":200, "Fish":150, "Rice":170, "Pasta":230,
    "Notebook":70, "Pen":30, "Pencil":35, "Eraser":45, "Ruler":100}

# Create a list of random items from the items list up to 995 items
random_items=[random.choice(items_list)for _  in range(994)]

# Create a list of prices for the random items
Prices=[]

#Iterate over the random items and assign a price to each item
for item in random_items:
    price=item_price[item]
    random_price=random.random()

    #increase the price by 30% with a 30% or less of probability , in order to create Absolutely-Right Rules 
    if random_price <0.30:
        price=price*1.30
    #decrease the price by 30% with 25% or less of probability, in order to create Absolutely-Right Rules
    elif 40<random_price<0.55:
        price=price*0.70
    
    else:
        price=price

    Prices.append(price)

# Create a list of time waiting in the queue for each item
#this will be related to Satisfaction
#in the case that the time in the queue is too long, the customer will be unsatisfied
#I adjust that posibility to 50% or less of the cases
Time_waiting=[]

for time in range(len(random_items)):
    if random.random()<0.50:
        Time_waiting.append(1)#this means that the time was really long
    else:
        Time_waiting.append(0)#this indicates that the customer didn't wait too much

'''
#NOT NOISE
#create a list of custumer service
#if the custumer service is bad, the customer will be unsatisfied (0)
#if the custumer service is good, the customer will be satisfied (1)
custumer_service=[]

for service in range(len(random_items)):
    if random.random()<0.50:
        custumer_service.append(0)#this means that the custumer service was bad
    else:
        custumer_service.append(1)#this indicates that the custumer service was good
'''
#NOISE
#I create a Noise feature , that will affect cashier mood so it will affect the service quality

Cashier_mood=[]
for mood in range(len(random_items)):
    if random.random()<0.10:
        Cashier_mood.append(1)#this means that the cashier was in a good mood only 10% of the time
    else:
        Cashier_mood.append(0)#this indicates that the cashier was in a bad mood


#create a list of custumer service
#if the custumer service is bad, the customer will be unsatisfied (0)
#if the custumer service is good, the customer will be satisfied (1)
custumer_service=[]

for service in range(len(random_items)):
    cashier_s=Cashier_mood[service]#we get the cashier mood from the list of cashier mood

    if cashier_s==1 :
        custumer_service.append(1)

    else:   
        custumer_service.append(0)


#NOISE
#I decided to add another Noise feature , which will affect the mood feature in order to see how the model accuracy is affected
#Create a list of weather
Weather=[]

for weather in range(len(random_items)):
    Weather.append(1 if random.random() < 0.10 else 0)


Mood=[]

for mood in range(len(random_items)):
    weather_s=Weather[mood]#we get the weather from the list of weather

    if weather_s==1 :
        Mood.append(1)

    else:
        Mood.append(0)

    

'''

#WITHOUT NOISE
#create a list of moods
#this represents the mood of the customer
#if the mood is bad so it is (0), that will happens only 30% or less of the times, if the mood is good is (1)
Mood=[]

for mood in range(len(random_items)):
    if random.random()<0.30:
        Mood.append(0)#this means that the custumer was in a bad mood
    else:
        Mood.append(1)#this indicates that the custumer was in a good mood
'''


#this represents the enviroment in the store
#this will be related to Satisfaction
#in the real world, the environment in the store is very important
#so if the environment is bad, the customer will be unsatisfied (0)
#otherwise, the customer will be satisfied (1)

Good_enviroment=[]

for noise in range(len(random_items)):
    if random.random()<0.40:
        Good_enviroment.append(0)#this means that the environment was bad
    else:
        Good_enviroment.append(1)#this indicates that the environment was good

#First Redundant Feature
#Payment Method
#Create a list of payment methods
payment_method=[]

#Iterate over the random items total of 994 items
for payment in range(len(random_items)):
    if random.random()<0.7:  #70% of the time the payment method is credit card
        payment_method.append(1)#credit card=1
    else:
        #30% of the time the payment method is cash
        payment_method.append(0) #cash=0

#Second Redundant Feature
#Casier gender list
cashier_gender=[]

#Iterate over the random items total of 994 items
for cashier in range(len(random_items)): 
    if random.random()<0.5:#The 50% of the purchase will be attended by a male cashier
        cashier_gender.append(1) #male=1

    else:
        ##The 50% of the purchase will be attended by a female cashier
        cashier_gender.append(0) #female=0

#Third Redundant Feature
#Hungry? create a column with a really redundant feature, if the customer is hungry or not
#since normally being hungry has nothing to do with the purchase, it is a random feature so it is redundant
#Create a list of hungry
hungry=[]
#Iterate over the random items total of 994 items
for hunger in range(len(random_items)):
    if random.random()<0.2: #20% of the time the customer is hungry
        hungry.append(1) #hungry=1
    else:
        hungry.append(0) #not hungry=0


'''
Absolutely Right Rules
•	If the item price is  higher than the original price, the possibility of unsatisfaction will increase, in the other hand if the price is less or equal to the original price , the chance of satisfaction increase. 
•	If the customer does not need to wait for a long time in the queue, this may increase the chance of satisfaction if is related with other positive Absolutely Rules like the first one , otherwise the satisfaction may be (0)Unsatisfied.  
•	If the costumer service is good and also this rule is combined with other positive Absolutely Rules, the satisfaction will be positive (1), otherwise will be (0)Unsatisfied. 
•	If the costumer mood is good , and this rule is combined with other positive Absolutely Rules, the satisfaction will be positive (1), otherwise will be (0)Unsatisfied.
•	If the environment of the store is good, and this rule is combined with other positive Absolutely Rules the satisfaction will be positive (1), otherwise will be (0)Unsatisfied.

'''



satisfaction=[]

for i in range(len(random_items)):
    price_s=Prices[i]#we get the price from the list of prices in which 50% of the prices are increased by 30%
    item_s=random_items[i]#we get the item from the list of random items
    normal_price=item_price[item_s]#we get the normal price from the dictionary
    time_s=Time_waiting[i]#we get the time from the list of times
    service_s=custumer_service[i]#we get the custumer service from the list of custumer service
    mood_s=Mood[i]#we get the mood from the list of moods
    enviroment_s=Good_enviroment[i]#we get the enviroment from the list of enviroments


    if price_s<=normal_price and time_s==1 and service_s==1:
        satisfaction.append(1)
    
    elif price_s<=normal_price and mood_s==1 and enviroment_s==1 :
        satisfaction.append(1)
    
    elif mood_s==1 and price_s<=normal_price and time_s==1  :
        satisfaction.append(1)

    elif service_s==1 and mood_s==1 and price_s<=normal_price :
        satisfaction.append(1)

    elif enviroment_s==1 and  price_s<=normal_price and time_s==1:
        satisfaction.append(1)

    else:
        satisfaction.append(0)
    
# Create a dataframe from the list of items
df=pd.DataFrame({"Items":random_items,"Price":Prices})

df["Time Waiting"]=Time_waiting

df["Custumer Service"]=custumer_service

#NOISE
df["Weather"]=Weather
#NOISE
df["Cashier Mood"]=Cashier_mood

df["Mood"]=Mood

df["Good Enviroment"]=Good_enviroment

df["Payment Method"]=payment_method

df["Cashier Gender"]=cashier_gender

df["Hungry?"]=hungry

df["Satisfaction"]=satisfaction

#NOISE
file_name='Satisfaction_noise.csv'

#NOT NOISE
#file_name='Satisfaction_not_noise.csv'

#Verify if the folder exists, if not create it
if not os.path.exists("Data"):
    os.mkdir("Data")

else:
    path=os.path.join(".","Data",file_name)


# Save the dataframe to a csv file
df.to_csv(path,index=False)
