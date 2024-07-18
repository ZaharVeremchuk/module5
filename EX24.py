from pathlib import Path 

original_path = Path("documents/test.txt")

# Change file type 
new_path = original_path.with_suffix(".doc")
print(new_path)
