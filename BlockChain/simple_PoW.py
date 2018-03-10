# solve for hash x*y where x=5 and the last 5 digits of the hash = 00000

from hashlib import sha256
import time

def hash(x, y):
    return sha256(f'{x*y}'.encode()).hexdigest()

def proof_of_work(x, proof):
    y = 0 # We don't know what y should be yet...
    t = time.time()
    z = len(proof) #z is the length of the proof string
    while hash(x, y)[:z] != proof:
        y += 1
    print(f'The solution is y = {y}')
    print('The hash is ' + hash(x, y))
    print('The hash took ' + str(time.time() - t) + ' seconds to compute')
    return

proof_of_work(5, "00000")
#000000 takes about a minute to compute


