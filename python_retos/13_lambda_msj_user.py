def filter_user_messages(messages, user):
    filtered = list(filter(lambda message: message['sender'] == user, messages))
    return filtered

messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

user = 'Alice'