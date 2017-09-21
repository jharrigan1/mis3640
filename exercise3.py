#exercise 3#

import time
print(time.time())
current = time.time()
second = current % 60
minutes = (current//60) % 60
hours = (current//60)//60 % 24
days = current// 60 //60 //24 
print("Current time: %d days, %d hours, %d minutes, %d seconds from Epoch." % (days, hours, minutes, second))