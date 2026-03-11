import csv
import json
import sys
from pathlib import Path

try:
    f_csc = Path(sys.argv[1])
    if sys.argv[2] != '-ip':
        raise ValueError()
    ip = sys.argv[3]
except IndexError:
    print("ERREUR : Le nombre d'argument est incorrecte...")
    print("Usage : python ip_log.py nom_fichier_csv -ip @ip")
    exit(1)
except ValueError:
    print("ERREUR : Le second argument doit être '-ip'...")
    print("Usage : python ip_log.py nom_fichier_csv -ip @ip")
    exit(1)

compteur_ip = 0

with open(f_csv, 'r', encoding='utf-8') as fichier_csv:
    lignes_csv = csv.reader(fichier_csv)
    for ligne in lignes_csv:
        if ip in ligne:
            compteur_ip += 1

print(f"Nombre d'occurence de l'@IP : {ip} : {compteur_ip}")

nom_fichier_json = Path('ip.json')
liste_dico_actuel = []
if nom_fichierijson.exists():
    with open(nom_fichier_json, 'r', encoding= 'utf-8') as fichier_json:
        print(liste_dico_actuel)

liste_dico_actuel.append({ip : compteur_ip})

