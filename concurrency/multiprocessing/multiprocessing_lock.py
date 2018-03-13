#Bathrooms have locks so that multiple people cannot use the shared resource at the same time
#without locks the balance result will vary from computation to computation

import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire() #acquires a lock over the shared resource
        balance.value = balance.value + 1
        lock.release() #releases the lock over the shared resource
        print(balance.value)

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        print(balance.value)
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200) #shared memory resource
    lock = multiprocessing.Lock() #create a lock to pass into each process
    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value)

