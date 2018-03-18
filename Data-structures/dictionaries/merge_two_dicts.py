#How to merge 2 dictionaries in python 3.5+
# using "unpacking generalisations"

a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
c = {'b': 3, 'c': 4}

x = {**a, **b}
y = {**a, **c} # the 'b' value in a is replaced by the 'b' value in c
z = {**a, **b, **c} # the 'c' value in b is replaced by the 'c' value in d

assert x == {'a': 1, 'b': 2, 'c': 3, 'd': 4}
assert y == {'a': 1, 'b': 3, 'c': 4}
assert z == {'a': 1, 'b': 3, 'c': 4, 'd': 4}

