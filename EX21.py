from pathlib import PurePath
from pathlib import Path

# Use alternative library to os 
# It's pathlib

p = PurePath('/usr/bin/simple.jpg')
print("Name: ", p.name) # simple.jpg
print("Suffix:", p.suffix) # .jpg
print("Parent:", p.parent) # /usr/bin


# Use path
p = Path("test.txt")
p.write_text("Nice to meet you") # write in file
print(p.read_text()) # read from file
print("Exists", p.exists()) # Check if file exists


# Add way to path
base_path = Path("/usr/bin")
full_path = base_path / "subdir" / "script.py"
print(full_path)

