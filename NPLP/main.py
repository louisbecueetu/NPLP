import pylrc
import time
import datetime
import pyautogui
import random
import tkinter as tk
from tkinter import ttk

choix = ["Celine Dion - Pour que tu m'aimes encore", "Céline Dion - Sous le vent", "Marc Lavoine - Elle A Les Yeux Revolver", "Dadju - Reine"]
link = ["lrc\Celine Dion - Pour que tu m'aimes encore.lrc",'lrc/Céline Dion - Sous le vent.lrc', 'lrc/Marc Lavoine - Elle A Les Yeux Revolver.lrc', "lrc\Dadju - Reine.lrc"]

def lyrics(adresse):
    flrc_file = open(adresse)
    lrc_string = ''.join(flrc_file.readlines())
    flrc_file.close()

    subs = pylrc.parse(lrc_string)
    lrc_string = subs.toLRC() # convert to lrc string
    data = lrc_string.split('\n')
    lyrics = []
    c = False
    for l in data:
        if c :
            lyrics.append(l)
        if l == '':
            c = True
    lyrics.append(" ")
    return lyrics

def play(lyrics):
    code = random.randint(5, len(lyrics)-5)
    pyautogui.press('playpause')
    prec_time = datetime.timedelta(minutes=00, seconds=00, microseconds=00)
    i = 0
    while i <= len(lyrics) and i != code:
        l = lyrics[i]
        affiche = lyrics[i-1]
        print(affiche[10:len(affiche)])
        t = datetime.timedelta(minutes=int(l[1:3]), seconds=int(l[4:6]), microseconds=int(l[7:9]))
        wait_time = t - prec_time
        time.sleep(wait_time.total_seconds())
        prec_time = t
        i += 1
    pyautogui.press('playpause')
    l = lyrics[i][10:len(l)]
    print(codage(l))
    res = int(input("Voulez-vous les intiales 1-oui 2-non:"))
    if res == 1:
        print(codage_intiale(l))
    str(input("Quelle est votre réponse :"))
    print("la réponse était :")
    print(l)

def codage(ligne):
    out = ""
    for c in ligne:
        if c == " ":
            out += " "
        else :
            out += "_"
    return out

def codage_intiale(ligne):
    ligne = ligne.split(" ")
    out = ""
    for elt in ligne:
        out += elt[0] + "_" * (len(elt)-1) + " "
    return out

def action(event):
	# Obtenir l'élément sélectionné
    select = listeCombo.get()
    print("Vous avez sélectionné : '", select,"'")

if __name__ == "__main__":
    # root = tk.Tk() 
    # root.geometry('300x200')

    # labelChoix = tk.Label(root, text = "Chansons disponible :")
    # labelChoix.pack()
    # # 3) - Création de la Combobox via la méthode ttk.Combobox()
    # listeCombo = ttk.Combobox(root, values=choix)
    
    # # 4) - Choisir l'élément qui s'affiche par défaut
    # listeCombo.current(0)

    # listeCombo.pack()
    # bouton= tk.Button(root, text="choisir", action())
    # bouton.pack()
    # listeCombo.bind("<<ComboboxSelected>>", action)
    # root.mainloop()
    print("Chansons disponible :")
    c = 1
    for cle in choix:
        print(str(c) +" - " +  cle)
        c += 1
    inp = int(input("Quelle numéro de chanson choisisez-vous : "))

    adresse = link[inp-1]
    play(lyrics(adresse))




