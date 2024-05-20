import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import os
import random

# Définition des noms des cartes et leurs chemins d'accès aux images
cartes = {
    '7 de carreau': 'images/7karo.png',
    '7 de coeur': 'images/7kupa.png',
    '7 de piques': 'images/7pika.png',
    '7 de trèfle': 'images/7spatiq.png',
    '8 de carreau': 'images/8karo.png',
    '8 de cœur': 'images/8kupa.png',
    '8 de pique': 'images/8pika.png',
    '8 de trèfle': 'images/8spatiq.png',
    '9 de carreau': 'images/9karo.png',
    '9 de cœur': 'images/9kupa.png',
    '9 de pique': 'images/9pika.png',
    '9 de trèfle': 'images/9spatiq.png',
    '10 de carreau': 'images/10karo.png',
    '10 de cœur': 'images/10kupa.png',
    '10 de pique': 'images/10pika.png',
    '10 de trèfle': 'images/10spatiq.png',
    'Valet de carreau': 'images/11karo.png',
    'Valet de cœur': 'images/11kupa.png',
    'Valet de pique': 'images/11pika.png',
    'Valet de trèfle': 'images/11spatiq.png',
    'Dame de carreau': 'images/12karo.png',
    'Dame de cœur': 'images/12kupa.png',
    'Dame de pique': 'images/12pika.png',
    'Dame de trèfle': 'images/12spatiq.png',
    'Roi de carreau': 'images/13karo.png',
    'Roi de cœur': 'images/13kupa.png',
    'Roi de pique': 'images/13pika.png',
    'Roi de trèfle': 'images/13spatiq.png',
    'As de carreau': 'images/14karo.png',
    'As de cœur': 'images/14kupa.png',
    'As de pique': 'images/14pika.png',
    'As de trèfle': 'images/14spatiq.png'
}

# Mélanger les cartes
liste_cartes = list(cartes.keys())
random.shuffle(liste_cartes)

# Distribuer les cartes aux joueurs
joueur_nord = liste_cartes[:5]
joueur_sud = liste_cartes[5:10]
joueur_est = liste_cartes[10:15]
joueur_ouest = liste_cartes[15:20]

# Initialiser les scores des équipes
score_equipe_nord_sud = 0
score_equipe_est_ouest = 0

# Variable pour suivre quel joueur doit prendre la carte au milieu
joueur_actuel = "nord"

# Variable pour stocker la carte retournée
carte_retournee = None

# Variable pour suivre le nombre de clics sur le bouton
nombre_clics = 0


# Fonction pour afficher les cartes d'un joueur
def afficher_cartes_joueur(joueur):
    fenetre = tk.Toplevel()
    fenetre.title("Cartes du joueur")

    for i, carte in enumerate(joueur):
        chemin_image = cartes[carte]
        image = Image.open(chemin_image)
        image = image.resize((96, 130), Image.BILINEAR)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(fenetre, image=photo)
        label.image = photo
        label.grid(row=0, column=i, padx=5, pady=5)


def mettre_a_jour_scores():
    global score_equipe_nord_sud, score_equipe_est_ouest
    # Mettre à jour les scores selon la logique du jeu


# Variable pour suivre le nombre total de clics sur le bouton "Retourne"
nombre_total_clics_retourne = 0

# Variable pour suivre le nombre de clics sur le bouton "Retourne"
nombre_clics_retourne = 0


# Fonction pour afficher une carte au milieu de l'interface
def afficher_carte_milieu():
    global nombre_clics_retourne
    global nombre_clics
    global joueur_actuel
    global carte_retournee

    if nombre_clics < 2 and nombre_clics_retourne < 2:
        nombre_clics += 1
        nombre_clics_retourne += 1

        fenetre = tk.Toplevel()
        fenetre.title("Carte au milieu")

        # Créer une liste de cartes restantes
        cartes_restantes = [carte for carte in liste_cartes if carte not in joueur_nord + joueur_sud + joueur_est + joueur_ouest]

        # Sélectionner aléatoirement une carte parmi les cartes restantes
        carte_milieu = random.choice(cartes_restantes)

        carte_retournee = carte_milieu  # Mettre à jour la carte retournée

        chemin_image = cartes[carte_milieu]
        image = Image.open(chemin_image)
        image = image.resize((96, 130), Image.BILINEAR)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(fenetre, image=photo)
        label.image = photo
        label.pack(padx=10, pady=10)

        # Afficher les boutons "oui" et "non" pour le joueur actuel
        bouton_oui = tk.Button(fenetre, text="Oui", command=lambda: prendre_carte_milieu(True, fenetre))
        bouton_oui.pack(side=tk.LEFT, padx=5, pady=5)

        bouton_non = tk.Button(fenetre, text="Non", command=lambda: prendre_carte_milieu(False, fenetre))
        bouton_non.pack(side=tk.LEFT, padx=5, pady=5)

        if nombre_clics_retourne == 2:
            bouton_carte_milieu.config(state=tk.DISABLED)  # Désactiver le bouton après 2 clics
            if nombre_clics == 2:
                messagebox.showinfo("Fin du jeu temporaire", "Aucun joueur n'a pris la carte.")  # Afficher un message
                nombre_clics = 0  # Réinitialiser le nombre de clics
                nombre_clics_retourne = 0  # Réinitialiser le nombre de clics sur le bouton "Retourne"

            if nombre_clics == 2:
                if joueur_actuel == "nord":
                    joueur_actuel = "est"
                elif joueur_actuel == "est":
                    joueur_actuel = "sud"
                elif joueur_actuel == "sud":
                    joueur_actuel = "ouest"
                elif joueur_actuel == "ouest":
                    joueur_actuel = "nord"

                messagebox.showinfo("Fin du jeu temporaire", "Aucun joueur n'a pris la carte.")  # Afficher un message
                nombre_clics = 0  # Réinitialiser le nombre de clics


def retour_menu():
    # Fonction pour retourner au menu principal
    racine.destroy()
    # Lancer le script menu.py
    subprocess.run(["python", "menu.py"])


# Variable pour suivre le nombre de fois où le bouton "Non" a été cliqué consécutivement
nombre_non_consecutifs = 0


# Fonction pour gérer le choix du joueur sur la carte au milieu
def prendre_carte_milieu(accepter, fenetre):
    global joueur_actuel
    global nombre_clics
    global nombre_non_consecutifs

    if accepter:
        if joueur_actuel == "nord":
            joueur_nord.append(carte_retournee)
        elif joueur_actuel == "est":
            joueur_est.append(carte_retournee)

        bouton_carte_milieu.config(state=tk.DISABLED)  # Désactiver le bouton "Retourne"
        fenetre.destroy()  # Fermer la fenêtre de la carte au milieu
    else:
        nombre_non_consecutifs += 1  # Incrémenter le compteur de non consécutifs

        if nombre_non_consecutifs >= 4:
            fenetre.destroy()  # Fermer la fenêtre de la carte au milieu
            nombre_non_consecutifs = 0  # Réinitialiser le compteur de non consécutifs

        else:
            # Passer au joueur suivant
            if joueur_actuel == "nord":
                joueur_actuel = "est"
            elif joueur_actuel == "est":
                joueur_actuel = "sud"
            elif joueur_actuel == "sud":
                joueur_actuel = "ouest"
            elif joueur_actuel == "ouest":
                joueur_actuel = "nord"

    nombre_clics = 0  # Réinitialiser le nombre de clics

# Créer la fenêtre principale
racine = tk.Tk()
racine.title("Jeu de cartes")

# Charger l'image d'arrière-plan
background_image = Image.open("images/verdebelote.jpg")
background_image = background_image.resize((1300, 840), Image.BILINEAR)
background_photo = ImageTk.PhotoImage(background_image)

# Afficher l'arrière-plan
background_label = tk.Label(racine, image=background_photo)
background_label.image = background_photo
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Boutons pour afficher les cartes de chaque joueur
bouton_nord = tk.Button(racine, text="Joueur Nord", command=lambda: afficher_cartes_joueur(joueur_nord))
bouton_nord.place(relx=0.5, rely=0.25, anchor="center")

bouton_sud = tk.Button(racine, text="Joueur Sud", command=lambda: afficher_cartes_joueur(joueur_sud))
bouton_sud.place(relx=0.5, rely=0.75, anchor="center")

bouton_est = tk.Button(racine, text="Joueur Est", command=lambda: afficher_cartes_joueur(joueur_est))
bouton_est.place(relx=0.75, rely=0.5, anchor="center")

bouton_ouest = tk.Button(racine, text="Joueur Ouest", command=lambda: afficher_cartes_joueur(joueur_ouest))
bouton_ouest.place(relx=0.25, rely=0.5, anchor="center")

# Bouton pour afficher une carte au milieu
bouton_carte_milieu = tk.Button(racine, text="Retourne", command=afficher_carte_milieu)
bouton_carte_milieu.place(relx=0.5, rely=0.5, anchor="center")

# Bouton pour revenir au menu principal
bouton_menu = tk.Button(racine, text="Menu", command=retour_menu)
bouton_menu.place(relx=0.05, rely=0.05)

racine.mainloop()