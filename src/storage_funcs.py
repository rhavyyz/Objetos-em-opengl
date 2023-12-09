import json

def get_stored_values():
    with open("storage/data.json") as f:
        data = json.load(f)
        return (data["verticies"], data["edges"])

def set_stored_values(verticies, edges):
    data = {"verticies" : verticies, "edges" :edges}
    with open("storage/data.json", "w+") as f:
        json.dump(data, f)