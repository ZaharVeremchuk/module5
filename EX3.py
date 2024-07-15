fh = open("test.txt", "w+") # w+ - rewrite if file exist
fh.write("Hello from Ex3.py")
fh.seek(0) # Move cursor to start of file 

first_two_symbols = fh.read(2)
print(first_two_symbols) # returned read symbols (He)
fh.close()