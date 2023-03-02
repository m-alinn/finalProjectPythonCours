from pymongo import MongoClient
import random
from time import sleep

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

    # TODO: adaugare verificare a caracterelor introduse
    @classmethod
    def generare_parola(cls):
        """Accepta un string mai mare de 5 caractere cu ajutorul caruia genereaza random parola"""

        input_parola = input(
            """Parola trebuie sa contina litere mari, litere mici, numere si caractere speciale
            \nIntroduceti sirul de caractere (minim 6 caractere):   """
        )
        if len(input_parola) > 5:
            print("Parola generata cu succes\n")
            return "".join(random.sample(input_parola, len(input_parola)))

        else:
            print("Numarul de caractere introdus este insuficient.\n")
            return superUser.generare_parola()

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

    # TODO: create a function that notifies the user that passwords are about to expire
    @classmethod
    def expirare_parola(cls):
        pass
