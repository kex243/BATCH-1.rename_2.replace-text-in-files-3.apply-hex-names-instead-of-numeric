import os

for x in range (0,3334):
    h=("000000000000000000000000000000000000000000000000000000000000000"+str(hex(x)[2:]))[-64:]
    print (h)
    try:
        if len (h) == 64:
            os.rename(str(x)+".json",str(h))
        else:
            print ("no")
    except:
        None