with open("contacts.txt", "w") as f:
    f.write("Felix, 0551234567\n")
    f.write("Ama, 0207654321\n")
    f.write("Wendy, 0243539956")
    
with open("contacts.txt", "r") as f:
    content = f.read()
    print(content)
