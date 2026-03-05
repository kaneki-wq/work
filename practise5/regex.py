import re

# 1
print(bool(re.match(r"ab*", "abbbb")))

# 2
print(bool(re.match(r"ab{2,3}$", "abb")))

# 3
print(re.findall(r"[a-z]+_[a-z]+", "hello_world test_case"))

# 4
print(re.findall(r"[A-Z][a-z]+", "Hello World Test"))

# 5
print(bool(re.match(r"a.*b$", "axxxb")))

# 6
text = "Hello, world. Test"
print(re.sub(r"[ ,\.]", ":", text))

# 7 snake → camel
def snake_to_camel(s):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), s)

print(snake_to_camel("hello_world_test"))

# 8 split at uppercase
print(re.split(r"(?=[A-Z])", "HelloWorldTest"))

# 9 insert spaces
print(re.sub(r"([A-Z])", r" \1", "HelloWorld").strip())

# 10 camel → snake
def camel_to_snake(s):
    return re.sub(r"([A-Z])", r"_\1", s).lower().strip("_")

print(camel_to_snake("HelloWorldTest"))