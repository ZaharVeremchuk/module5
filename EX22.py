from pathlib import Path

# absolute way to file
relative_path = Path("documents/test.txt")
absolute_path = relative_path.absolute()
print(absolute_path)

# relative way to file 
current_working_directory = Path("C:/Users/zahar/Neoversity/Projects/module5/documents/test.txt")
relative_path = absolute_path.relative_to(current_working_directory)
print(relative_path)