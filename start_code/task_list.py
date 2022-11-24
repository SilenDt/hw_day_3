tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#1. Print a list of uncompleted tasks

def get_incompleted_tasks():
    for task in tasks:
        if task["completed"] == False:
            print(task)

print(get_incompleted_tasks())

#2. Print a list of completed tasks

def get_completed_tasks():
    for task in tasks:
        if task["completed"] == True:
            print(task)

print(get_completed_tasks())

#3. Print a list of all task descriptions

def task_descriptions():
    for task in tasks:
        print(task["description"])

print_descriptions = task_descriptions()
print(print_descriptions)

#4. Print a list of tasks where time_taken is at least a given time
#time taken >= given time

#I dont understand what this question is asking

#5. Print any task with a given description
#input description, return task

def find_task(description):
    for task in tasks:
        if task["description"] == description:
            print(task)

print(find_task("Feed Cat"))




