import json
a = {"name":"sayjal","age":20,"place":"sikkim"}
file = open("meraki2ans", "w")
json.dump(a, file, indent = 5)
file.close()

