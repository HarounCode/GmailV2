import smtplib
import tkinter
from tkinter import filedialog
from email.message import EmailMessage
import pathlib
import mimetypes


fenetre = tkinter.Tk()
fenetre.title("Gmail v2")
fenetre.resizable(False,False)
fenetre.geometry("600x600")
fenetre.configure(bg="green")


def envoyer_email():
    contenu_expediteur = entree_expediteur.get()
    contenu_mot_de_passe = entree_mot_de_passe.get()
    contenu_destinataire = entree_destinataire.get()
    contenu_sujet = entree_sujet.get()
    contenu_message = entree_message.get("1.0",tkinter.END)

    email_message = EmailMessage()
    email_message["From"] = contenu_expediteur
    email_message["To"] = contenu_destinataire
    email_message["Subject"] = contenu_sujet
    email_message.set_content(contenu_message)
   
    if chemin:
        fichier = pathlib.Path(chemin)
        contenu_fichier = fichier.read_bytes()

        type_fichier, encodage = mimetypes.guess_type(fichier.name)

    if type_fichier:
        maintype, subtype = type_fichier.split("/")
        filename=fichier.name
    else:
        maintype = "application"
        subtype = "octet-stream"


    email_message.add_attachment(
        contenu_fichier,
        maintype=maintype,
        subtype=subtype,
        filename=fichier.name
    )
        
        

    

    try:
        serveur = smtplib.SMTP("smtp.gmail.com",587)
        serveur.starttls()
        serveur.login(contenu_expediteur,contenu_mot_de_passe)
        serveur.send_message(email_message)

        message_resultat.config(text="Email Envoyé Avec Succès !")
        message_resultat.grid(row=6, column=0, columnspan=2)

    except:
        message_resultat.config(text="Impossible De Se Connecter à Votre Adresse Mail")
        message_resultat.grid(row=6, column=0, columnspan=2)

    finally:
        try:
            serveur.quit()
        except:
            pass


expediteur = tkinter.Label(fenetre,text="Expediteur  :",fg="black")
expediteur.grid(row=0,column=0)

entree_expediteur = tkinter.Entry(fenetre)
entree_expediteur.grid(row=0,column=1)


mot_de_passe = tkinter.Label(fenetre,text="Mot De Passe D'Application  :",fg="black")
mot_de_passe.grid(row=1,column=0)

entree_mot_de_passe = tkinter.Entry(fenetre,show="*")
entree_mot_de_passe.grid(row=1,column=1)


destinataire = tkinter.Label(fenetre,text="Destinataire  :",fg="black")
destinataire.grid(row=2,column=0)

entree_destinataire = tkinter.Entry(fenetre)
entree_destinataire.grid(row=2,column=1)


sujet = tkinter.Label(fenetre,text="Sujet  :",fg="black")
sujet.grid(row=3,column=0)

entree_sujet = tkinter.Entry(fenetre)
entree_sujet.grid(row=3,column=1)


message = tkinter.Label(fenetre,text="Message : ",fg="black")
message.grid(row=4,column=0)

entree_message = tkinter.Text(fenetre,width=40,height=7)
entree_message.grid(row=4,column=1)


bouton = tkinter.Button(fenetre,text="Envoyer",fg="black",command=envoyer_email)
bouton.grid(row=5,column=1,pady=20)

chemin=""

def envoyer_piece_jointe():
    global chemin
    chemin = filedialog.askopenfilename()
    
    
    
    


piece_jointe = tkinter.Button(fenetre,text="📎 Ajouter une pièce jointe",fg="black",command=envoyer_piece_jointe)

piece_jointe.grid(row=5,column=0)


message_resultat = tkinter.Label(fenetre,text="",fg="black")


fenetre.mainloop()
