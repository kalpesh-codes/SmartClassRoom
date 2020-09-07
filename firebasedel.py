from firebase import firebase
import datetime
from time import sleep
firebase = firebase.FirebaseApplication('https://fingerprint-c000e.firebaseio.com', None)


while True:
    now = datetime.datetime.now()
    if(now.hour >= 19 and now.minute == 1):
        firebase.delete('/'+str(now.day)+"_"+str(now.month)+"_"+str(now.year),None)
        sleep(5)
        print "Deleted"

