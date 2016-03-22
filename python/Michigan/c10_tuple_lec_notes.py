x = ('Glenn', 'Sally', 'Joseph')
print x[2]
y = (1, 9, 2)
print y
print max(y)

# Tuples are 'immutable'
# Unlike a list, once you created a tuple, you cannot alter its contents
# similar to a string

# Tuples are more efficient

# Since Python does not have to build tuple structures to be modifiable,
# they are simpler and more efficient in terms of memory use and performance
# than lists

# So in our program when we are making 'temporary variables' we prefer tuples over lists

# Tuples and Assignment
# We can also put a tuple on the left hand side of an assignment statement

(x, y ) = (4, 'fred')
print x
print y
a, b = (99, 98) # can even remove parenthesis
print a
print b


# Tuples and Dictionaries
# The items() method in dictionaries return a list of (key, value) tuples
d = dict()
d['csev'] = 2
d['cewn'] = 4
for (k,v) in d.items():
	print k,v

tups = d.items()
print tups

# Tuples are Comparable
# The comparison operators work with tuples and other sequences if the first
# item is equal, Python goes on to the next element, and so on, until it finds
# elements that differ.
print (0, 1, 2) < (5, 1, 2)

# Sorting Lists of Tuples
# We can take advantage of the ability to sort a list of tuples to get a 
# sorted version of a dictionary
# First we sort the dictionary by the key using the items() method
d = {'a':10, 'b':1, 'c':22}
t = d.items()
print t # [('a', 10), ('c', 22), ('b', 1)]
t.sort()
print t # [('a', 10), ('b', 1), ('c', 22)]

# Using sorted()
# We can do this even more directly using the built-in function sorted 
# that takes a sequence as a parameter and returns a sorted sequence
for k, v in sorted(d.items()):
	print k, v

# Sort by values instead of key
# - If we could constructs a list of tuples of the form (value, key) we could sort by value
# - We do this with a for-loop that creates a list of tuples
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
	tmp.append( (v, k) )
print tmp # [(10, 'a'), (22, 'c'), (1, 'b')]
tmp.sort(reverse=True) # [(22, 'c'), (10, 'a'), (1, 'b')]
print tmp
tmp.sort() # [(1, 'b'), (10, 'a'), (22, 'c')]
print tmp

# Adv
# Even Shorter Version 
# List comprehension creates a dynamic list.
# In this case, we make a list of reversed tuples and then sort it.
c = {'a':10, 'b':1, 'c':22}
print sorted( [ (v,k) for k, v in c.items() ] ) # [(1, 'b'), (10, 'a'), (22, 'c')]





