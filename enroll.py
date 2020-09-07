import time
from pyfingerprint.pyfingerprint import PyFingerprint


try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

## Tries to enroll new finger
while True:
    try:
        print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Checks if finger is already enrolled
        result = f.searchTemplate()
        #print result
        positionNumber = result[0]

        if ( positionNumber >= 0 ):
            print('Template already exists at position #' + str(positionNumber))
            exit(0)

        name = raw_input("Enter New Student Name: ")
        time.sleep(2)

        local_db = open("student_db.csv","ab+")
        for i in range(6):
        ## Wait that finger is read again
            print "Place your finger on sensor %d/6"%(i+1)
            while ( f.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 2
            f.convertImage(0x02)

            ## Compares the charbuffers
            #if ( f.compareCharacteristics() == 0 ):
                #raise Exception('Fingers do not match')

            ## Creates a template
            f.createTemplate()

            ## Saves template at new position number
            positionNumber = f.storeTemplate()
            print('New template position #' + str(positionNumber))

            local_db.write(str(positionNumber)+","+name+"\n")
            time.sleep(3)
            
        local_db.close()  
        print('Finger enrolled successfully!')
        

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
