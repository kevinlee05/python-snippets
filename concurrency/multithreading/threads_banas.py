import threading
import time
import random

def executeThread(i): #i is identification for thread name
    print("Thread {} sleeps at {}".format(i,
                time.strftime("%H:%M:%S", time.gmtime())))
    #strftime = string format time
    #gmtime = ???

    randSleepTime = random.randint(1, 10)

    time.sleep(randSleepTime)

    print("Thread {} stops sleeping at {}".format(i,
                time.strftime("%H:%M:%S", time.gmtime())))

for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    print("Active Threads :", threading.activeCount()) #print the number of threads actively executing

    print("Thread Objects :", threading.enumerate()) #list of all Thread objects currently live
