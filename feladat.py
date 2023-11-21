import json

adatbazis = []
#a
with open("database.json", "r", encoding="utf8") as fájl:
    adatbazis = json.load(fájl)

print(adatbazis)