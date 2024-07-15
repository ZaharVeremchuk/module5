fh = open("test.txt", "w+")
fh.write("Nice to meet you")

fh.seek(1)
symbol =  fh.read(1)
print(symbol)
fh.close()

