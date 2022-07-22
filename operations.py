# Let's practice more data types!

# integers = whole numbers
integ = 20
print(type(integ))
# Use a # in the next line to write the data type:
# answer from output: <class 'int'>

# floats = numbers with decimals
floa = 1.001
print(type(floa))
# answer from output:<class 'float'>

# strings = sequences of characters
jams = "spotify_playlist"
print(type(jams))
# answer from output: <class 'str'>

# Booleans = represent true or false
is_it_friday = False
print(type(is_it_friday))
# answer from output: <class 'bool'>

## Operators you can do with integers & floats

# addition
print(integ + 5)
# answer from output: 25

# subtraction
print(integ - 3)
# answer from output: 17

# multiplication
print(integ * 10)
# answer from output: 200

# division
print(floa/5)
# answer from output: 0.2002

"""" Modulus Operator = an inbuilt operator in Python that returns the remaining numbers by division """
print(integ % 3)
# answer from output: 2

### Typecasting = converting 1 data type to another kind of data type

## How to convert string to int
# "25" is numerical but since it's inside double quotes, it's treated as a string. It can be converted to an integer by inputting the number within single or double quotes insdie type(int()):
print(type(int('25')))
# What data type does it show in the output? <class 'int'> an integer

# However this would not work if 25 was written in words "twenty-five"--only for stringed numbers that are still look numerical.

## How to convert int to string
print(type(str(10)))
# What data type does it show in the output? <class 'str'> a string

## How to convert int to bool
bool(10)
print(bool(10))
print(type(bool(10)))