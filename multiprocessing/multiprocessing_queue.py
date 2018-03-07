# demonstration of using a normal queue vs multiprocessing queue with Processes
import multiprocessing
import queue
result = []

def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n) #add n*n to the queue

if __name__ == '__main__':
    numbers = [2,3,5]

    q1 = queue.Queue() #normal queue

    q2 = multiprocessing.Queue() #multiprocessing queue lives in shared memory and is used to share data between processes
    p1 = multiprocessing.Process(target=calc_square, args=(numbers, q1))
    p2 = multiprocessing.Process(target=calc_square, args=(numbers, q2))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("q1: ")
    while q1.empty() is False:
        print(q1.get())  #empty because Processes create their own copy

    print("q2: ")
    while q2.empty() is False:
        print(q2.get())  #uses the shared multiprocess queue object
