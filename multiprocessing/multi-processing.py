import time
from multiprocessing import Process

square_result=[]

def calc_square(numbers):
    global square_result
    for n in numbers:
        time.sleep(0.4)
        print('square ' + str(n*n))
        square_result.append(n*n)
    print('inside process result ' + str(square_result))

def calc_cube(numbers):
    for n in numbers:
        time.sleep(0.5)
        print('cube ' + str(n*n*n))


if __name__ == '__main__':
    arr = [2,3,8,9]

    p1 = Process(target=calc_square, args=(arr,))
    #p2 = Process(target=calc_cube, args=(arr,))

    p1.start()
    #p2.start()

    p1.join() #wait for process p1 to complete
    #p2.join() #wait for process p2 to complete

    print('outside process result ' + str(square_result)) # each process creates its own copy of square_result in its own address space
    print("Done!")
