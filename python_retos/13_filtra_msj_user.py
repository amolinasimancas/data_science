def filter_user_messages(messages, user):
    filtered = []
    for message in messages:
        if message['sender'] == user:
            filtered.append(message)
    return filtered

messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

user = 'Alice'
print(filter_user_messages(messages, user))

'''
[
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]
'''