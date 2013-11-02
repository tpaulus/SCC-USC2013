#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com

import time
import requests

timeURL = 'http://json-time.appspot.com/time.json?tz='
zone = 'America/Los_Angeles'

while True:
    r = requests.get(timeURL + zone)                # Get the requested data form the server
    if r.status_code != 200:                        # Check to see if the server is okay
        quit(str(r.status_code) + ' - Service is not available, Sorry!')    # BAIL!
    else:
        timeJSON = r.json()                         # Convert request to JSON data
    hour = timeJSON['hour']                         # Create a variable form the 'hour' field in the JSON package
    minute = timeJSON['minute']                     # Create a variable form the 'minute' field in the JSON package
    second = timeJSON['second']                     # Create a variable form the 'second' field in the JSON package
    dateTime = timeJSON['datetime']                 # Create a string form the 'datetime' field in the JSON package
    print str(hour) + ':' + str(minute) + ':' + str(second)
    print dateTime
    time.sleep(1)