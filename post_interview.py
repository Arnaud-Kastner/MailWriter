#################################
### Created by Arnaud KASTNER ###
#################################

import random
from pathlib import Path
import codecs

#Définition du texte à rechercher dans les templates
entreprise_search = "xxx"
date_search = "zzz"
personne_search = "yyy"
poste_search = "vvv"

#Variables définissant le nombre de template
nb_min = 1
nb_max = 10

#génère le nombre aléatoire qui va définir le template à utiliser
choice = random.randint(nb_min,nb_max)

#données des entrepises
if choice == 3 :
    print("Pas besoin de définir le nom de l'entreprise")
entreprise_replace = str(input("Nom de l'entreprise : "))
personne_replace = str(input("Nom de la personne : "))
date_replace = str(input("Date de l entretien : "))
if choice == 2 or choice == 4 :
    poste_replace = str(input("Intitulé du poste : "))
   
#chemin des dossiers template et mail
template_path = Path("C:\\").joinpath("Users\\").joinpath("path\\").joinpath(str(choice)+".txt")
mail_path = Path("C:\\").joinpath("Users\\").joinpath("path\\").joinpath("réponse entretien"+entreprise_replace+".txt")

#création du fichier txt contenant le mail modifié
with codecs.open(template_path,'r','utf-8') as file :
    data = file.read()
    data = data.replace(entreprise_search,entreprise_replace)
    data = data.replace(date_search,date_replace)
    data = data.replace(personne_search,personne_replace)
    
    if choice == 2 or choice == 4:
        data = data.replace(poste_search,poste_replace)
        
    print(data)
    with codecs.open(mail_path,'w','utf-8') as mess :
       mess.write(data)
