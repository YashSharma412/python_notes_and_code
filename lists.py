# A List is a collection which is ordered and changeable. Allows duplicate members.

#! Making a list, 
# 1 using general square brackets
nums = [1, 2, "three", 4, 5];
# 2 using list constructor
nums1 = list((1, 2, "three", 4, 5));
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(nums)
print(nums1)

'''
    List Methods
    append() - Adds an item to the end of the list
    remove() - Removes an item from the list
    pop() - Removes the last item from the list by default, passing an index will remove the item at that index.
    reverse() - Reverses the list
    sort() - Sorts the list
    copy() - Returns a copy of the list

'''

# Get List Length
print(len(fruits))

# Add to list, (in javascript we would use .push)
fruits.append("pineapple")
print(fruits, len(fruits))

# remove from list
fruits.remove("banana")
print(fruits)

# remove from list at an index
poppedFruit =  fruits.pop(2)
print(fruits, f"popped fruit: {poppedFruit}")

# reverse list
fruits.reverse()
print(fruits)

# sort a list in ascending order
fruits.sort()
print(fruits)

# sort a list in descending order
fruits.sort(reverse=True)
print(fruits)

# copy a list
fruits2 = fruits.copy()
print(fruits2)



