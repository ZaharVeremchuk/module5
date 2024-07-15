fh = open("test.txt", "w+")
fh.write("Mockito")

position = fh.tell()
print(position)

fh.seek(1)
position = fh.tell()
print(position)

fh.seek(6)
position = fh.tell()
print(position)

fh.close()