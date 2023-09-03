import random

#Generate stories using lists

age = random.randint(12,99)
epoque = random.randint(1,2023)
date = random.randint(1,31)
lieu=["la Tour Eiffeil","le Jardin du Luxembourg","le Panthéon"]
personnage=["Nathanael","Matteo","Quentin","Kamel","Emirhan","Bernabée","Safia","Lucile"]
mois = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']


# Here we basically print the prompt:
print("C'était un beau jour de",date,random.choice(mois),epoque,"après JC\nJ'étais tranquillement en train de me balader vers",random.choice(lieu),"quand soudain",random.choice(personnage),"m'accosta")
print("On tombe immédiatement amoureux l'un de lautre.")
print("Il me fait découvrir la programmation, et j'adore ça. Peut-être que je dois essayer de coder de grandes choses ?")

# Using the asterix operand is useful here so that elements of lists gets outputted without any commas.
# Global format getting outputted = ['Quentin'] --> with * operand, output = Quentin