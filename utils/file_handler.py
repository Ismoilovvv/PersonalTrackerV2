import json
import os
from json import JSONDecodeError


def load_data(filepath):
    if not os.path.exists(filepath):
        return []

    with open(filepath, 'r') as file:
        try:
            return json.load(file)
        except JSONDecodeError:
            return []

def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)