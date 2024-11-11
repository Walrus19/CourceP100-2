# TODO решите задачу
import json
FILENAME = "input.json"
def task() -> float:
    with open(FILENAME, encoding="utf-8") as f:
        json_data = json.load(f)
    sum = 0
    for i in json_data:
        sum =sum + i["score"]*i["weight"]
    return round(sum, 3)
print(task())
