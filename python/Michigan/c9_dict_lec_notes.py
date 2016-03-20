"""
list : a linear collection of values that stay in order
dictionary : a 'bag' of values, each with its own label
The 'key' is the label.
Dictionaries are Python's most powerful data collection.
Dictionaries allow us to do fast database-like operations in Python
- Lists index their entries based on the position in the list
- Dictionaries are like bags - no order
- So we index the things we put in the dictionary with a 'lookup tag'.

"""

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print purse # {'money': 12, 'tissues': 75, 'candy': 3}
print purse['candy']
purse['candy'] = purse['candy'] + 2
print purse

"""
The get method for dictionary
-----------------------------
- This pattern of checking to see if a key is already in a dictionary
and assuming a default value if the key is not there is so common, that
there is a method called get() that does this for us.

if name in counts:
	print counts[name]
else:
	print  0 # Default

print counts.get(name,0)
"""

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
	counts[name] = counts.get(name,0) + 1 # CREATE OR UPDATE
print counts # {'csev': 2, 'zqian': 1, 'cwen': 2}

"""
Retriving lists of Keys and Values
----------------------------------
You can get a list of keys, values or items (both) from a dictionary.
"""
jjj = {'chuck':1, 'fred':42, 'jan':100}
print list(jjj) # ['jan', 'chuck', 'fred']
print jjj.keys() # ['jan', 'chuck', 'fred']
print jjj.values() # [100, 1, 42]
print jjj.items() # [('jan', 100), ('chuck', 1), ('fred', 42)]

