
# Function to get unique elements from a list
def unique_elements(lst):
    return list(set(lst))

# Function to generate list of prime numbers in a given range using Sieve of Eratosthenes
def sieve_of_eratosthenes(min_val, max_val):
    if min_val <= 1:
        min_val = 2
    sieve = [True] * (max_val + 1)
    for start in range(2, int(max_val**0.5) + 1):
        if sieve[start]:
            for i in range(start*start, max_val + 1, start):
                sieve[i] = False
    return [num for num in range(min_val, max_val + 1) if sieve[num]]

# Class to represent a point in 2D space
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

# Function to sort list of strings by length
def sort_strings_by_length(strings):
    sorted_asc = sorted(strings, key=len)
    sorted_desc = sorted(strings, key=len, reverse=True)
    return sorted_asc, sorted_desc

# Tests
if __name__ == "__main__":
    # Test unique_elements
    print("Unique elements:", unique_elements([1, 2, 3, 2, 1, 4, 5, 5]))
    
    # Test sieve_of_eratosthenes
    print("Prime numbers in range 1-30:", sieve_of_eratosthenes(1, 30))
    
    # Test Point class
    point1 = Point(0, 0)
    point2 = Point(3, 4)
    print("Distance between points:", point1.distance_to(point2))
    
    # Test sort_strings_by_length
    string_list = ["apple", "banana", "cherry", "date"]
    sorted_asc, sorted_desc = sort_strings_by_length(string_list)
    print("Sorted by increasing length:", sorted_asc)
    print("Sorted by decreasing length:", sorted_desc)
