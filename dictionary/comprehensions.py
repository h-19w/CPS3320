# numbers = [1, 2, 3, 4]
# squares = {}

# for item in numbers:
#     squares[item] = item**2

# print(squares)


# squares = {item:item**2 for item in numbers}
# ## dict comprehension syntax: {key_expression: value_expression for item in iterable}
# # one liner for the above code block
# print(squares)



# ----------------------------

# selecting certain items using if

populations = {'New York': 8398748, 'Los Angeles': 3990456,
              'Chicago': 2705994, 'Houston': 2325502, 
              'Phoenix': 1660272, 'Philadelphia': 1584138}
largest = {k:v for k,v in populations.items() if v > 3000000}
print(largest)



# ----------------------------

dct1 = {'monday': 1, 'tuesday': 2, 'wednesday': 3}
print(dct1['monday'])
print(dct1.get('friday')) # this will return KeyError [since no key 'friday']
print(dct1.get('friday', 'not found')) # this will return the default value 
