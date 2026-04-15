import re

#
with open("verbe.txt", "r", encoding="utf-8") as f: # PowerShell génère souvent de l'UTF-16
    content = f.read()


pattern = r"^(\w+).*\n?"


result = re.sub(pattern, r"\1, ", content, flags=re.MULTILINE)

print(result)
