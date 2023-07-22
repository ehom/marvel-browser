import json

def load():
    with open("app/dataset/comics.json") as f:
        comics = json.load(f)
    return comics
