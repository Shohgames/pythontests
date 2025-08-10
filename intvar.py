# ✅ VALID variable names
a2 = "valid"           # starts with letter
_private = "valid"     # starts with underscore
my_var = "valid"       # underscores allowed
Variable123 = "valid"  # numbers after letters are OK

print("Valid variables work fine:")
print(a2)
print(_private)
print(my_var)
print(Variable123)

# ❌ INVALID variable names (commented out to avoid errors):
# 2var = "invalid"     # starts with number
# 123 = "invalid"      # just a number
# my-var = "invalid"   # contains hyphen
# my var = "invalid"   # contains space

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#its possible to  have multiple vars in a single line didn't know that actually wow
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#this one feels cringe
x = y = z = "Orange"

print(x)
print(y)
print(z)

# Your question: unpacking a list
print("\n--- Unpacking a list ---")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print("x:", x)
print("y:", y)
print("z:", z)

# Can we do fruits = x, y, z? YES!
print("\n--- Packing variables into a tuple ---")
fruits = x, y, z  # This creates a tuple!
print("fruits:", fruits)
print("type of fruits:", type(fruits))

# Let's see the difference
print("\n--- Comparison ---")
original_list = ["apple", "banana", "cherry"]
recreated_tuple = x, y, z

print("original_list:", original_list, "- type:", type(original_list))
print("recreated_tuple:", recreated_tuple, "- type:", type(recreated_tuple))

# If you want a list instead of tuple:
print("\n--- Creating a list instead ---")
fruits_as_list = [x, y, z]  # Use square brackets for list
print("fruits_as_list:", fruits_as_list, "- type:", type(fruits_as_list))

print("\n" + "="*50)
print("TUPLE vs LIST - Key Differences")
print("="*50)

# 1. SYNTAX - How they're created
print("\n1. SYNTAX:")
my_list = ["apple", "banana", "cherry"]    # Square brackets []
my_tuple = ("apple", "banana", "cherry")   # Parentheses ()
# or even simpler tuple syntax:
my_tuple2 = "apple", "banana", "cherry"    # No parentheses needed

print("List:", my_list)
print("Tuple:", my_tuple)
print("Tuple2:", my_tuple2)

# 2. MUTABILITY - Can you change them?
print("\n2. MUTABILITY (Can you change them?):")
print("Lists are MUTABLE (can be changed):")
my_list[0] = "CHANGED!"
print("After changing:", my_list)

print("Tuples are IMMUTABLE (cannot be changed):")
try:
    my_tuple[0] = "CHANGED!"  # This will fail!
except TypeError as e:
    print("Error:", e)

# 3. METHODS - What can you do with them?
print("\n3. AVAILABLE METHODS:")
print("List methods:", [method for method in dir(my_list) if not method.startswith('_')])
print("Tuple methods:", [method for method in dir(my_tuple) if not method.startswith('_')])

# 4. PERFORMANCE
print("\n4. PERFORMANCE:")
import time

# Time creating large list vs tuple
start = time.time()
big_list = [i for i in range(10000)]
list_time = time.time() - start

start = time.time()
big_tuple = tuple(i for i in range(10000))
tuple_time = time.time() - start

print(f"Creating 10,000 items - List: {list_time:.6f}s, Tuple: {tuple_time:.6f}s")

# 5. WHEN TO USE WHICH?
print("\n5. WHEN TO USE WHICH?")
print("\nUse LISTS when:")
print("- You need to add/remove/change items")
shopping_cart = ["milk", "eggs"]
shopping_cart.append("bread")      # Add item
shopping_cart.remove("eggs")       # Remove item
shopping_cart[0] = "almond milk"   # Change item
print("Shopping cart:", shopping_cart)

print("\nUse TUPLES when:")
print("- Data should never change (coordinates, RGB colors, etc.)")
coordinates = (40.7128, -74.0060)  # NYC coordinates - should never change
rgb_red = (255, 0, 0)              # Red color - should never change
print("NYC coordinates:", coordinates)
print("Red color RGB:", rgb_red)

print("- Returning multiple values from functions")
def get_name_age():
    return "John", 25  # Returns a tuple

name, age = get_name_age()
print(f"Name: {name}, Age: {age}")

# 6. MEMORY USAGE
print("\n6. MEMORY USAGE:")
import sys
sample_list = [1, 2, 3, 4, 5]
sample_tuple = (1, 2, 3, 4, 5)
print(f"List memory: {sys.getsizeof(sample_list)} bytes")
print(f"Tuple memory: {sys.getsizeof(sample_tuple)} bytes")
print("Tuples use less memory!")
