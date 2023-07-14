import json

def load():
    with open("app/dataset/chars.json") as f:
        chars = json.load(f)
    return chars
