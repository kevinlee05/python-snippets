import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square: ', n*n)

def calc_cube(numbers):
    print("calculate cube numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube: ', n*n*n)

arr = [2, 3, 8, 9]

def without_threading(arr):
    t = time.time()
    calc_square(arr)
    calc_cube(arr)
    return "without_threading done in: " + str(time.time() - t) + " seconds"

def with_threading(arr):

    t = time.time()
    thread1 = threading.Thread(target=calc_square, args=(arr,))
    thread2 = threading.Thread(target=calc_cube, args=(arr,))

    thread1.start()
    thread2.start()

    thread1.join() # waits for thread1 to finish executing before continuing
    thread2.join() # waits for thread2 to finish executing before continuing

    return "with_threading done in: " + str(time.time() - t) + " seconds"

def with_and_without(arr):
    t = time.time()
    thread1 = threading.Thread(target=without_threading, args=(arr,))
    thread2 = threading.Thread(target=with_threading, args=(arr,))

    thread1.start()
    thread2.start()

    thread1.join() # waits for thread1 to finish executing before continuing
    thread2.join() # waits for thread2 to finish executing before continuing

    return "with_and_without done in: " + str(time.time() - t) + " seconds"


print(with_and_without(arr))
