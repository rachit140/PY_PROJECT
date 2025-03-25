#Program to FIND Average temp. of weak 
#by rachit sharma on 14.03.2023
from statistics import mean
monday = float(input("enter monday Temperature"))
tuesday = float(input("enter tuesday Temperature"))
wednesday = float(input("enter wednesday Temperature"))
thrusday = float(input("enter thrusday Temperature"))
friday = float(input("enter friday Temperature"))
saturday = float(input("enter saturday Temperature"))
sunday = float(input("enter sunday Temperature"))
#NOW AVERAGE TEMP. OF WEEK IS HERE!
Average_temperature = (monday+tuesday+wednesday+thrusday+friday+saturday+sunday)/7
print ("Average temperature:",Average_temperature)
