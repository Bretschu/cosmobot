import json


def get_tok():
    f = open('Token/token.json')

    data = json.load(f)

    f.close()

    return data['token']