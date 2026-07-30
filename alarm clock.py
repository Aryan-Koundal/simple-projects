import datetime
import time
import winsound
print ("Entre alarm time")
while True :
  hour = int(input("Entre hours : (HH)"))
  if (0<=hour<=23):
    break
  print ("invalid hours")
while True :
 minutes = int (input("Entre minutes : (MM)"))
 if (0<=minutes<=59):
   break
 print ("invalid minutes")
while True:
   seconds = int(input ("Entre seconds : (SS)"))
   if (0<=seconds<=59):
     break
   print ("invalid seconds")
alarm_time = f"{hour:02}:{minutes:02}:{seconds:02}"
while True :
   now = datetime.datetime.now()
   now = now.strftime("%H:%M:%S")
   print (now, end ="\r")
   time.sleep(1)
   if now == alarm_time :
      print ("wake up")
      winsound.Beep(1000,3000)
      break