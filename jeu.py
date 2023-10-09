import os
from random import randint

def genere_un_nombre():
    return randint(1, 100)

def demande_un_nombre():
    return int(input("Entrez un nombre entre 1 et 100: "))

def compare(nbr1, nbr2):
    if nbr1 < nbr2:
        return "Trop grand"
    elif nbr1 > nbr2:
        return "Trop petit"
    else:
        return "Gagné"
    
def affiche_resultat(resultat):
    print(resultat)

def main():
    nombre_a_trouver = genere_un_nombre()
    nombre_dessais = 0
    resultat = ""
    while resultat != "Gagné":
        nombre_dessais += 1
        nombre = demande_un_nombre()
        resultat = compare(nombre_a_trouver, nombre)
        affiche_resultat(resultat)
    print("Vous avez trouvé en", nombre_dessais, "essais")
    os.system("pause")

if __name__ == "__main__":
    main()

    

