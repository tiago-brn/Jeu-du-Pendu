# 🎯 Jeu du Pendu

Un jeu du Pendu jouable dans le terminal, avec sélection aléatoire parmi 500 mots en français.

## Présentation

Le jeu choisit un mot au hasard dans une liste de 500 mots (animaux, objets du quotidien, métiers, informatique, nature, etc.). Vous devez le deviner lettre par lettre avant de perdre toutes vos vies.

## Règles

- Un mot est tiré au hasard, et sa longueur vous est indiquée.
- Vous proposez une lettre à la fois.
- Vous avez **7 vies**.
- Si la lettre n'est pas dans le mot, vous perdez une vie.
- Si vous découvrez toutes les lettres avant d'arriver à 0 vie, vous gagnez.

## Prérequis

- [Python 3](https://www.python.org/downloads/)

Aucune bibliothèque externe n'est nécessaire.

## Installation et lancement

```bash
git clone https://github.com/tiago-brn/NOM-DU-DEPOT.git
cd NOM-DU-DEPOT
python main.py
```

> Sous Linux/macOS, utilisez `python3 main.py` si `python` ne fonctionne pas.

## Exemple de partie

```
~~~~~~~~~~~~ Pendu ~~~~~~~~~~~~
Bienvenue sur le jeu du Pendu !

Le mot à deviner contient 5 lettres.
_____
Il vous reste 7 Vies
Veuillez entrer une lettre : a
La lettre a est dans le mot.
Mot : _ a _ _ _
```

## Structure du projet

```
.
├── main.py        # Logique du jeu et boucle principale
└── word_list.py   # Liste des 500 mots utilisables
```

## Personnaliser la liste de mots

Les mots sont stockés dans `word_list.py`, séparés par des espaces. Pour ajouter ou retirer des mots, modifiez simplement ce fichier. Les mots sont écrits sans accents pour faciliter la saisie des lettres.

## Auteur

Projet réalisé par [Tiago](https://github.com/tiago-brn).
