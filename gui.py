#################################
### Created by Arnaud KASTNER ###
#################################

import tkinter as tk
import pyperclip as pyper

# import script.py as redac
class MyGUI:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Mail Redactor")
        
        self.titre = tk.Label (self.root, text="Ecrire un mail", font=('Arial', 20))
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
        
        self.test_button = tk.Button(self.root, text="Test print", command=self.getinfo)
        self.test_button.pack(padx=10,pady=20)
        
        self.root.mainloop()

    def getinfo(self) :
        self.personne = self.En_per.get()
        self.date = self.En_dat.get()
        self.entreprise = self.En_ent.get()
        self.popup()
    
    def popup(self) :
        popup = tk.Toplevel()
        label = tk.Label(popup, text = self.date)
        label.grid()
        close_btn = tk.Button(popup, text ="Close", command= popup.destroy)
        close_btn.grid(row = 2, column = 2)
        copy_btn = tk.Button(popup, text="Copy", command =self.copy)
        copy_btn.grid(row = 2, column= 0)
        
        def copy(self) :
         pyper.copy(self.date)
        
MyGUI()
