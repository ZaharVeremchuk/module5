# Write file
fh = open('test.txt', 'w')
fh.write('Hello')
fh.close()

# Read file
fh = open('test.txt', 'r')
all_file = fh.read()
print(all_file)
fh.close()

