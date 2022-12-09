# Lists
# author: Kat
# date: 07/11/2022

# To create a list in Python, put a number of expressions in square brackets:


L = []
L = [expression, ...]

# This construct is known as a “list display”. You can also use
# the built-in list type object to create lists:

L = list() # empty list
L = list(sequence)

# The sequence can be any kind of sequence object or iterable, including tuples (covered later).
# If you pass in another list, the list function makes a copy. Note that Python creates a single new list every time
# you execute the [] expression. Python never creates a new list if you assign a list to a variable.

A = B = [] # both names will point to the same list
 
A = []
 
B = A # both names will point to the same list
 
A = []; B = [] # independent lists

# Accessing list

len(L) returns the number of items in the list 
 
L[i] returns the item at index i (the first item has index 0)
 
L[i:j] returns a new list, containing the objects between i and j.
 
n = len(L)
 
item = L[index]
