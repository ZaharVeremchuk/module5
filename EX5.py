fh = open('test.txt', 'w')
fh.write("Hello")
fh.close()

# Read by 1 symbol
fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)
    
fh.close()