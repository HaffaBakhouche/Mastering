import qrcode
import random
import os

tmp = "azertyuiopqsdfghjklmwxcvbn7894561230AZERTYUIOPQSDFGHJKLMWXCVB"
len = int(input("Taille des charactères pour chaque QR code ? "))
taille = int(input("Combien de QR codes voulez vous générer ? "))
count = 0

while count != taille:
        # Pour chaque QR code dans cette boucle, on va ajouter de la data random
        # pour que le nouveau QR diffère de l'ancien loopé
        # On encode le QR code avec la data générée
        New_Random_QR_Code = qrcode.make(random.sample(tmp, len))
        # Charactères random pour le titre du file + .png"
        p = "".join(random.sample(tmp, len))
        New_Random_QR_Code.save(p + ".png")
        count+=1
else:
        print("QR codes générés avec succès !")
        quit()