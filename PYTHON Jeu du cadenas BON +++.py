# Créé par regis.serres, quand il était plus jeune
print("    ┌---┐")
print("  __|___|__ ")
print(" /         \\")
print("|    LOCK   |")# Ceci est un dessin d'un cadenas...
print("|    0000   |")
print(" \\_________/")
print("")


import random

def generer_combinaison():
    combinaison = random.sample(range(10), 4)  # Les 4 premiers chiffres sont dans la combinaison
    random.shuffle(combinaison)  # Mélanger la combinaison
    return combinaison

def afficher_indices(combinaison):
    print("Indices en début de partie :")
    indices_combinaison = random.sample(combinaison, 2)  # Sélectionner aléatoirement 2 chiffres de la combinaison
    indices_non_combinaison = random.sample([x for x in range(10) if x not in combinaison], 2)  # Sélectionner aléatoirement 2 chiffres qui ne sont pas dans la combinaison
    indices = indices_combinaison + indices_non_combinaison
    random.shuffle(indices)  # Mélanger les indices
    for i, chiffre in enumerate(indices):
        if chiffre in indices_combinaison:
            print(f"*** Indice {i + 1} : Le chiffre {chiffre} est dans la combinaison ***")
        else:
            print(f"*** Indice {i + 1} : Le chiffre {chiffre} n'est pas dans la combinaison ***")
    print("*****************************************************************************")

def evaluer_guess(combinaison, guess):
    bien_places = mal_places = 0

    for i in range(4):
        if guess[i] == combinaison[i]:
            bien_places += 1
        elif guess[i] in combinaison:
            mal_places += 1

    return bien_places, mal_places

def main():
    print("Bienvenue dans le jeu du CADENAS ! Trouveras-tu la bonne combinaison pour l'ouvrir ?")
    print("Monsieur SERRES pense que non")
    print("Tu dois entrer des combinaisons de 4 chiffres différents (par exemple : 1234)")
    print("*****************************************************************************")

    combinaison = generer_combinaison()
    essais_restants = 10

    afficher_indices(combinaison)  # Afficher les indices en début de partie

    while essais_restants > 0:
        guess = input("Entrez une combinaison de 4 chiffres (différents) ► ")

        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Veuillez entrer une combinaison valide de 4 chiffres différents ► ")
            continue

        guess = [int(x) for x in guess]
        bien_places, mal_places = evaluer_guess(combinaison, guess)

        print(f"► Nombre de chiffres bien placés : {bien_places}")
        print(f"► Nombre de chiffres mal placés : {mal_places}\n")

        essais_restants -= 1

        if bien_places == 4:
            print("*****************************************************************************")
            print(f"BRAVO, vous avez trouvé la combinaison correcte en {11 - essais_restants} essais !")
            print(f"La combinaison correcte était bien : {''.join(map(str, combinaison[:4]))}")
            print("*****************************************************************************")
            break

    if essais_restants == 0 and bien_places != 4:
        print("*****************************************************************************")
        print(f"PERDU. La combinaison correcte était : {''.join(map(str, combinaison[:4]))}")
        print("*****************************************************************************")

if __name__ == "__main__":
    main()
