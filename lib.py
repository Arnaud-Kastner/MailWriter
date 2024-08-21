#################################
### Created by Arnaud KASTNER ###
#################################

import random
from pathlib import Path
import codecs

class Redactor :
    
    #Définition du texte à rechercher dans les templates
    entreprise_search = "~Entreprise~"
    date_search = "~Date~"
    personne_search = "~Personne~"
    poste_search = "~Poste~"
    
    # Chemin pour aller vers le dossier contenant les templates
    global folder_path 
    folder_path =Path("C:\\").joinpath("Users\\").joinpath("akastner02\\").joinpath("Desktop\\").joinpath("Mails\\").joinpath("Template_reponse\\")
       
    # Compte le nombre de fichier dans le dossier pour définir le nombre max 
    def nb_finder() :
        global nb_file
        nb_file = 0
        for path in Path(folder_path).iterdir():
            if path.is_file():
                nb_file += 1
        print (nb_file)
        # return nb_file

      
    #génère le nombre aléatoire qui va définir le template à utiliser
    def randomizer(file) :
        choice = random.randint(1,file)
        global template_path
        template_path = folder_path.joinpath(str(choice)+".txt")
        return template_path
        print(choice)
 
    #création du fichier txt contenant le mail modifié
    def file_writer(template_path) :
        with codecs.open(template_path,'r','utf-8') as file :
            data = file.read()
            # data = data.replace(entreprise_search,GUI.self.entreprise)# Faire en sorte de ramener les infos depuis l'UI
            # data = data.replace(date_search,GUI.self.date)# Faire en sorte de ramener les infos depuis l'UI
            # data = data.replace(personne_search,GUI.self.personne)# Faire en sorte de ramener les infos depuis l'UI
            return data
        
    nb_finder()
