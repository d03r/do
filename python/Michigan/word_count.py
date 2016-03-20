"""
Counting Pattern
----------------
The general pattern to count the words in a line of text is to split
the line of text is to split the line into words, then loop through 
the words and use a dictionary to track the count of each word independently.
"""

counts = dict()
print "Enter a line of text:"
line = raw_input(">> ")

words = line.split()
print "Words: ", words

print "Counting..."
for word in words:
	counts[word] = counts.get(word, 0) + 1

print "Counts", counts

"""
Definite Loops and Dictionaries
-------------------------------
Even though dictionaries are not stored in order, we can write a for loop
that goes through all entries in a dictionary - actually it goes through 
all of the keys in the dictionary and looks up the values.
"""
for key in counts:
	print key, counts[key]
	