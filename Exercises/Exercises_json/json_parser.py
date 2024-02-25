import json

course = '{"name": "José", "languages": ["Java", "Python"]}'

#Lectura de json retornar un diccionario:
dict_courses = json.loads(course)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

#Convertir elementos de una key del diccionario a una lista:
list_language = dict_courses['languages']
print(type(list_language))
print(list_language)
print(dict_courses['languages'][0])

print("\nLectura de un archivo json\n")
### Lectura de un archivo json ###
with open("test-reading.json") as file:
    data = json.load(file)
    print(data)
    print(type(data))
    print(data["courses"])
    print(data["courses"][1])
    print(data["courses"][1]['title'])

    print(data["dashboard"]['website'])

    for course in data['courses']:
        print(course)
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] == 45


with open("test-reading.json") as file:
    data1 = json.load(file)

with open("test-reading-2.json") as file:
    data2 = json.load(file)

assert data1 == data2
