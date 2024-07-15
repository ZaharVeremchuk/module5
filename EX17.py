byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)

#Add symbol
byte_array.append(ord("!"))
print(byte_array)

# Convert to str
str = byte_array.decode("utf-8")
print(str)