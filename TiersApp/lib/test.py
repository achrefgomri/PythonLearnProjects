from tkinter import *

fenetre=Tk()
barre_de_texte=Label(fenetre,text="afficher qqe chose")
barre_de_texte.pack()
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()
var_case = IntVar()
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()
fenetre.mainloop()


#if __name__=="__main__":
 #   main()
