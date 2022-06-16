import json
from datetime import datetime


def update_json():
    json_file = open("data.json", "r")
    json_object = json.load(json_file)
    json_file.close()

    json_object["id"] += 1
    json_object["updated_at"] = str(datetime.now())

    a_file = open("data.json", "w")
    json.dump(json_object, a_file)
    a_file.close()










def update_text():
    json_file = open("text.json", "r")
    json_object = json.load(json_file)
    json_file.close()

    json_object["id"] += 1
    json_object["updated_at"] = str(datetime.now())

    a_file = open("text.json", "w")
    json.dump(json_object, a_file)
    a_file.close()






if __name__ == "__main__":
    print("hi")
    update_json()
    update_text()
