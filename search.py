from Buzzer import *
import hashlib
import datetime
from pyfingerprint.pyfingerprint import PyFingerprint
from time import *
from get_data import *
from firebase import firebase

firebase = firebase.FirebaseApplication('https://fingerprint-c000e.firebaseio.com', None)

## Search for a finger
##

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

## Tries to search the finger and calculate hash
while True:
    try:
        print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)
        sleep(1)
        ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber == -1 ):
            ring(2)
            print('No match found!')
            #exit(0)
        else:
            now = datetime.datetime.now() 
            ring(1)
            print('Found template at position #' + str(positionNumber))
            print("Student: " + get_student(str(positionNumber)))
            result = firebase.post('/'+str(now.day)+"_"+str(now.month)+"_"+str(now.year),{str(now.hour)+"_"+str(now.minute):get_student(str(positionNumber))})

        ## OPTIONAL stuff
        ##

        ## Loads the found template to charbuffer 1
        f.loadTemplate(positionNumber, 0x01)

        ## Downloads the characteristics of template loaded in charbuffer 1
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

        sleep(3)

        ## Hashes characteristics of template
        #print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        sleep(3)
        pass
        #exit(1)
