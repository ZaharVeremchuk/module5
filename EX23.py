from pathlib import Path

# File way
original_path = Path("documents/test.txt")

# Change file name 
new_path = original_path.with_name("report.txt")
print(new_path)