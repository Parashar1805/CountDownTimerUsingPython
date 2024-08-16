# import the time module
import time
import datetime
import keyboard 
# input time in hours, minutes & seconds 
h = int(input("Enter the time in hours: "))
m = int(input("Enter the time in minutes: "))
s = int(input("Enter the time in seconds: "))
t = h*3600 + m*60 + s
# while loop for countdown 
while t>0:
 timer = datetime.timedelta(seconds = t)
 print(timer, end="\r")
 if keyboard.is_pressed('space'):
   break
 time.sleep(1)
 t -= 1
 
# to display 'times up' message
for i in range(5,0,-1):
 print('TIMES UP', end='\r')
 time.sleep(.5)
 print(' ', end='\r')
 time.sleep(.5) 
 print('TIMES UP', end='\r')
