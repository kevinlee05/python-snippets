#sequential download

import urllib.request

def downloadImage(imagePath, fileName):
    print("downloading image from ", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    print("Completed Download")

def main_sequential():
    t0 = time.time()
    for i in range(10):
        imageName = "temp/image-" + str(i) + ".jpg"
        # generate a imageName which includes the temp/ directory, a string representation of what
        # iteration we are currently at--str(i)--and the file extension .jpg
        downloadImage("http://lorempixel.com/400/200/sports", imageName) #gives us a random image
    t1 = time.time()
    totalTime = t1 - t0
    print("main_sequential total execution time {}".format(totalTime))

#Concurrent Download

import threading
import urllib.request
import time

def executeThread(i):
    imageName = imageName = "temp/image-" + str(i) + ".jpg"
    downloadImage("http://lorempixel.com/400/200/sports/", imageName)

def main_threaded():
    t0 = time.time()
    #create an array which will store a reference to all our threads
    threads = []
    # create 10 threads, append them to our array of threads and start them off
    for i in range(10):
        thread = threading.Thread(target=executeThread, args=(i, ))
        threads.append(thread)
        thread.start()
    # ensure that all the threads in our array have completed their execution
    # before we log the total time to complete
    for i in threads:
        i.join()
    # calculate the total execution time
    t1 = time.time()
    totalTime = t1 - t0
    print("main_threaded total execution time {}".format(totalTime))

if __name__ == '__main__':
    # main_sequential()
    main_threaded()
