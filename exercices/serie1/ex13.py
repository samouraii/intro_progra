#!/usr/bin/python

nb_batiments = int(input("Combien de bâtiment(s) à contruire ? : "))
ressources_necessaires = int(input("Combien de ressources nécessaires par bâtiment ? : "))
ressources_disponibles = int(input("Combien de ressources possèdons-nous ? : "))

nb_batiments_valide = nb_batiments != 0 and nb_batiments <= 15 #si cela vaux -1 cela passe
ressources_insuffisantes = nb_batiments * ressources_necessaires > ressources_disponibles # si le nombre de ressource est exactement le meme que ce que nous avons besoin on doit pouvoir construire
peut_construire =  nb_batiments != 0 and nb_batiments <= 15 and nb_batiments * ressources_necessaires <= ressources_disponibles # tu as déja virifier les condition et tu refais la même chose, utilise les variables déjà défini.

print("\nLe nombre de bâtiment est-il valide ? : {}".format(nb_batiments_valide))
print("Les ressources sont-elles insuffisantes ? : {}".format(ressources_insuffisantes))
print("Pouvez-vous contruire ? : {}".format(peut_construire))

