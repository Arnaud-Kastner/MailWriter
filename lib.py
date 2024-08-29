#################################
### Created by Arnaud KASTNER ###
#################################

import random
from pathlib import Path
import codecs
import glob

class Redactor :
    def __init__ (self) :                
        #Définition du texte à rechercher dans les templates
        self.entreprise_search = "~Entreprise~"
        self.date_search = "~Date~"
        self.personne_search = "~Personne~"
    
        # Chemin pour aller vers le dossier contenant les templates
        self.folder_path =Path("C:\\").joinpath("Users\\").joinpath("akastner02\\").joinpath("Desktop\\").joinpath("Mails\\").joinpath("Template_reponse\\")
        # self.g_folder_path = glob.glob('C:\\Users\\akastner02\\Desktop\\Mails\\Template_reponse\*.txt')

    # Compte le nombre de fichier dans le dossier pour définir le nombre max 
    def nb_finder(self) :
        self.nb_file = 0
        for path in Path(self.folder_path).iterdir():
            if path.is_file():
                self.nb_file += 1
        return self.nb_file
        # self.nb_file = glob.glob(self.g_folder_path)
        # print (len(self.nb_file))

      
    #génère le nombre aléatoire qui va définir le template à utiliser
    def randomizer(self) :
        self.choice = random.randint(1,self.nb_file)
        self.template_path = self.folder_path.joinpath(str(self.choice)+".txt")
        return self.template_path
        print(self.template_path)
        return self.choice
 
    #création du fichier txt contenant le mail modifié
    def file_writer(self) :
        with codecs.open(self.template_path,'r','utf-8') as file :
            self.data = file.read()
            return self.data
        
    def list_finder(self) :
        g_folder_path =  'C:\\Users\\akastner02\\Desktop\\Mails\\Template_reponse\*.txt'
        file_list = glob.glob(g_folder_path)
        print(len(file_list))        
    
    #Fonction que vérifie que les différents fichiers txt existent
    def ver_file_exist(self,file_name) :
        path_to_verify = self.folder_path.joinpath(str(file_name))
        if Path.exists(path_to_verify) == False:
            return False        
        else :
            return True
 
    #Fonction qui va créer le nouveau template       
    def file_create(self,file_name,file_text) :
        new_file_path = self.folder_path.joinpath(str(file_name))
        with codecs.open(new_file_path,'w','utf-8') as mess :
            mess.write(file_text)
        return True
