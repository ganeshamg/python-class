# {} and (key and value)==> pair == dict
a = {"name":"ganesh",
     "surname":"amgain",
     "age":40,
     "address":["gorkha", "kathmandu"]
}
print(a["name"])
print(a["age"])


# get all key from dict
print(a.keys())
print(len(a))
print(a.get("middle_name", "-"))

# add key and value in dict
a["broadway"]="python"
print(a)
