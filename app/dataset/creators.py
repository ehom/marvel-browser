import json

def load():
    with open("app/dataset/creators.json") as f:
      chars = json.load(f)
    return chars
