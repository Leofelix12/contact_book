with open("greeting.txt", "w") as f:
    f.write("Hello from Felix")

with open("greeting.txt", "r") as f:
    content = f.read()
    print(content)

with open("contacts.txt", "w") as f:
    f.write("Felix, 0551234567\n")
    f.write("Ama, 0207654321\n")
