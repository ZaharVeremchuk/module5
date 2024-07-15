p = b'Nice'
print(p[1]) # (ASCII-код символу)

# By default utf-8
# encoding  -> code in format
# erors -> how to handle error strict-> show, ignore -> ignore, replace -> replace unknown symbol as ?
byte_str = "test".encode(encoding="utf-8", errors="strict") 
print(byte_str)

# Convert list of number in bytes-row
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)

# Check last result with hex 
for num in [0, 128, 255]:
    print(hex(num))
    
# Symbol in utf8
print(ord('a')) # 97

# UTF-8 to symbol 
print(chr(108)) # l

s = "Привіт"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

utf32 = s.encode("utf-32")
print(f"UTF-32: {utf32}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)
