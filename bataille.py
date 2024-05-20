import os
import random
import tkinter as tk
import time


class Carte:
    def __init__(self, nom, valeur, chemin_image):
        self.nom = nom
        self.valeur = valeur
        self.chemin_image = chemin_image


class AffichageCarte:
    def __init__(self, fenetre, cartes, position_y):
        self.fenetre = fenetre
        self.frames_carte = []
        for i, (nom_carte, carte) in enumerate(cartes.items()):
            image_carte = tk.PhotoImage(file=carte.chemin_image)
            label_carte = tk.Label(fenetre, image=image_carte)
            label_carte.image = image_carte
            label_carte.grid(row=position_y, column=i)
            self.frames_carte.append(label_carte)


def comparer_cartes():
    global cartesJ1, cartesJ2, bataille
    bataille = []
    if cartesJ1 and cartesJ2:
        carte1_J1 = next(iter(cartesJ1.values()))
        carte1_J2 = next(iter(cartesJ2.values()))

        if carte1_J1.valeur == carte1_J2.valeur:
            print("Bataille ! Les deux joueurs ont la même carte de valeur",
                  carte1_J1.valeur)
            bataille.append(carte1_J1)
            bataille.append(carte1_J2)
            cartesJ1.pop(carte1_J1.nom)
            cartesJ2.pop(carte1_J2.nom)
            nouvelle_bataille()
        elif carte1_J1.valeur > carte1_J2.valeur:
            print("Le joueur 1 gagne la manche avec la carte",
                  carte1_J1.nom, 'et prend la carte du joueur 2', carte1_J2.nom)
            cartesJ1[carte1_J1.nom] = cartesJ1.pop(carte1_J1.nom)
            cartesJ1[carte1_J2.nom] = cartesJ2.pop(carte1_J2.nom)
        else:
            print("Le joueur 2 gagne la manche avec la carte",
                  carte1_J2.nom, 'et prend la carte du joueur 1', carte1_J1.nom)
            cartesJ2[carte1_J2.nom] = cartesJ2.pop(carte1_J2.nom)
            cartesJ2[carte1_J1.nom] = cartesJ1.pop(carte1_J1.nom)

    actualiser_affichage()


def nouvelle_bataille():
    global cartesJ1, cartesJ2, bataille

    while len(cartesJ1) >= 2 and len(cartesJ2) >= 2:
        carte1_J1 = next(iter(cartesJ1.values()))
        carte1_J2 = next(iter(cartesJ2.values()))
        carte2_J1 = list(cartesJ1.values())[1]
        carte2_J2 = list(cartesJ2.values())[1]

        bataille.extend([carte1_J1, carte1_J2, carte2_J2, carte2_J1])

        cartesJ1.pop(carte1_J1.nom)
        cartesJ1.pop(carte2_J1.nom)
        cartesJ2.pop(carte1_J2.nom)
        cartesJ2.pop(carte2_J2.nom)

        if carte2_J1.valeur > carte2_J2.valeur:
            print("Le joueur 1 gagne la bataille avec la carte",
                  carte2_J1.nom, 'et prend les cartes du joueur 2')
            for carte in bataille:
                cartesJ1[carte.nom] = carte
            break
        elif carte1_J1.valeur < carte1_J2.valeur:
            print("Le joueur 2 gagne la bataille avec la carte",
                  carte1_J2.nom, 'et prend les cartes du joueur 1')
            for carte in bataille:
                cartesJ2[carte.nom] = carte
            break
        else:
            print(
                "Nouvelle bataille ! Les deux joueurs ont de nouveau la même carte de valeur", carte1_J1.valeur)


def tirage_automatique():
    global auto_tirage_actif
    auto_tirage_actif = True
    while auto_tirage_actif and cartesJ1 and cartesJ2:
        comparer_cartes()
        fenetre_principale.update()
        time.sleep(0.01)

def actualiser_affichage():
    global frames_cartes_J1, frames_cartes_J2
    for frames_cartes in [frames_cartes_J1, frames_cartes_J2]:
        for frame in frames_cartes:
            for label_carte in frame.frames_carte:
                label_carte.grid_forget()

    frames_cartes_J1.clear()
    frames_cartes_J2.clear()
    frames_cartes_J1.append(AffichageCarte(fenetre_principale, cartesJ1, 0))
    frames_cartes_J2.append(AffichageCarte(fenetre_principale, cartesJ2, 1))


def arreter_tirage_auto():
    global auto_tirage_actif
    auto_tirage_actif = False


script_directory = os.path.dirname(os.path.abspath(__file__))
dossier_cartes = os.path.join(script_directory, "cartes")

class Carte:
    def __init__(self, nom, valeur, image_path):
        self.nom = nom
        self.valeur = valeur
        self.chemin_image = image_path

dossier_cartes = "images"

cartes = {
    "As de Coeur": Carte("As de Coeur", 14, os.path.join(dossier_cartes, "14kupa.png")),
    "As de Pique": Carte('As de Pique', 14, os.path.join(dossier_cartes, "14pika.png")),
    "As de Carreau": Carte("As de Carreau", 14, os.path.join(dossier_cartes, "14karo.png")),
    "As de Trèfle": Carte('As de Trèfle', 14, os.path.join(dossier_cartes, "14spatiq.png")),
    "Roi de Pique": Carte("Roi de Pique", 13, os.path.join(dossier_cartes, "13pika.png")),
    "Roi de Coeur": Carte("Roi de Coeur", 13, os.path.join(dossier_cartes, "13kupa.png")),
    "Roi de Carreau": Carte("Roi de Carreau", 13, os.path.join(dossier_cartes, "13karo.png")),
    "Roi de Trèfle": Carte("Roi de Trèfle", 13, os.path.join(dossier_cartes, "13spatiq.png")),
    "Dame de Pique": Carte("Dame de Pique", 12, os.path.join(dossier_cartes, "12pika.png")),
    "Dame de Coeur": Carte("Dame de Coeur", 12, os.path.join(dossier_cartes, "12kupa.png")),
    "Dame de Carreau": Carte("Dame de Carreau", 12, os.path.join(dossier_cartes, "12karo.png")),
    "Dame de Trèfle": Carte("Dame de Trèfle", 12, os.path.join(dossier_cartes, "12spatiq.png")),
    "Valet de Pique": Carte("Valet de Pique", 11, os.path.join(dossier_cartes, "11pika.png")),
    "Valet de Coeur": Carte("Valet de Coeur", 11, os.path.join(dossier_cartes, "11kupa.png")),
    "Valet de Carreau": Carte("Valet de Carreau", 11, os.path.join(dossier_cartes, "11karo.png")),
    "Valet de Trèfle": Carte("Valet de Trèfle", 11, os.path.join(dossier_cartes, "11spatiq.png")),
    "10 de Pique": Carte("10 de Pique", 10, os.path.join(dossier_cartes, "10pika.png")),
    "10 de Coeur": Carte("10 de Coeur", 10, os.path.join(dossier_cartes, "10kupa.png")),
    "10 de Carreau": Carte("10 de Carreau", 10, os.path.join(dossier_cartes, "10karo.png")),
    "10 de Trèfle": Carte("10 de Trèfle", 10, os.path.join(dossier_cartes, "10spatiq.png")),
    "9 de Pique": Carte("9 de Pique", 9, os.path.join(dossier_cartes, "9pika.png")),
    "9 de Coeur": Carte("9 de Coeur", 9, os.path.join(dossier_cartes, "9kupa.png")),
    "9 de Carreau": Carte("9 de Carreau", 9, os.path.join(dossier_cartes, "9karo.png")),
    "9 de Trèfle": Carte("9 de Trèfle", 9, os.path.join(dossier_cartes, "9spatiq.png")),
    "8 de Pique": Carte("8 de Pique", 8, os.path.join(dossier_cartes, "8pika.png")),
    "8 de Coeur": Carte("8 de Coeur", 8, os.path.join(dossier_cartes, "8kupa.png")),
    "8 de Carreau": Carte("8 de Carreau", 8, os.path.join(dossier_cartes, "8karo.png")),
    "8 de Trèfle": Carte("8 de Trèfle", 8, os.path.join(dossier_cartes, "8spatiq.png")),
    "7 de Pique": Carte("7 de Pique", 7, os.path.join(dossier_cartes, "7pika.png")),
    "7 de Coeur": Carte("7 de Coeur", 7, os.path.join(dossier_cartes, "7kupa.png")),
    "7 de Carreau": Carte("7 de Carreau", 7, os.path.join(dossier_cartes, "7karo.png")),
    "7 de Trèfle": Carte("7 de Trèfle", 7, os.path.join(dossier_cartes, "7spatiq.png")),
}
liste_cartes = list(cartes.values())
random.shuffle(liste_cartes)
cartesJ1 = {}
cartesJ2 = {}
for i in range(0, len(liste_cartes), 2):
    cartesJ1[liste_cartes[i].nom] = liste_cartes[i]
    cartesJ2[liste_cartes[i + 1].nom] = liste_cartes[i + 1]

if __name__ == "__main__":
    fenetre_principale = tk.Tk()
    frames_cartes_J1 = []
    frames_cartes_J2 = []
    frames_cartes_J1.append(AffichageCarte(fenetre_principale, cartesJ1, 0))

    frames_cartes_J2.append(AffichageCarte(fenetre_principale, cartesJ2, 1))
    bouton_tirer = tk.Button(
        fenetre_principale, text="Tirer", command=comparer_cartes)

    bouton_tirer.grid(row=2, columnspan=1)
    message_label = tk.Label(fenetre_principale, text="", font=("Arial", 12))
    message_label.grid(row=2, columnspan=1)
    bouton_auto = tk.Button(
        fenetre_principale, text="Tirage Automatique", command=tirage_automatique)
    bouton_auto.grid(row=4, columnspan=1)

    bouton_arreter_auto = tk.Button(
        fenetre_principale, text="Arrêter Tirage Auto", command=arreter_tirage_auto)
    bouton_arreter_auto.grid(row=5, columnspan=1)

    auto_tirage_actif = False

    fenetre_principale.mainloop()
