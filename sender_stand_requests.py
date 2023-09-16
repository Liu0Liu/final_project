import requests
import data
import configuration


def post_new_order(body):
    return requests.post(
        url=configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers,
    )


def get_order_response(track: int):
    _params = {'t': track}

    return requests.get(
        url=configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
        params=_params,
        headers=data.headers,
    )
