print({})
print(type({}))
d = dict()
print(d)
from pprint import pprint
yoruba_to_english = {
    "ewe":"book",
    "okurin":"man",
    "obirin":"woman",
    "mama":"mom"
}
person = {
    "first_name":"rukayya",
    "last_name":"abdulkadir",
    "age":40,
    "ismarried":True,
    "country":"nigeria",
    "kids":('firdaus','abdulganee','fateemah','nafeesah'),
    "skills":['html','css','tailwind'],
    "hobbies":['reading','coding'],
    "adress": {

        "city":"ilorin",
        "state":"kwara",
        "street":"alubarka street",
    }
    
}
pprint(person)
print(person["age"])
print(person["ismarried"])
person['nationality'] = "canada"
pprint(person)
print(person.get('nationality'))
person['schools'] = ['bayero','crown']
person['schools'].append('webfella')
pprint(person)
print(person.get('schools'))
if 'hobbies' in person:
    print(person["hobbies"])
print(len(person))
print(yoruba_to_english.values())
print(yoruba_to_english.items())
for item in yoruba_to_english.items():
    print(item, item[0],item[1])
for key in person:
    print(key,person[key])