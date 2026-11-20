import random  # Importe le module random, qui permet de faire des choix aléatoires
from word_list import word  # Importe la liste "word" depuis ton fichier word_list.py

def get_random_word():  # Définit une fonction qui ne prend aucun paramètre
    return random.choice(word)  # Choisit un mot au hasard dans la liste "word" et le renvoie

print("~~~~~~~~~~~~ Pendu ~~~~~~~~~~~~")  # Affiche le titre du jeu
print("Bienvenue sur le jeu du Pendu !")  # Affiche un message de bienvenue
print("Voici les règles de la partie : ")  # Introduit les règles
print("- Vous devez deviner un mot en choisissant des lettres.")  # Règle 1 : le but du jeu
print("- Vous avez 7 vies pour deviner le mot.")  # Règle 2 : le nombre de vies au départ
print("- Si vous devinez une lettre qui n'est pas dans le mot, vous perdez une vie.")  # Règle 3 : la pénalité en cas d'erreur
print("- Si vous devinez toutes les lettres du mot avant de ne plus avoir de vies, vous gagnez la partie.")  # Règle 4 : la condition de victoire

Vie = 7  # Crée la variable qui stocke le nombre de vies restantes (7 au départ)
mot_a_trouver = get_random_word()  # Appelle la fonction pour tirer un mot au hasard et le stocke
print("\nLe mot à deviner contient", len(mot_a_trouver), "lettres.")  # Affiche la longueur du mot (\n = saut de ligne avant le texte)
print("_" * len(mot_a_trouver))  # Affiche autant de "_" que de lettres (ex : "_____" pour un mot de 5 lettres)

mot_cache = ["_"] * len(mot_a_trouver)  # Crée une liste de "_" (un par lettre) qui sera remplie au fil des bonnes réponses

while True:  # Boucle infinie : le jeu tourne jusqu'à un "break" (victoire ou défaite)
    if Vie > 0:  # Vérifie qu'il reste au moins une vie avant de continuer le tour
        print("Il vous reste", Vie, "Vies")  # Affiche le nombre de vies restantes
        lettre = str(input("Veuillez entrer une lettre : ")).lower()  # Demande une lettre au joueur, la convertit en texte puis en minuscules
        if len(lettre) != 1:  # Vérifie que le joueur n'a pas tapé 0 ou plusieurs caractères
            print("Veuillez entrer une seule lettre.")  # Message d'erreur si l'entrée n'est pas valide
            continue  # Revient au début de la boucle sans perdre de vie

        if lettre in mot_a_trouver:  # Teste si la lettre saisie est présente dans le mot secret
            print("La lettre", lettre, "est dans le mot.")  # Confirme que la lettre est bonne
            for index, lettre_du_mot in enumerate(mot_a_trouver):  # Parcourt le mot lettre par lettre, avec sa position (index)
                if lettre_du_mot == lettre:  # Si la lettre du mot correspond à celle proposée
                    mot_cache[index] = lettre  # Remplace le "_" à cette position par la lettre trouvée
            print("Mot :", " ".join(mot_cache))  # Affiche l'état du mot avec des espaces entre chaque caractère

            if "_" not in mot_cache:  # Si il ne reste plus aucun "_", toutes les lettres sont trouvées
                print("Félicitations, vous avez trouvé le mot !")  # Message de victoire
                break  # Sort de la boucle : la partie est terminée
        else:  # Sinon, la lettre n'est pas dans le mot
            print("La lettre", lettre, "n'est pas dans le mot.")  # Informe le joueur de son erreur
            Vie -= 1  # Retire une vie (équivalent à Vie = Vie - 1)
            print("Mot :", " ".join(mot_cache))  # Réaffiche l'état actuel du mot (inchangé)
        if Vie == 0:  # Vérifie si le joueur vient de perdre sa dernière vie
            print("Vous n'avez plus de vies, vous avez perdu ! Le mot à deviner était :", mot_a_trouver, "\nTenter votre chance une prochaine fois ;)")  # Message de défaite avec révélation du mot
            break  # Sort de la boucle : la partie est terminée