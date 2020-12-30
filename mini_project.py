#Importing the necessary library
import datetime

addHour=int(input("Enter the hour for the alarm to be set"))
addMinute=int(input("Enter the minute for the alarm to be set"))
amPm= str(input("Is the time am or pm?"))

if(amPm=="pm"):
   addHour=addHour+12

while(1==1):
    if(addHour==datetime.datetime.now().hour and
       addMinute==datetime.datetime.now().minute):
         print("Wake up...it's time")
         break
#checking if the time matches with that of the computer
print("Thank you!!Hope you liked it")


         
   

