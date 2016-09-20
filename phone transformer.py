import re
file = open("run4hackz.py","r+")
txt = file.read()
print("Enter the patch where you want to save your game")
patch = input("Enter full patch default(/storage/emulated/0/games/db.txt): ")
if patch == "":
    patch = "/storage/emulated/0/games/db.txt"
elif patch[-3:] != "txt":
    patch += "db.txt"
txt = re.sub(r"db.txt",patch,txt)
file.truncate()
file.write(txt)
file.close()
print("Modified to phone version.")
input("Press any key to exit...")
