"""
Задание №1

Необходимо реализовать 2 ручки:
Ручка PUT на изменение отеля
Ручка PATCH на изменения отеля

Обе ручки позволяют видоизменить конкретный отель. Однако, в ручке PUT мы обязаны передать оба параметра title и name,
а в PATCH ручке можем передать либо только title, либо только name, либо оба параметра сразу
(тогда PATCH ничем не отличается от PUT ручки).
"""
from fastapi import FastAPI

fake_hotels = [
    {"id": 1, "title": "Russia", "name": "Золотая Гавань"},
    {"id": 2, "title": "Dubai", "name": "Social hotel"},
    {"id": 3, "title": "Turkey", "name": "Ramada"}
]
hotel_app = FastAPI()


@hotel_app.put("/hotels/{hotel_id}")
def change_hotel_put(hotel_id: int, title: str, name: str):
    for hotel in fake_hotels:
        if hotel.get("id", 'There is no key') == hotel_id:
            hotel["title"] = title
            hotel["name"] = name
            return {"status": 200, "data": hotel}
        else:
            return {"status": 404, "message": "hotel_id does not exist"}


@hotel_app.patch("/hotels/{hotel_id}")
def change_hotel_patch(hotel_id: int, title: str = None, name: str = None):
    for hotel in fake_hotels:
        if hotel.get("id", 'There is no key') == hotel_id:
            hotel["title"] = title
            hotel["name"] = name
            return {"status": 200, "data": hotel}
        else:
            return {"status": 404, "message": "hotel_id does not exist"}
