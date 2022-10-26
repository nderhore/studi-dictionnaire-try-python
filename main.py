def list_to_dict():
    #Nous avons deux listes, il suffit de les convertir en dictionnaire Python
    list_key : list = ['clef_un', 'clef_deux', 'clef_trois']
    list_value : list = ['value_un', 'valeu_deux', 'value_trois']

def fusion_dict():
    #Il faut fusionner deux dictionnaire en un
    dict_un : dict = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict_deux : dict = {'Fourty': 40, 'Fifty': 50}

def display_key_values():
    #Vous devez afficher les clefs du dictionnaires ainsi que ses valeurs
    # Si une valeur vaux 0, il faut afficher "absence de données"
    dict_sample : dict = {'Ten': 0,
                          'Twenty': 20,
                          'Thirty': 60,
                          'Fourty': 15,
                          'Fifty': 50}

def display_key(key : str):
    #l'utilisateur vous donne a donné une clef au préalable, vous devez afficher sa valeur
    dict_sample : dict = {'nom' : 'toto',
                          'prenom': 'tarte',
                          'age': 20}

def rename_key_dict(new_key : str, old_key : str):
    #Vous devez remplacer le nom de la clef od_key à new_key
    sample_dict : dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

def division(numerator : int, denumerator : int):
    #Réaliser une division avec une gestion d'erreur

def moyenne_note():
    #demandez à l'utilisateur des notes, si la notes est inférieur à 0 ou superieur à 20
    #indiquez lui que la note n'est pas correcte.
    #Vous devez mettre en place une gestion d'erreur afin d'éviter que l'utiliasteur saisi des str

def major_minor():
    #demandez l'age à l'utilisateur, si il est en dessous de 0
    #levez une exception ValueError. Si son age est correcte, calculez sa moyenne

