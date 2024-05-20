import tkinter as tk
import subprocess


def jouer_bataille():
    # Fonction à exécuter lorsque le bouton "Jeu Bataille" est cliqué
    print("Bataille lancé")
    subprocess.run(["python", "bataille.py"])


def jouer_belote():
    # Fonction à exécuter lorsque le bouton "Belote" est cliqué
    print("Belote lancé")
    # Lancer le script main.py
    subprocess.run(["python", "main.py"])


# Création de la fenêtre principale
root = tk.Tk()
root.title("Menu de Jeux")

# Création des boutons pour les jeux
btn_bataille = tk.Button(root, text="Jeu Bataille", command=jouer_bataille)
btn_bataille.pack(pady=10)

btn_belote = tk.Button(root, text="Belote", command=jouer_belote)
btn_belote.pack(pady=10)

# Exécution de la boucle principale
root.mainloop()






