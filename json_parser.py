import requests
import io_util
import json


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        raise RuntimeError("{} has {} code".format(url, response.status_code))


def submit_headers(response):
    dict_for_json = {}
    for key, value in response.headers.items():
        dict_for_json[key] = value
        print('"{}": {}'.format(key, value))
    io_util.writef('output.txt', json.dumps(dict_for_json, indent=2))


def submit_json(response):
    dict_for_json = response.json()
    io_util.writef('json_data.txt', json.dumps(dict_for_json, indent=2))


def print_free_space():
    print('\n\n\n')


def parse_json_data(response):
    dict_for_json = response.json()
    for item in dict_for_json:
        for key, value in item.items():
            print("{}: = {}".format(key, value))
        print()