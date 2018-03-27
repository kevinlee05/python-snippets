# serial, threading, processing and pool approach for computing primes
import time
import threading as th
import multiprocessing as mp
import queue

def isprime(n):
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def prime(Nth, q=None): # prints the Nth prime
    n_found = 0
    i = 0
    while n_found < Nth:
        i+=1
        n_found = n_found + int(isprime(i))
    if q:
         q.put(i) # send to Queue object if set
    return i

start = 20000

if __name__ == '__main__':
    t1 = time.time() #time serial segment
    print(prime(start), prime(start + 1), prime(start + 2), prime(start+3))
    print('Serial test took ', time.time() - t1, 'seconds')


    t2 = time.time() #time multithreaded segment
    q1 = queue.Queue()
    jobs = [ th.Thread(target=prime, args=(start, q1)),
        th.Thread(target=prime, args=(start+1, q1)),
        th.Thread(target=prime, args=(start+2, q1)),
        th.Thread(target=prime, args=(start+3, q1))
    ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print(q1.get(),q1.get(),q1.get(),q1.get())
    print('multithreaded test took ', time.time() - t2, 'seconds')


    t3 = time.time() #time multiprocessing segment
    q = mp.Queue()
    jobs2 = [ mp.Process(target=prime, args=(start, q)),
        mp.Process(target=prime, args=(start+1, q)),
        mp.Process(target=prime, args=(start+2, q)),
        mp.Process(target=prime, args=(start+3, q))
    ]
    for j in jobs2:
        j.start()
    for j in jobs2:
        j.join()
    print(q.get(),q.get(),q.get(),q.get())
    print('multiprocessing test took ', time.time() - t3, 'seconds')

    t4 = time.time()
    pool = mp.Pool(processes=4)
    result = pool.map(prime, range(start, start+4))
    print(result)
    print('Pool test took', time.time() - t4, 'seconds')
