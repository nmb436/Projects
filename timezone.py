import datetime
from datetime import datetime
import time
import pytz
from pytz import timezone
from dateutil.tz import tzutc, tzlocal


utc = datetime.now(tzutc())

portland = utc.astimezone(tzlocal())
portland_time = portland.strftime("%H : %M")
portland_hour = portland.strftime ("%H")

new_york = utc.astimezone(pytz.timezone('US/Eastern'))
new_york_time = new_york.strftime("%H : %M")
new_york_hour = new_york.strftime ("%H")

london = utc.astimezone(pytz.timezone('Europe/London'))
london_time = london.strftime("%H : %M")
london_hour = london.strftime ("%H")



if 0 < int(portland_hour) < 6:
     print ("London Open")
     print ("NY & Portland CLOSED")
     print ("time in London is" + " " + london_time)    
     
if 6 < int(portland_hour) < 9:
     print ("London & NY Open")
     print ("Portland CLOSED")
     print ("time in London is" + " " + london_time)
     print ("time in New York is" + " " + london_time) 
     
if 9 < int(portland_hour) < 13:
     print ("London & NY & Portland Open")
     print ("time in London is" + " " + london_time)
     print ("time in New York is" + " " + london_time)
     print ("time in Portland is" + " " + portland_time)

if 13 < int(portland_hour) < 18:
     print ("NY & Portland Open")
     print ("time in New York is" + " " + new_york_time)
     print ("time in Portland is" + " " + portland_time)
     print ("London is CLOSED")

if 18 < int(portland_hour) < 21:
     print ("Portland Open")
     print ("New York and London CLOSED")
     print ("time in Portland is" + " " + portland_time)

if 21 < int(portland_hour) < 24:
     print ("All Closed")





