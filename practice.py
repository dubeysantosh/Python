import time
from datetime import datetime

def loop():
    while True:


        odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

        right_this_minute = datetime.today().minute

        if right_this_minute in odds:
            print ("This minute seems a litte odd")
        else:
            print("Not an odd minute.")


    #time.sleep(10);

if __name__ == "__main__":
    loop()


