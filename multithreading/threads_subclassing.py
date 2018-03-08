import threading
import time
import random

class CustThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self): #this is called when the thread is executed
        getTime(self.name)

        print("Thread", self.name, "Execution Ends")

def getTime(name):
    print("Thread {} sleeps at {}".format(name,
                time.strftime("%H:%M:%S", time.gmtime())))

    randSleepTime = random.randint(1, 5)

    time.sleep(randSleepTime)

thread1 = CustThread("1")
thread2 = CustThread("2")

thread1.start()
thread2.start()

print("Thread 1 Alive:", thread1.is_alive()) #check if thread1 is alive
print("Thread 2 Alive:", thread2.is_alive()) #check if thread2 is alive

print("Thread 1 Name:", thread1.getName()) #get name of thread
print("Thread 2 Name:", thread2.getName()) #get name of thread

thread1.join() #wait for threads to exit
thread2.join()

print("Execution Ends")
