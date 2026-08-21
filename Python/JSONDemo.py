import json
#---JSON String ---> Python object
json_str = '{"name" : "Ajoy", "isStudent" : true, "isGF" : null}'

py_obj = json.loads(json_str)
print(type(py_obj), py_obj)

#---Python object ---> JSON String
py_obj = {"name" : "Ajoy",
          "isStudent" : True,
          "isGF" : None
        }

json_str = json.dumps(py_obj)
print(type(json_str), json_str)

with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(type(py_obj), py_obj)

# data = {
#     "name" : "Ajoy",
#     "age" : 23,
#     "isStudent" : True
# }
# with open("data.json", "r") as f:
#     json.dump(data, f)
#     json.dump(data, f, indent=4)
#     json.dump(data, f, indent=4, sort_keys=True)
