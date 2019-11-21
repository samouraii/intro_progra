#!/usr/bin/python

### FONCTION ###
def affiche_echiquier():
    for i in range(8): #pas de range et pas vue les for ....
        if i %2 == 0:
            print("_ # _ # _ # _ #") # "_#" * 4
        else: 
            print("# _ # _ # _ # _")

### MAIN ###
affiche_echiquier()
