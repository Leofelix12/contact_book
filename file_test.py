contacts = ["Felix, 0551234567"," Ama, 0207654321 ","Wendy, 0243539956" , " Naomi, 0501243564" ]

with open("contacts.txt", "w") as f:
    for contact in contacts:
        f.write(contact.strip() + "\n")
    
    
with open("contacts.txt", "r") as f:
    content = f.read()
    print(content)
