#JSON - JavaScript Object Notation
import json
data = '''{
    'name':'chuck',
    'phone':{
        'type':"int1",
        'number':"+1 699544758"
    },
    'email':{
        "hide":'yes'
    }
}
'''

info = json.loads(data)#This returns a dictionary
print('Name:',info['name'])
print('Hide:',info['email']['hide'])