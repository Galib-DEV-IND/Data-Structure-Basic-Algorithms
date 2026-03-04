# List
num = [1, 'Two', 3, 4, 5, 3.45]
print(num)

# Add an item to the end of the list
num.append('Thrity five')
print(num)

num[len(num):] = '87'
print(num)

num[len(num):] = ['67']
print(num)

# Below will raise TypeError: must assign iterable to extended slice
try:
    num[len(num):] = 88
    print(num)
except TypeError as e:
    print('Must assign iterable to extended slice')

# Extend the list by appending all the items from the iterable
# -- with list
num.extend(['2', 5])
print(num)

# -- with range
num.extend(range(7, 10))
print(num)

# -- with tuples
num.extend((56, 78))
print(num)

# -- with set
num.extend({5, 5, 6})
print(num)

# Insert into a specific position
num.insert(4, '100')
print(num)

# Remove the first item from the list whose value is equal to x
try:
    num.remove(33)
    print(num)
except ValueError as e:
    print('The mentioned item is not present anywhere in the list')


# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.
popped_item_5 = num.pop(5)
print(popped_item_5) 

popped_item_without_index = num.pop()
print(popped_item_without_index)

# list.clear()
# Remove all items from the list. Similar to del a[:].
# num.clear()
# print(num)

# list.index(x[, start[, end]])
# Return zero-based index of the first occurrence of x in the list. Raises a ValueError if there is no such item.

# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
num = [1,2,3,1,3,4,5,6,1,7,8,2,3]
print(num.index(1,2,len(num))) #Always return index of the first occurence
# list.count(x)
# Return the number of times x appears in the list.
num.count(1)

# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
words = ["cat", "elephant", "dog"]
## For the above list sort the list in reverse order based on len of word
words.sort(key=len, reverse=True)
print(words)
# list.reverse()
# Reverse the elements of the list in place.
num.reverse()
print(num)

# list.copy()
# Return a shallow copy of the list. Similar to a[:].
num1 = num.copy()
print(num1)


# Tuple

# Set

# Dictionary