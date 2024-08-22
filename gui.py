#################################
### Created by Arnaud KASTNER ###
#################################

import tkinter as tk
import pyperclip as pyper
from lib import Redactor 

class MyGUI:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Mail Redactor")
        
        self.titre = tk.Label (self.root, text="Write your mail", font=('Arial', 20))
        self.titre.pack(padx=20,pady=20)
        self.text_ent = tk.Label (self.root, text="Nom de l'entreprise")
        self.text_ent.pack(padx=20,pady=0)
        self.En_ent = tk.Entry(self.root)
        self.En_ent.pack(padx=20,pady=0)
        self.text_dat = tk.Label (self.root, text="Date")
        self.text_dat.pack(padx=20,pady=5)
        
        self.En_dat = tk.Entry(self.root)
        self.En_dat.pack(padx=20,pady=0)
        
        self.text_per = tk.Label (self.root, text="Personne")
        self.text_per.pack(padx=20,pady=5)
        
        self.En_per = tk.Entry(self.root)
        self.En_per.pack(padx=20,pady=0)
        
        self.test_button = tk.Button(self.root, text="Generate", command=self.getinfo)
        self.test_button.pack(padx=10,pady=20)
        
        self.root.mainloop()
    
    def popup(self) :
        popup = tk.Toplevel()
        label = tk.Label(popup, text = self.texte)
        label.grid(row=0, column=1)
        frame = tk.Frame(popup)
        frame.grid(row=1, column=0)
        copy_btn = tk.Button(frame, text="Copy", command =self.copy)
        copy_btn.grid(row=0,column=0)
        retry_btn = tk.Button(frame, text="Retry", command=lambda:[popup.destroy(),self.getinfo()])
        retry_btn.grid(row=0,column=1)
        close_btn = tk.Button(frame, text ="Close", command= popup.destroy)
        close_btn.grid(row=0,column=2)
        
        
    def getinfo(self) :
        self.personne = self.En_per.get()
        self.date = self.En_dat.get()
        self.entreprise = self.En_ent.get()
        self.gpt()
        self.popup()
    
    def copy(self) :
        pyper.copy(self.texte)

    def gpt(self) :
        p1 = Redactor()
        p1.nb_finder()
        p1.randomizer()
        p1.file_writer()
        p1.data = p1.data.replace(p1.entreprise_search,self.entreprise)
        p1.data = p1.data.replace(p1.date_search,self.date)
        p1.data = p1.data.replace(p1.personne_search,self.personne)
        self.texte = p1.data
           
MyGUI()
