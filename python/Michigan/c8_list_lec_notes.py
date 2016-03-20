# We can create a new list by adding two existing lists together
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print c
print a

# Lists can be sliced using:
t = [9, 41, 12, 3, 74, 15]
print t[1:3] # [41,12]
print t[3:] # [3, 74, 15]
print t[:] # [9, 41, 12, 3, 74, 15]
# Note: Just like in strings, the second number is "up to but not including"

# Building a list from scratch
# - We can create an empty list and then add elements using the append method
# - The list stays in order and new elements are added at the end of the list
stuff = list()
print stuff
stuff.append("book")
stuff.append(99)
print stuff
stuff.append("cookie")
print stuff

# Is Something in a List?
# - Python provides two operators that let you check if an item is in a list.
# - These are logical operators that return True or False
# - They do not modify the list
some = [1, 9, 21, 10, 16]
print 9 in some # True
print 15 in some # False
print 20 not in some # True

# A List is an Ordered Sequence
# - A list can hold many items and keeps those items in the order until we do somthing to change the order
# - A list can be sorted (i.e., change its order)
# - The sort method (unlike in strings) means "sort yourself"
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort() # ['Glenn', 'Joseph', 'Sally']
print friends
print friends[1] # Joseph

# Build in Functions and Lists
# - There are a number of functions built into Python that take lists as parameters
# - http://docs.python.org/lib/built-in-funcs.html
nums = [3, 41, 12, 9, 74, 15]
print len(nums) # 6
print max(nums) # 74
print min(nums) # 3
print sum(nums) # 154
print sum(nums)/len(nums) # 25

# Best Friends: Strings and Lists
abc = "With three words"
stuff = abc.split()
print stuff # ['With', 'three', 'words']
print len(stuff) # 3
print stuff[0] # With 



