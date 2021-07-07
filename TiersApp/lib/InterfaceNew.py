from tkinter import *
from tkinter.messagebox import *


def mana3rech():
    fenetre=Tk()

    canvas1 =Canvas(fenetre, width = 400, height = 300)
    canvas1.pack()

    titre=Label(fenetre,text="Formulaire")
    titre.pack()

    nom=Label(fenetre,text="Votre Nom: ")
    nom.pack()


    entry_nom = Entry(fenetre) 
    entry_nom.pack()

    adresse=Label(fenetre,text="adresse: ")
    adresse.pack()


    entry_adresse = Entry (fenetre) 
    entry_adresse.pack()

    Type=Label(fenetre,text="Type: ")
    Type.pack()


    entry_type = Entry (fenetre) 
    entry_type.pack()

    note=Label(fenetre,text="Note: ")
    note.pack()


    entry_note = Entry (fenetre) 
    entry_note.pack()

    canvas1.create_window(200, 60, window=titre)

    canvas1.create_window(70, 100, window=nom)

    canvas1.create_window(200, 100, window=entry_nom)

    canvas1.create_window(70, 140, window=adresse)
    canvas1.create_window(200, 140, window=entry_adresse)

    canvas1.create_window(70, 180, window=Type)
    canvas1.create_window(200, 180, window=entry_type)

    canvas1.create_window(70, 220, window=note)
    canvas1.create_window(200, 220, window=entry_note)
    return fenetre,canvas1

    #bouton_envoyer = Button(fenetre, text="Valider", fg="red",command=fenetre.cliquer)
    #bouton_envoyer.pack(side="right")
def main ():
    fenetre=Tk()

    canvas1 =Canvas(fenetre, width = 400, height = 300)
    canvas1.pack()

    titre=Label(fenetre,text="Formulaire")
    titre.pack()

    nom=Label(fenetre,text="Votre Nom: ")
    nom.pack()


    entry_nom = Entry (fenetre) 
    entry_nom.pack()

    adresse=Label(fenetre,text="adresse: ")
    adresse.pack()


    entry_adresse = Entry (fenetre) 
    entry_adresse.pack()

    Type=Label(fenetre,text="Type: ")
    Type.pack()


    entry_type = Entry (fenetre) 
    entry_type.pack()

    note=Label(fenetre,text="Note: ")
    note.pack()


    entry_note = Entry (fenetre) 
    entry_note.pack()

    canvas1.create_window(200, 60, window=titre)

    canvas1.create_window(70, 100, window=nom)

    canvas1.create_window(200, 100, window=entry_nom)

    canvas1.create_window(70, 140, window=adresse)
    canvas1.create_window(200, 140, window=entry_adresse)

    canvas1.create_window(70, 180, window=Type)
    canvas1.create_window(200, 180, window=entry_type)

    canvas1.create_window(70, 220, window=note)
    canvas1.create_window(200, 220, window=entry_note)
    


    boutton_envoyer = Button(fenetre, text ="Sauvegarder", command = helloCallBack)
    boutton_envoyer.pack()
    canvas1.create_window(200, 260, window=boutton_envoyer)
def helloCallBack():
    if entry_nom.get() != 'achref':
        showwarning('ALERT!','le nom doit etre achref')
    elif entry_type.get() not in ('a','b','c','d'):
        showwarning('ALERT!','type doit etre a,b,c ou d !!!!')
    else:
        if not askyesno('Contact enregister','Le contact que vous venez d entrée est enregistré avec succès, Vous voulez entrer un autre?'):
            print('fenetre.destroy()')
        else:
            #fenetre.destroy
            mana3rech()
    #fenetre.mainloop()

if __name__=='__main__':
    main()
