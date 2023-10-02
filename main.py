import sys
actions = [
    "Ajouter un élément à la liste de courses",
    "Retirer un élément de la liste de courses",
    "Afficher les éléments de la liste de courses",
    "Vider la liste de courses",
    "Quitter le programme"
]

liste = []

while True:
    print("-" * 15)
    print("Choisissez parmi les 5 options suivantes :")
    for i, element in enumerate(actions):
        print(i + 1, element)
    choix = input("Votre choix : ")
    print("-" * 15)

    if choix.isdigit():
        choix = int(choix) 
        if choix == 1:
            element_a_ajouter = input("Entrer le nom d'un élément à ajouter à la liste de courses : ")
            if element_a_ajouter != "":
                liste.append(element_a_ajouter)
                print(element_a_ajouter, "a bien été ajouté à la liste ")
            else:
                print("Veuillez entrer un nom.")
        elif choix == 2:
            print("Éléments de la liste de courses :")
            for i, element in enumerate(liste):
                print(i + 1, element)
            retirer = input("Sélectionnez le numéro de l'élément à retirer (ou '0' pour annuler) : ")
            if retirer.isdigit():
                retirer = int(retirer)
                if retirer > 0 and retirer <= len(liste):
                    element_retirer =liste.pop(retirer - 1)  
                    print(f"({retirer}) {element_retirer} , a bien été retirer de la liste")
                else:
                    print("Numéro d'élément invalide.")
            elif retirer == '0':
                print("Annulation de la suppression.")
            else:
                print("Veuillez entrer un numéro valide.")
        elif choix == 3:
            print("Éléments de la liste de courses :")
            if not(liste) :
                print("La liste est vide !!!!")
            else :
                for item in liste:
                    print(item)
        elif choix == 4:
            liste.clear()
            print("La liste de courses a été vidée.")
        elif choix == 5:
            print("Vous avez quitté le programme.")
            sys.exit()
        else:
            print("Veuillez entrer un nombre de 1 à 5.")
    else:
        print("Veuillez entrer un nombre valide (de 1 à 5).")
