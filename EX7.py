fh = open("test.txt", "w")
fh.write("to be or not to be\nnever again\nhave fun")
fh.close()

fh = open("test.txt", "r")
lines = fh.readlines()
print(lines)
fh.close() 