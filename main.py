from superUser import *
from user import user
from sys import exit
from os import system


# Curatare consola
def clear():
    system('cls')


def meniu_optiune_user(dictionar):
    optiune = input("Introduceti optiune: ")
    # Apelarea optiunii corespunzatoare input-ului
    if optiune in dictionar:
        dictionar[optiune]()
    else:
        print("Nu ati introdus o optiune valida.")
        sleep(7)


def submeniu_vizualizare_user():
    """Submeniu vizulalizare
    1. Vizualizare toti userii
    2. Vizualizare useri pe categorie
    3. Iesire la meniul anterior
    """

    dict_vizualizare = {
        "1": superUser.vizualizare_all,
        "2": user.vizualizare_user,
        "3": main_user
    }

    while True:
        clear()
        print(60 * "=")
        print("1. Meniu Vizualizare".center(60))
        print(60 * "=")
        print("1. Vizualizare toti userii\n2. Vizualizare useri pe categorie\n3. Intoarcere la meniul principal")
        print(60 * "=")

        meniu_optiune_user(dict_vizualizare)


def submeniu_vizualizare_superuser():
    """Submeniu vizulalizare
    1. Vizualizare toti userii
    2. Vizualizare useri pe categorie
    3. Iesire la meniul anterior
    """

    dict_vizualizare = {
        "1": superUser.vizualizare_all,
        "2": user.vizualizare_user,
        "3": main_superuser
    }

    while True:
        clear()
        print(60 * "=")
        print("1. Meniu Vizualizare".center(60))
        print(60 * "=")
        print("1. Vizualizare toti useri\n2. Vizualizare useri pe categorie\n3. Intoarcere la meniul principal")
        print(60 * "=")

        meniu_optiune_user(dict_vizualizare)


def submeniu_modificare():
    """Submeniu modificare
    1. Modificare user
    2. Stergere user
    3. Intoarcere la meniul anterior
    """

    dict_modificare = {
        "1": user.editare_parola,
        "2": user.editare_departament,
        "3": user.stergere_user,
        "4": main_superuser
    }

    while True:
        clear()
        print(60 * "=")
        print("2. Meniul Editare ".center(60))
        print(60 * "=", "\n1. Editare parola\n2. Editare departament\n3. Stergere user"
                        "\n4. Iesire la meniul principal\n", 60 * "=")

        meniu_optiune_user(dict_modificare)


def main_superuser():

    """Functia de main a proiectului pentru super user."""
    while True:
        """Meniul principal super user"""
        dict_meniuprincipal = {
            "1": submeniu_vizualizare_superuser,
            "2": user.adaugare_user,
            "3": submeniu_modificare,
            "4": exit
        }

        while True:
            clear()
            superUser.expirare_parola()
            clear()
            print(35 * "=")
            print("Meniu Principal Super User".center(35))
            print(35 * "=", "\n1. Vizualizare\n2. Adaugare\n3. Modificare\n4. Iesire\n", 35 * "=")

            meniu_optiune_user(dict_meniuprincipal)


def main_user():
    print("Meniu principal user normal")
    """Functia de main a proiectului pentru user."""
    while True:
        """Meniul principal"""
        dict_meniu_principal = {
            "1": submeniu_vizualizare_user,
            "2": exit
        }

        while True:
            clear()
            print(35 * "=")
            print("Meniu Principal".center(35))
            print(35 * "=", "\n1. Vizualizare\n2. Iesire\n", 35 * "=")

            meniu_optiune_user(dict_meniu_principal)


if __name__ == "__main__":
    """Verificare/conectare user"""

    incercare = 0
    while incercare < 3:
        input_user = input("User: ")
        input_parola = input("Parola: ")

        """Meniu dublu in functie de ce categorie de user se logheaza"""
        # TODO: What if there are no users in the database?
        if input_user in [i['user'] for i in superUser_collection.find({}, {'_id': 0, 'user': 1})] and input_parola in \
                [j['parola'] for j in superUser_collection.find({}, {'_id': 0, 'parola': 1})]:

            main_superuser()

        elif input_user in [i['user'] for i in user_collection.find({}, {'_id': 0, 'user': 1})] and input_parola in \
                [j['parola'] for j in user_collection.find({}, {'_id': 0, 'parola': 1})]:

            main_user()

        else:
            if incercare < 2:
                incercare += 1
                print("User sau parola incorecte. Va rugam reincercati!\nIncercari ramase: ", 3-incercare)
            else:
                print("Ati introdus user sau parola gresit de trei ori.\nLa revedere!")
                break
