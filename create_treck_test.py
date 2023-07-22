# Щепетьева Жанна, 6-ая когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_create_and_get_order():
    create_resp = sender_stand_request.create_order(data.TEST_ORDER_DATA) # статус создания заказа
    assert create_resp.status_code == 201
    track = create_resp.json()["track"] # Сохранение трека заказа
    get_resp = sender_stand_request.get_order(track) # Запрос на получение заказа
    assert get_resp.status_code == 200 # http статус получения заказа
