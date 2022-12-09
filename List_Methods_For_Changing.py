# Methods for Changing Lists
#
# @ author: Kat
# date: 08/11/2022


    list.append(elem)
        Adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
    list_1.extend(list_2) 
        Appends all of list_2 elements to the end of list_1.
    list.insert(index, elem) 
        Inserts the element at the given index, shifting elements to the right.
    list.index(elem)
        Searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError - see below).
    list.remove(elem)
        Searches for the first instance of the given element and removes it (throws ValueError if not present)
    list.sort()
        Sorts the list in place (does not return it)
    list.reverse()
        Reverses the list in place (does not return it)
    list.pop(index)
        Removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
    if value in L: 
        A boolean check to find out if a value exists in the list L
