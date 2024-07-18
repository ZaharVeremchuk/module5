from pathlib import Path

original_path = Path("documents/test.txt")
# Change for path object
new_path = original_path.with_name("report.txt")
# Change exactly in the system
original_path.rename(new_path)