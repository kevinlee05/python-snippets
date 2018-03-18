#The standard string repr for dicts is hard to read
#as an alternative to pprint module use json.dumps() to pretty print python dicts
import json
from pprint import pprint

my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}

print(my_mapping)
print(pprint(my_mapping))
print(json.dumps(my_mapping, indent=4, sort_keys=True))

#note this only works with dicts containing primitive types
