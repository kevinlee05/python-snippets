#How to merge 2 dictionaries in python 3.5+
# using "unpacking generalisations"

a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
c = {'b': 3, 'c': 4}

x = {**a, **b}
y = {**a, **c}
z = {**a, **b, **c}

print(x)
print(y)
print(z)
