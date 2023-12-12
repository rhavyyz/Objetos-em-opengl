import json
import os

def get_stored_values(file = "data"):
    with open(os.path.join("storage", file + ".json")) as f:
        data = json.load(f)
        return (data["verticies"], data["edges"])

def set_stored_values(verticies, edges, filename = "data"):
    data = {"verticies" : verticies, "edges" :edges}
    with open(os.path.join("storage",filename + ".json"), "w+") as f:
        json.dump(data, f)

def get_n_on_storage():
    return len(os.listdir("storage"))