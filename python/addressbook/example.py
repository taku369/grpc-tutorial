from google.protobuf import json_format
import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.PHONE_TYPE_HOME

try:
    # raises AttributeError
    person.no_such_field = 1
except Exception as e:
    print(e)

try:
    # raises TypeError
    person.id = "1234"
except Exception as e:
    print(e)

# Serialize to JSON
json_string = json_format.MessageToJson(person)
print(json_string)

# Parse from JSON
new_person = addressbook_pb2.Person()
json_format.Parse(json_string, new_person)
