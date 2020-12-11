import requests

from bokeh.io import output_file
from bokeh.plotting import figure


COOKIES = {
    'session': '53616c7465645f5f8cef573c0514deb6dca4514b5d31f60b32e6a839518be36383fc3cfb18bfde2307193dce79d28f06'
}

LEADERBOARDS = {
    'Meter': '1037780',
    'PythonDev.slack': '52704'
}


def get_leaderboard(id: int):
    resp = requests.get(f'https://adventofcode.com/2020/leaderboard/private/view/{id}.json',
                        cookies=COOKIES)
    members = resp.json()['members']
    return members


def
