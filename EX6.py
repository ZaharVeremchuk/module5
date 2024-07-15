fh = open('test.txt', 'w')
fh.write('Good morning\nHow are you')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)
    
fh.close()