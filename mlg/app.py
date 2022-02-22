from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator')

def mlg():
    animals = input('Entrer le nom d\'un animal : ')
    profession = input('Entrer le nom d\'un métier : ')
    cloth = input('Entrer le nom d\'un vêtement : ')
    things = input('Entrer le nom d\'un objet : ')
    name = input('Entrer un prénom : ')
    place = input('Entrer le nom d\'un lieu : ')
    food = input('Entrer le nom d\'un aliment : ')
    
    print(
            f"Dîtes {food}, quand le photographe prend la photo! {name}, doit aller à/au {place} pour aller récupérer les photos de son anniversaire.",
            f"La première photo qu'on a vraiment voulu était un(e) {animals} qui prétendait être un(e) {profession}.",
            f"Nous ressemblions tout les deux à un(e) {things} et nous portions un(e) {cloth}."
         )

# Button to launch the mad libs generator
Button(root, text= 'Le photographe', font ='poppins 14', command= mlg, bg = 'ghost white').place(x=60, y=120)

root.mainloop()