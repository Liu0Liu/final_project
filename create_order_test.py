import data
import sender_stand_requests

# Шадрина Любовь, 8-я когорта — Финальный проект. Инженер по тестированию плюс

def test_get_order_by_track_return_200():
    create_new_order_response = sender_stand_requests.post_new_order(body=data.order_body)
    track = create_new_order_response.json()["track"]

    get_existing_order_response = sender_stand_requests.get_order_response(track=track)
    assert get_existing_order_response.status_code == 200
