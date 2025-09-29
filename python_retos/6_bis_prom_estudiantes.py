def get_student_average(students):
  # Tu código aquí 👈
  answer = {
    "class_average": 0,
    "students": []
  }

  counter = 0

  for student in students:
    entry = {}
    entry["name"] = student["name"]
    entry["average"] = round(sum(student["grades"])/len(student["grades"]),2)
    answer["students"].append(entry)
    counter += entry["average"]
  
  class_average = round(counter/len(students),2)
  answer["class_average"] = class_average

  return answer

print(get_student_average([
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
]))