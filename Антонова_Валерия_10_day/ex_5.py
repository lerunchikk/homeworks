files = [
"main.py",
"test.py",
"README.md",
"data.csv",
"notes.txt"
]
python_files = filter(lambda x: x.endswith(".py"),files)
print(list(python_files))
