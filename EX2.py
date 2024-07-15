# Create and write into test.txt
fh = open("test.txt", "w")
symbols_written = fh.write("Hello from EX2.py")
print(f"Count of symbols written in file: {symbols_written}")
fh.close()