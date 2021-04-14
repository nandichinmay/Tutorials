import json

def read_db():
    with open("flash_db.json") as f:
        return json.load(f) 


db=read_db()