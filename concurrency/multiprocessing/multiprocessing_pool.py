# use multiprocessing pool to divide the work among multiple cores of your computer = > parallel computing
# simple map reduce concept
# MAP - dividing the work among multiple processes to run on CPU cores
# REDUCE - aggregating results from the multiple processes
from multiprocessing import Pool
import time


def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == '__main__':
    t1=time.time() #record the current time
    p = Pool()
    result = p.map(f, range(100000))
    #Pool.map() divides the task f amongst the cores
    p.close()
    p.join()
    print(len(result))
    print("pool took:", time.time() - t1)

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))

    print("serial processing took: ", time.time() - t2)
    print(len(result))
