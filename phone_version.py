import re
with open("run4hackz.py", "r") as f:
    txt = f.read()
    txt = txt.replace('"save.pkl"', "", 1)
    str2 = '''  if f.read() == "":
                f.close()
                return False'''
    txt = txt.replace(str2, "", 1)

with open("run4hackz_phone.py", "w") as f:
    f.write(txt)

print("Version transformed.")