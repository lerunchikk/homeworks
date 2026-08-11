words = ["Python", "java", "C++", "Rust", "Go", "Swift", "PHP"]
result = [word.lower() for word in words if len(word)>=5]
print(result)