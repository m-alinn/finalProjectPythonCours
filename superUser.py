from pymongo import MongoClient
import random
import re
from datetime import datetime, timedelta


# Initializare baza de date
client = MongoClient("mongodb://localhost:27017")
mydb = client["pythonFinalProject"]
# Initializare colectii de date
user_collection = mydb["user"]
superUser_collection = mydb["superUser"]


class superUser:

    @classmethod
    def alegere_user(cls):
        """Perminte alegerea categoriei de useri pentru care se efectueaza operatia"""

        while True:
            print(45 * "=")
            match input("Alegeti una dintre categorii:"
                        "\n1. Super User"
                        "\n2. User"
                        "\n\nOptiune: "):
                case '1':
                    return superUser_collection
                case '2':
                    return user_collection
                case  _:
                    return superUser.alegere_user()

    @classmethod
    def generare_parola(cls):
        """Accepta un string mai mare de 5 caractere cu ajutorul caruia genereaza random parola"""

        input_parola = input(
            "Introduceti un sir de caractere (minim 6 caractere):   "
        )
        if len(input_parola) < 6:
            print("Parola trebuie sa aiba cel putin 6 caractere.")
            return superUser.generare_parola()
        elif re.search("[0-9]", input_parola) is None:
            print("Parola trebuie sa contina cifre.")
            return superUser.generare_parola()
        elif re.search("[A-Z]", input_parola) is None:
            print("Parola trebuie sa contina litere mari.")
            return superUser.generare_parola()
        elif re.search("[a-zA-Z0-9 ]* ", input_parola) is None:
            print("Parola trebuie sa contina caractere speciale.")
            return superUser.generare_parola()
        else:
            print("Parola generata cu succes\n")
            return "".join(random.sample(input_parola, len(input_parola)))

    # TODO: beautify the output of the function
    @classmethod
    def vizualizare_all(cls):
        """Culege obiectele din toate colectile"""

        print("=============================================")
        for i in superUser_collection.find({}, {"_id": 0}):
            for attr, value in i.items():
                print(f"{attr}: {value}")
            print(f"=============================================")
        for i in user_collection.find({}, {"_id": 0}):
            for attr, value in i.items():
                print(f"{attr}: {value}")
            print(f"=============================================")
        input("Apasati orice tasta pentru a continua ...")

    # TODO: try to make the message persistent for more days (before or after the timedelta of 30 days)
    @classmethod
    def expirare_parola(cls):
        init_data = datetime.today().date()
        # data = [j for i in user_collection.find({}, {'_id': 0, 'user': 1, 'data': 1}) for j in i.values()]
        data = [i for i in user_collection.find({}, {'_id': 0, 'user': 1, 'data': 1})]
        for i in data:
            if init_data - datetime.strptime(i.get('data'), "%Y-%m-%d").date() == timedelta(days=30):
                print(f"Parola pentru userul --{i.get('user')}-- urmeaza sa expire.")

        print("\n", 92 * "*", "\n\tVa rugam accesati meniul 'Modificare' -> 'Editare parola' pentru a o schimba.\n", 92 * "*", "\n")
        input("\nApasati orice tasta pentru a continua ...")