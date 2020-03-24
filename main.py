from basic_linear_search import linear_search
from binary_search import binary_search
from basic_recursive_search import recursive_search

sorted_array = [1, 2, 3, 4, 5, 7, 10, 12, 15, 27, 33]

print(linear_search(10, sorted_array))

print(binary_search(4, sorted_array))
print(binary_search(15, sorted_array))
print(binary_search(34, sorted_array))

print(recursive_search(sorted_array, 0, 10))
print(recursive_search(sorted_array, 0, 11))

