# Primitive Data Types in python
# 1. String
# 2. Integer
# 3. Float
# 4. Boolean

# Subscripting
print("Hello"[0])
print("Hello"[-1])

# String
print("123" + "456")

# Integer = Whole number
print(123 + 456)

# Float = Floating point number
print(3.142)

# Boolean
print(True)
print(False)

# Type Error
# These errors occur when you are using the wrong data type.
# len(12345)

# Type Checking
# You can check the data type of any value or variable in python using the type() function
print(type("abc")) # <class 'str'>
print(type(123)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(True) # True

# Type Conversion
# You can convert data into different data types using special function.
print(int("123") + int("2"))