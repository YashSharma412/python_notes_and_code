# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#! Initialize Tuple
# a.) general method
fruits_tuple  = ("apple", "banana", "cherry")
print(fruits_tuple, type(fruits_tuple))

# b.) using tuple constructor
fruits_tuple1 = tuple(("kiwi", "melon", "grapes", "mango"))
print(fruits_tuple1, type(fruits_tuple1))

#! if Tuple only has a single entry add a comma at the end.
test_tuple = ("test")
print(test_tuple, type(test_tuple)) # gives <class 'str'>

test_tuple1 = ("test",)
print(test_tuple1, type(test_tuple1)) # gives <class 'tuple'>

#! Deleteing a tuple
del test_tuple1
# print(test_tuple1)

#! Tuple Length
print(f"Tuple Length: {len(fruits_tuple)}")

# A Set is a collection which is unordered and unindexed. No duplicate members.

#! creating a set
# a.) general method
fruits_set = {"apple", "banana", "cherry", "apple"}
# b.) using set constructor
fruits_set1 = set(("kiwi", "melon", "grapes", "mango"))

#! Check if item is in a set
print("banana" in fruits_set)
print("banana" not in fruits_set)

#! add item in set
fruits_set.add("pineapple")
fruits_set.add("banana") 
print(fruits_set)


#! remove item from set
fruits_set.remove("banana")
print(fruits_set)


#! clear set
fruits_set.clear()
print(fruits_set)


#! delete set
del fruits_set
print(fruits_set)

#! set length
print(f"Set Length: {len(fruits_set1)}")

