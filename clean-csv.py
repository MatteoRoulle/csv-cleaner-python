import csv

def clean(nom, nouveau_nom):
    donnees_propres = []
    lignes_totales = 0
    lignes_conservees = 0
    lignes_ignorees = 0

    with open(f"{nom}.csv", "r", encoding="utf-8") as fichier:
        lignes = csv.DictReader(fichier)
        colonnes = lignes.fieldnames

        for ligne in lignes:
            lignes_totales += 1
            ligne_propre = {cle: valeur.strip() for cle, valeur in ligne.items()}

            if all(ligne_propre.values()):
                donnees_propres.append(ligne_propre)
                lignes_conservees += 1
            else:
                lignes_ignorees += 1

    with open(f"{nouveau_nom}.csv", "w", newline="", encoding="utf-8") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()
        writer.writerows(donnees_propres)

    with open("rapport.txt", "w", encoding="utf-8") as fichier:
        fichier.write(
            "RÉSULTAT DU NETTOYAGE\n"
            "---------------------\n\n"
            f"Lignes totales initiales : {lignes_totales}\n"
            f"Lignes conservées        : {lignes_conservees}\n"
            f"Lignes ignorées          : {lignes_ignorees}\n\n"
            "Nettoyage terminé avec succès.\n"
        )


if __name__ == "__main__":
    clean("data", "nouvelle_data")