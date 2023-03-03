from superUser import user_collection
from datetime import date, timedelta, datetime


#, , 'parola': 0, , 'departament': 0
init_data = datetime.today().date()

# data = [j for i in user_collection.find({}, {'_id': 0, 'user': 1, 'data': 1}) for j in i.values()]
data = [i for i in user_collection.find({}, {'_id': 0, 'user': 1, 'data': 1})]

# print(init_data)
# print(type(init_data))
# print(data)

for i in data:
    if init_data - datetime.strptime(i.get('data'), "%Y-%m-%d").date() == timedelta(days = 1):
        print(f"Parola pentru userul --{i.get('user')}-- urmeaza sa expire.")

print("\nVa rugam accesati meniul 'Modificare' -> 'Editare parola' pentru a o schimba.")



# if init_data - timedelta(days = 35) == data[1]:
#     print(data[1])
# else:
#     print(data[2])
