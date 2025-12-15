# 🧹 Nettoyage automatique de fichiers CSV en Python

Ce projet propose un script Python de nettoyage de fichiers CSV.

Il permet de traiter des fichiers de données simples mais imparfaits (valeurs manquantes, espaces inutiles) et de générer automatiquement :
- un nouveau fichier CSV propre
- un rapport de nettoyage

---

## 🎯 Objectifs du projet

- Lire un fichier CSV contenant des données brutes
- Nettoyer les valeurs (suppression des espaces inutiles)
- Ignorer les lignes incomplètes
- Produire un fichier CSV propre et exploitable
- Générer un rapport récapitulatif automatique

---

## 📄 Format des données

Le fichier d’entrée doit être un fichier CSV avec une ligne d’en-tête.

Exemple (data.csv) :
nom,age,ville
 Alice ,18,Paris
Bob,,Lyon
,20,Marseille

Clara ,19,Lille

---

## ✅ Résultat attendu

Fichier nettoyé (nouvelle_data.csv) :
nom,age,ville
Alice,18,Paris
Clara,19,Lille

Rapport généré (rapport.txt) :
RÉSULTAT DU NETTOYAGE
---------------------
Lignes totales initiales : 5
Lignes conservées        : 2
Lignes ignorées          : 3

Nettoyage terminé avec succès.

---

## ⚙️ Fonctionnement du script

Le script effectue les étapes suivantes :
1. Lecture du fichier CSV avec csv.DictReader
2. Nettoyage des espaces autour des valeurs
3. Vérification des lignes si elles sont complètes ou non
4. Conservation des lignes valides
5. Écriture des données propres dans un nouveau CSV
6. Génération automatique d’un rapport texte

---

## ▶️ Utilisation

Prérequis :
- Python 3 installé

Exécution :
python cleaner.py

Le script utilise par défaut :
- data.csv comme fichier d’entrée
- nouvelle_data.csv comme fichier de sortie
