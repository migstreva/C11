name = input("Enter your full name: ")

print(name.upper())

print(name.lower())

letters_only = [char for char in name if char.isalpha()]
print(len(letters_only))

parts = name.split()
parts[-1] = "do Inatel"

new_name = " ".join(parts)
print(new_name)
