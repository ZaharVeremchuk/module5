with open("test.txt", "w") as fh:
    fh.write("Nice to meet you")
    
with open("test.txt", "r") as fh:
    lines = [line.strip() for line in fh.readlines()]
    print(lines)