# MULTI VALUE CONATINER
# TUPLE () cannot be changed once it is created    # IMMUTABLE

# LISTS [] can be changed    #MUTABLE

# MVC
friends = ["A", "B", "C", 1001]
print(friends, type(friends), id(friends))

print(friends[0], type(friends[0]), id(friends[0]))
print(friends[1], type(friends[1]), id(friends[1]))
print(friends[2], type(friends[2]), id(friends[2]))
print(friends[3], type(friends[3]), id(friends[3]))

friends[0] = "JOHN"
print(friends[0], type(friends[0]), id(friends[0]))

