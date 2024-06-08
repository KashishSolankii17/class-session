john_friends = {'joe', 'jim', 'fionna', 'harry', 'koe', 'joe'}
sia_friends = {'joe', 'georga', 'fionna', 'jack', 'ben'}

print(john_friends)
print(sia_friends)

mutual_friends = john_friends & sia_friends
print(mutual_friends)


# SET does not support indexing 
# it support hashing 
# hence we cannot get the data from set
print(john_friends[0])


# Draw the  RAM model of dictionary