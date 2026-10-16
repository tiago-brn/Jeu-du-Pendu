import random
from word_list import word

def get_random_word():
    return random.choice(word)

print("~~~~~~~~~~~~ Pendu ~~~~~~~~~~~~")
print("Bienvenue sur le jeu du Pendu !")
print("Voici les règles de la partie : ")
print("- Vous devez deviner un mot en choisissant des lettres.")
print("- Vous avez 7 vies pour deviner le mot.")
print("- Si vous devinez une lettre qui n'est pas dans le mot, vous perdez une vie.")
print("- Si vous devinez toutes les lettres du mot avant de ne plus avoir de vies, vous gagnez la partie.")

Vie = 7
mot_a_trouver = get_random_word()
print("\nLe mot à deviner contient", len(mot_a_trouver), "lettres.")
print("_" * len(mot_a_trouver))

mot_cache = ["_"] * len(mot_a_trouver)

while True:
    if Vie > 0:
        print("Il vous reste", Vie, "Vies")
        lettre = str(input("Veuillez entrer une lettre : ")).lower()
        if len(lettre) != 1:
            print("Veuillez entrer une seule lettre.")
            continue

        if lettre in mot_a_trouver:
            print("La lettre", lettre, "est dans le mot.")
            for index, lettre_du_mot in enumerate(mot_a_trouver):
                if lettre_du_mot == lettre:
                    mot_cache[index] = lettre
            print("Mot :", " ".join(mot_cache))

            if "_" not in mot_cache:
                print("Félicitations, vous avez trouvé le mot !")
                break
        else:
            print("La lettre", lettre, "n'est pas dans le mot.")
            Vie -= 1
            print("Mot :", " ".join(mot_cache))
        if Vie == 0:
            print("Vous n'avez plus de vies, vous avez perdu ! Le mot à deviner était :", mot_a_trouver, "\nTenter votre chance une prochaine fois ;)")
            break