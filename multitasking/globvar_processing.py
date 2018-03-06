from multiprocessing import Process

globvar = 0

def add_one_to_globvar():
    global globvar    # Needed to modify global copy of globvar
    globvar += 1

def add_one_and_print():
    global globvar
    globvar += 1
    print(globvar)

if __name__ == '__main__':
    add_one_to_globvar()
    print(globvar) #1

    p1 = Process(target=add_one_and_print, args=()) #2 - makes a copy of globvar at this point and runs the process with the new copy
    p1.start()
    p1.join()

    print(globvar) #1 - prints the original copy of globvar

