from superUser import superUser, sleep
from datetime import date


class user(superUser):

    def __init__(self, user, parola, data, departament):
        """Construtorul clasei User"""
        self.user = user
        self.parola = parola
        self.data = data
        self.departament = departament
        # for i in kwargs:
        #     setattr(self, i, kwargs[i])

    @classmethod
    def adaugare_user(cls):
        categorie = superUser.alegere_user()
        input_user = input("Introduceti id user: ")
        parola = superUser.generare_parola()
        data = str(date.today())
        departament = input("Introduceti departamentul: ").upper()
        db_item = {"user": input_user, "parola": parola, "data": data, "departament": departament}
        categorie.insert_one(db_item)

    @classmethod
    def vizualizare_user(cls):
        categorie = superUser.alegere_user()
        data = categorie.find({}, {'_id': 0})
        for i in data:
            print(45 * "=")
            for attr, value in i.items():
                print(f"{attr}: {value}")
            print(45 * "=")
        input("\nApasati orice tasta pentru a continua...")

    @classmethod
    def editare_parola(cls):
        """Functia de editare a parolei user ului"""

        categorie = superUser.alegere_user()
        try:
            user_edit = input("Modificare user: ")
            parola_edit = superUser.generare_parola()
            categorie.update_one({"user": user_edit}, {"$set": {"data": str(date.today()), "parola": parola_edit}})
            print(f"Parola pentru user-ul {user_edit} a fost modificata.")
            sleep(5)
        except BaseException:
            print("Parola nu a putut fi modificata!")
            sleep(5)

    @classmethod
    def editare_departament(cls):
        """Functia de editare a departamentului din care face user ul"""

        categorie = superUser.alegere_user()
        try:
            user_edit = input("Modificare user: ")
            departament_edit = input("Departament nou: ").upper()
            categorie.update_one({"user": user_edit}, {"$set": {"departament": departament_edit}})
            print(f"Departamentul pentru user-ul {user_edit} a fost modificat.")
            sleep(5)
        except BaseException:
            print("Departamentul nu a putut fi modificat!")
            sleep(5)

    @classmethod
    def stergere_user(cls):
        """Functia de stergere a user ului"""

        categorie = superUser.alegere_user()
        try:
            user_del = categorie.delete_one({"user": input("Introduceti id user pentru stergere: ")})
            assert user_del.deleted_count
            print("Userul a fost sters.")
            sleep(5)
        except AssertionError:
            print("Userul nu a putut fi sters!")
            sleep(5)
