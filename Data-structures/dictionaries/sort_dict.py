#how to sort a Python Dict by value
import operator

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted1 = sorted(xs.items(), key=lambda x:x[1])
#use sorted 'key' parameter to specify a function to be called on each list element prior to making comparisons.
print(sorted1)

sorted2 = sorted(xs.items(), key=operator.itemgetter(1))
#operator.itemgetter returns a callable object that fetches item from its operand using the operand’s __getitem__() method
print(sorted2)
