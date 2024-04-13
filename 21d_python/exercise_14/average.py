def get_student_average(students):
    names = []
    averages = []
    student_list = []
    new_dict = {}

    for student in students:
        names.append(student["name"])
        averages.append(sum(student["grades"])/len(student["grades"]))
    
    global_average = sum(averages)/len(averages)
    
    for i in range(len(names)):
        student = {
            "name": names[i],
            "average": averages[i]
        }
        student_list.append(student)
    
    new_dict["class_average"] = round(global_average,2)
    new_dict["students"] = student_list
    
    return new_dict

students = [
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
]

print(get_student_average(students))