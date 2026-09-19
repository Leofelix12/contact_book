with open("greeting.txt", "w") as f:
    f.write("Hello from Felix")

with open("greeting.txt", "r") as f:
    content = f.read()
    print(content)
