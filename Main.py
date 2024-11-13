# collections: a module containing alternatives of other storage methods.
#              Includes Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

print("\nCounter creates a dictionary that separates each element as keys with their count as the value. All dictionary "
      "functions work with the result.")
a = "aaaaabbbcc"
my_string = Counter(a)
print(my_string)

print("\nIt is possible to find the most common elements in the dictionary using .most_common(). It will generate a list "
      "with tuples as the elements.")
print(my_string.most_common(1))
print(my_string.most_common(2))

print("\nIt is possible to access the elements in the generated list using brackets([]).")
print(my_string.most_common(2)[1])
print(my_string.most_common(2)[1][0])

print("\nIt is also possible to generate a list showing all the elements using .elements().")
print(list(my_string.elements()))

print("\nUsing namedtuple will generate a class with however many fields desired separated by a comma.")
Point = namedtuple("Point", "x,y,z")
pt = Point(4,5,-1)
print(pt)

