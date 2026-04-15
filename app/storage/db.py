import json
import os

DB_FILE = "positions.json"

def save_position(position):
    data = position.to_dict()

    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            positions = json.load(f)
    else:
        positions = []

    positions.append(data)

    with open(DB_FILE, "w") as f:
        json.dump(positions, f, indent=2)


def load_positions():
    if not os.path.exists(DB_FILE):
        return []

    with open(DB_FILE, "r") as f:
        data = json.load(f)

    return data