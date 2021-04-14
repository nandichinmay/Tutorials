import json

def read_db():
    with open("flash_db.json") as f:
        return json.load(f) 

def save_db():
    with open("flash_db.json","w") as f:
        return json.dump(db,f)

db=read_db()