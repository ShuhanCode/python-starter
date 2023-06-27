
# This is a string INSERTED
print ('This is a string {}'.format("INSERTED"))

# The fox brown quick
print ("The {} {} {}".format('fox', 'brown', 'quick'))

# The quick brown fox
print ("The {2} {1} {0}".format('fox', 'brown', 'quick'))

# The fox fox fox
print ("The {0} {0} {0}".format('fox', 'brown', 'quick'))

# The quick brown fox
print ("The {q} {b} {f}".format(f = 'fox', b = 'brown', q = 'quick'))


my_name = 'Jose'

print ("Hello " + my_name)