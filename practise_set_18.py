# Python practise 18 (Medium - From codewithharry) - Water Reminder Notification

"""
Water Reminder Notification

Created the python program that will Notifide us as per the calculation of 3.5 Liter to drink water per day
Use time module and also plyer for notification
"""

# Author = Abhinav
# Date = 24 April 2021
# Motive = Just for the python practise to not just learn python also to expert it

import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "**Please Drink Water Now!!",
            message ="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = r"E:\ADMIN\Pictures\Saved Pictures\drinkwater.ico",
            timeout= 10
            )
        time.sleep(60*60)