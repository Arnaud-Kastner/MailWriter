#################################
### Created by Arnaud KASTNER ###
#################################

import tkinter as tk
from lib import Redactor

class AddTemplate :
    
    #Initialise la class
    def __init__(self) :
        self.lib = Redactor()
    
    #Lance la fenètre de départ
    def start(self) :
        self.root = tk.Tk()
        self.root.title("Mail Redactor")
        
        self.title = tk.Label(self.root, text = "Add template menu", font=("Arial",20))
        self.title.grid(row=0,column=0)
        
        self.requirement = tk.Label(self.root, text="To successfully create a template you need to follow te following rules :")
        self.requirement.grid(row=1,column=0)
        
        self.requirement_1 = tk.Label(self.root, text="1- To replace the name of the person you want to write use this formula : ~Personne~")
        self.requirement_1.grid(row=2,column=0)
    
        self.requirement_2 = tk.Label(self.root, text="2- To replace the compagny name use this formula : ~Entreprise~")
        self.requirement_2.grid(row=3,column=0)
    
        self.requirement_3 = tk.Label(self.root, text="3- To replace the date of your meeting use this formula : ~Date~")
        self.requirement_3.grid(row=4,column=0)
        
        self.template_entry= tk.Entry(self.root)
        self.template_entry.grid(row=5,column=0)
        
        self.add_btn = tk.Button(self.root,text="Add your template",command=self.get_info)
        self.add_btn.grid(row=6, column=1)
      
        self.root.mainloop()
        
    
    #Récupère les infos et vérifie calcule le nombre de fichier existant
    def get_info(self) :
        self.text = self.template_entry.get()
        self.lib.nb_finder()
        self.new_file_nb_temp = int(self.lib.nb_file) + 1
        self.add_template()
        
    #Fonction qui va configurer le template
    def add_template(self) :
        #Vérifies d'abord que le template n'est pas vide
        if self.text != "":
            #Si il ne l'est pas,vérifies ensuite qu'il n'existe pas un trou dans le nom des fichiers (exp nom : 3.txt)
            for i in range (1,self.new_file_nb_temp) :
                nb_verif = self.lib.ver_file_exist(str(i)+".txt")
                #Définit le nom du nouveau fichier
                if nb_verif == False :
                   self.new_file_nb = str(i)+".txt"
                   break
                else :
                    self.new_file_nb = self.new_file_nb_temp
            #Lance la fonction qui va créer le fichier comportant le template
            self.template_creation()
        #Prévient l'utilisateur que le template est vide
        else :
            self.popup_error()
    
    def template_creation(self) :
        self.lib.file_writer(self.new_file_nb,self.text)
        self.popup_cr()
        
    def popup_cr(self) :
        popup = tk.Toplevel()
        popup.title("Mail Redactor")
        label_ok = tk.Label(popup, text = "Template number "+str(self.new_file_nb)+" has been created")
        label_ok.grid(row=0,column=0)
        label_tot = tk.Label(popup, text = "There is now a total of "+str(self.new_file_nb_temp)+" templates")
        label_tot.grid(row=1,column=0)
        close_btn = tk.Button(popup,text="Close",command=popup.destroy)
        close_btn.grid(row=2,column=1)
        
    def popup_error(self) :
        popup = tk.Toplevel()
        popup.title("Mail Redactor")
        label_error = tk.Label(popup, text= "You can\'t add an empty template")
        label_error.grid()
        close_btn = tk.Button(popup,text="Close",command=popup.destroy)
        close_btn.grid(row=1,column=0)
