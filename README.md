# GmailV2 📧

### Application de messagerie électronique développée en Python

**GmailV2** est une application de bureau développée en Python permettant d'envoyer des courriers électroniques via les serveurs SMTP de Gmail, à travers une interface graphique simple et accessible.

Ce projet a été conçu dans une démarche d'apprentissage et de développement informatique. Il met en œuvre plusieurs fonctionnalités essentielles de la communication électronique, notamment la création de messages, la gestion des informations de l'expéditeur et du destinataire, ainsi que l'ajout de pièces jointes.

L'application s'appuie sur les bibliothèques natives de Python pour gérer la composition des e-mails, la communication avec les serveurs de messagerie et la création de son interface graphique.

---

## ✨ Fonctionnalités principales

### 📩 Envoi de courriers électroniques
GmailV2 permet de composer et d'envoyer des e-mails directement depuis son interface graphique.

L'utilisateur peut renseigner :
- L'adresse e-mail de l'expéditeur.
- Le mot de passe d'application associé au compte Gmail.
- L'adresse e-mail du destinataire.
- Le sujet du message.
- Le contenu du courrier électronique.

### 📎 Gestion des pièces jointes
L'application intègre un système de sélection de fichiers permettant d'ajouter une pièce jointe à un courrier électronique.

Grâce aux modules `pathlib` et `mimetypes`, le programme peut lire le fichier sélectionné et déterminer son type MIME afin de préparer son intégration au message.

### 🖥️ Interface graphique
L'application possède une interface graphique développée avec Tkinter.

Elle regroupe les différents champs nécessaires à la rédaction d'un e-mail, ainsi que des boutons permettant d'ajouter une pièce jointe et de déclencher l'envoi.

### 🔐 Communication sécurisée
La communication avec les serveurs SMTP de Gmail utilise une connexion SMTP avec activation de TLS via STARTTLS.

L'authentification s'effectue à l'aide des identifiants fournis par l'utilisateur et d'un mot de passe d'application Gmail.

### 📊 Gestion des résultats
Après une tentative d'envoi, l'application affiche un message indiquant si l'opération a réussi ou si une erreur de connexion est survenue.

---

## 🛠️ Technologies et bibliothèques

| Technologie | Utilisation |
|---|---|
| Python | Langage principal |
| Tkinter | Création de l'interface graphique |
| smtplib | Communication avec le serveur SMTP |
| email.message | Construction des messages électroniques |
| pathlib | Gestion et lecture des fichiers |
| mimetypes | Identification des types MIME |

---

## ⚙️ Fonctionnement technique

Le fonctionnement de GmailV2 repose sur plusieurs étapes :

1. **Saisie des informations :** l'utilisateur renseigne les informations nécessaires à la création du courrier électronique.
2. **Construction du message :** le programme utilise `EmailMessage` pour définir l'expéditeur, le destinataire, le sujet et le contenu du message.
3. **Préparation de la pièce jointe :** lorsqu'un fichier est sélectionné, son contenu est lu et intégré au message.
4. **Connexion au serveur SMTP :** le programme établit une connexion avec `smtp.gmail.com` sur le port 587.
5. **Sécurisation de la connexion :** STARTTLS est activé avant l'authentification.
6. **Authentification et envoi :** le programme s'authentifie auprès du serveur et transmet le message.
7. **Retour utilisateur :** l'interface affiche le résultat de la tentative d'envoi.

---

## 📚 Objectifs pédagogiques

GmailV2 constitue également un projet pratique permettant d'approfondir plusieurs notions de programmation Python :

- Programmation orientée événements.
- Création et organisation d'interfaces graphiques.
- Utilisation des bibliothèques standard de Python.
- Communication avec des serveurs SMTP.
- Manipulation de messages électroniques.
- Gestion des fichiers et des pièces jointes.
- Gestion des exceptions.
- Utilisation de protocoles de communication sécurisés.

---

## 🔒 Sécurité et utilisation responsable

GmailV2 est un projet éducatif indépendant, développé dans un objectif d'apprentissage et d'expérimentation.

Quelques précautions importantes :
- Utiliser uniquement des comptes et des adresses e-mail pour lesquels une autorisation existe.
- Ne jamais partager ses identifiants ou ses mots de passe d'application.
- Ne pas publier de données sensibles dans le dépôt GitHub.
- Respecter les règles de sécurité et les conditions d'utilisation des services Google.
- Utiliser l'application uniquement dans un cadre légal et autorisé.

**Remarque :** le programme utilise actuellement une authentification SMTP par mot de passe d'application. Il ne constitue pas une intégration OAuth 2.0.

---

## ⚠️ Limitations actuelles

Cette version de GmailV2 possède un fonctionnement volontairement simple.

Certaines améliorations pourront être envisagées dans de futures versions :
- Amélioration de la gestion des erreurs.
- Validation des adresses électroniques.
- Gestion de plusieurs destinataires.
- Possibilité de sélectionner plusieurs pièces jointes.
- Amélioration de l'interface graphique.
- Sécurisation renforcée de la gestion des identifiants.
- Intégration éventuelle d'une authentification OAuth 2.0.

---

## 👨‍💻 Auteur

**Haroun Studio**

Projet personnel développé en Python dans le cadre d'un apprentissage approfondi de la programmation et de la création d'applications de bureau.

---

## 📄 Licence et propriété

GmailV2 est un projet indépendant et éducatif.

Gmail et Google sont des marques appartenant à Google LLC. Ce projet n'est ni affilié à Google, ni sponsorisé, ni officiellement approuvé par Google.

---

**GmailV2 — Simple. Fonctionnel. Python.**
