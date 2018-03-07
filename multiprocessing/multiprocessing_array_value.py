#sharing data between 2 processes using shared memory
import multiprocessing
import array

result = []

def calc_square(numbers, result, v):
    v.value += 5.67 #v is the shared value
    for idx, n in enumerate(numbers):
        result[idx]= (n*n) # result is the shared indexed Array

if __name__ == '__main__':
    numbers = [2,3,5]

    result = multiprocessing.Array('i', 3) #result is an Array shared between processes
    v = multiprocessing.Value('d', 0.0) #v is a shared Value

    p1 = multiprocessing.Process(target=calc_square, args=(numbers,result, v))
    p2 = multiprocessing.Process(target=calc_square, args=(result,result, v))

    p1.start()
    p1.join()

    print(v.value, result[:])

    p2.start()
    p2.join()

    print(v.value, result[:])
