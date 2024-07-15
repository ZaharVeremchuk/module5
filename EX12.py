fh = open("test.txt", 'w')
fh.write("Hello\nmy\nmate")
fh.close()

fh = open("test.txt", 'r')
lines = [el.strip() for el in fh.readlines()]
print(lines)
fh.close()