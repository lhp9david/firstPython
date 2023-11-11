import tkinter as tk
from random import randint

nombre_dessais = 0  # Initialisation du compteur d'essais

def genere_un_nombre():
    # return randint(1, 100)
    return 50

def compare(nbr1, nbr2):
    if nbr1 < nbr2:
        return "Trop grand"
    elif nbr1 > nbr2:
        return "Trop petit"
    else:
        return "Gagné"

def demande_nombre(event=None):
    global nombre_dessais  # Utilisation de la variable globale
    try:
        nombre = int(entry.get())
        resultat = compare(nombre_a_trouver, nombre)
        label_resultat.config(text=resultat)
        nombre_dessais += 1  # Incrémentation du nombre d'essais
        if resultat == "Gagné":
            
            label_resultat.config(text=f"Vous avez trouvé en {nombre_dessais} essais")  # Affichage du nombre d'essais
            btn_submit.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
    except ValueError:
        label_resultat.config(text="Veuillez entrer un nombre valide.")

def rejouer():
    global nombre_a_trouver
    global nombre_dessais  # Réinitialisation du compteur d'essais lors d'une nouvelle partie
    nombre_a_trouver = genere_un_nombre()
    nombre_dessais = 0
    label_resultat.config(text='')
    btn_submit.config(state=tk.NORMAL)

def on_enter_key(event):
    demande_nombre()

nombre_a_trouver = genere_un_nombre()

root = tk.Tk()
root.title("Jeu devine le nombre")

label = tk.Label(root, text="Entrez un nombre entre 1 et 100 :")
label.pack()

entry = tk.Entry(root)
entry.pack()

btn_submit = tk.Button(root, text="Valider", command=demande_nombre)
btn_submit.pack()

label_resultat = tk.Label(root, text='')
label_resultat.pack()

btn_rejouer = tk.Button(root, text="Rejouer", command=rejouer)
btn_rejouer.pack()

entry.bind('<Return>', on_enter_key)

root.mainloop()
