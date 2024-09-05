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

print(a.get("Adress","Pokhara"))
print(len(a))

test = {
     "name":"Broadway",
     "company": "Technology",
     "Number" : {
         "type":"NTC", 
         "mobile":"9841436920"
         }
}
print(test.keys())


test = {
     "name":"Broadway",
     "company": "Technology",
     "Number" : [
        {
          "type":"NTC", 
         "mobile":"9841436920"
         },
         {
          "type":"Ncell",
          "mobile":"98054"
         },
     ]
}


print(test.keys())

test.update({"name":"ganesh"})
print(test)

# del test["Number"]
# print(test)

# tt= test.pop("Number")
# print(test)
# print(tt)

# test.pop("Number")
# print(test)
# print(tt)

test.popitem()
print(test)

test.clear()
print(test)

