import json

people_string='''
{
    "people":[
        {
            "name":"John Doe",
            "phone":"615-555-7164",
            "emails":["johndoe69@bogusemail.com" , "john.doe@work_place_email.com"],
            "has_license":false
        },
        {
            "name":"Jane Doe",
            "phone":"564-453-2174",
            "emails":null,
            "has_license":true
        }
    ]
}
'''
data=json.loads(people_string)
print(type(data))
print(data)

for person in data["people"]:
    print(person["name"])

for person in data["people"]:
    del person["phone"]   

new_people_string=json.dumps(data,indent=2) 
print(new_people_string)
