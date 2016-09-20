import re
file = open("run4hackz.py","r+")
txt = file.read()
patch = input("Enter full patch default(/storage/emulated/0/games/db.txt): ")
if patch == "":
    patch = "/storage/emulated/0/games/db.txt"
txt = re.sub(r"db.txt",patch,txt)
file.truncate()
file.write(txt)
file.close()
print("Modified to phone version.")
input("Press any key to exit...")
