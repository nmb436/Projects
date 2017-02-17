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



print ("The time in Portland is" + " " +  portland_time)

if 9 < int(new_york_hour) < 21:
    print ("New York is Open" + " " + new_york_time)
    

else:
     print ("New York is Closed" + " " + new_york_time)

if 9 < int(london_hour) < 21:
    print ("London is Open" + " " + london_time)

else:
     print ("London is Closed" + " " + london_time)
