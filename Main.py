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

print("\nOrderedDict is a dictionary that is ordered, however later versions of Python already have Python do that by "
      "default so it is not as relevant nowadays.")
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

print("\nDefaultdict assigns a default value to keys without a value, whether it be int, float, or even a list. Default "
      "must be a builtin, so strings don't work. \nThis avoids the Key Value error.")
def_dict = defaultdict(list)
def_dict['a'] = 1
def_dict['b'] = 2
print(def_dict['c'])

print("\nDeque generates a double-sided queue that we can manipulate with various commands.")
double_queue = deque()
print("\nIt is possible to add to it normally with .append(). It is also possible to add to the left side with "
      ".appendleft().")
double_queue.append(1)
double_queue.append(2)
double_queue.appendleft(3)
print(double_queue)
print("\n.pop() still works normally, but it also possible to use it from the left side with .popleft()")
double_queue.pop()
print(double_queue)
double_queue.popleft()
print(double_queue)
print("\n.clear() works normally.")
double_queue.clear()
print(double_queue)
double_queue.append(1)
double_queue.append(2)
double_queue.appendleft(3)
print("\nIt is possible to add on multiple elements at once as a list using .extend(). It is also possible to add from"
      " the left side using .extendleft(), \nhowever it will look like it's added in reverse since it's doing it one by one.")
double_queue.extend([4,5])
print(double_queue)
double_queue.extendleft([6,7])
print(double_queue)
print("\nIt is also possible to rotate the list using .rotate(). The number put in determines how many times it will "
      "rotate and if it is negative it will rotate to the left.")
double_queue.rotate(1)
print(double_queue)
double_queue.rotate(2)
print(double_queue)
double_queue.rotate(-4)
print(double_queue)