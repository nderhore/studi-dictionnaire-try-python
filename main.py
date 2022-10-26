def list_to_dict():
    # Nous avons deux listes, il suffit de les convertir en dictionnaire Python
    list_key: list = ['clef_un', 'clef_deux', 'clef_trois']
    list_value: list = ['value_un', 'value_deux', 'value_trois']

    # 1ere ecriture possible
    # new_dict : dict = dict(zip(list_key,list_value))

    # 2eme ecriture possible
    new_dict: dict = {}
    if len(list_value) == len(list_key):
        for index, value in enumerate(list_key):
            new_dict[value] = list_value[index]
    else:
        print("les deux liste n'ont pas la même longueur.")


def fusion_dict():
    # Il faut fusionner deux dictionnaire en un
    dict_un: dict = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict_deux: dict = {'Fourty': 40, 'Fifty': 50}

    # 1ere ecriture possible
    # new_dict : dict = dict_un.copy()
    # new_dict.update(dict_deux)

    # 2eme ecriture : python 3.5+
    new_dict = {**dict_un, **dict_deux}


def display_key_values():
    # Vous devez afficher les clefs du dictionnaires ainsi que ses valeurs
    # Si une valeur vaux 0, il faut afficher "absence de données"
    dict_sample: dict = {'Ten': 0,
                         'Twenty': 20,
                         'Thirty': 60,
                         'Fourty': 15,
                         'Fifty': 50}
    value: str = ''
    for cle, valeur in dict_sample.items():
        if valeur == 0:
            value = 'absence de données'
        else:
            value = valeur
        print("la clef ", cle, ", possede la valeur : ", str(value))


def display_key(key: str):
    # l'utilisateur vous donne a donné une clef au préalable, vous devez afficher sa valeur
    dict_sample: dict = {'nom': 'toto',
                         'prenom': 'tarte',
                         'age': 20}

    # 1ere ecriture
    # if key in dict_sample.keys():
    #    print("la valeur de la clef", key, "est ", dict_sample.get(key))

    # 2eme ecriture
    try:
        print("la valeur de la clef ", key, "vaux : ", str(dict_sample[key]))
    except KeyError:
        print("la clef n'existe pas")
    except Exception:
        print("erreur inconnue")


def rename_key_dict(new_key: str, old_key: str):
    # Vous devez remplacer le nom de la clef od_key à new_key
    sample_dict: dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

    if old_key in sample_dict.keys():
        sample_dict[new_key] = sample_dict.pop(old_key)  # si old_key = name , alors cela me renvoie "Kelly"


def division(numerator: int, denumerator: int):
    # Réaliser une division avec une gestion d'erreur
    try:
        print("le resultat est : ", str(numerator / denumerator))
    except ZeroDivisionError:
        print("division par 0 impossible")


def moyenne_note():
    # demandez à l'utilisateur des notes, si la notes est inférieur à 0 ou superieur à 20
    # indiquez lui que la note n'est pas correcte.
    # tant que l'utilisateur ne met pas -1, nous continuons à lui demander des notes
    # Vous devez mettre en place une gestion d'erreur afin d'éviter que l'utiliasteur saisi des str

    choix_saisie: float = 0
    liste_note: list = []
    note: float = 0

    while choix_saisie != -1:
        is_float: bool = False
        while not is_float:
            try:
                note = float(input("Saissez votre note : "))
                is_float = True
            except ValueError:
                print("Vous n'avez pas entré un type valide. Veuillez réessayer")
        if note == -1:
            choix_saisie = -1
        else:
            if 0 <= note <= 20:
                liste_note.append(note)
            else:
                print("la note n'est pas correcte")
    if len(liste_note) >= 1:
        somme: float = 0
        for i in liste_note:
            somme += i
        result: float = somme / len(liste_note)
        print(str(result))
    else:
        print("Aucune note de présente")


def major_minor():
    # demandez l'age à l'utilisateur, si il est en dessous de 0
    # levez une exception ValueError. Si son age est correcte, calculez sa moyenne
    print('TODO')


if __name__ == "__main__":
    moyenne_note()
