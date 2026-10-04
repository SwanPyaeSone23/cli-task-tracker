import sys
import json
import os
from datetime import datetime

FILE_PATH = "tasks.json"

def load_tasks():
    # Check if tasks.json exists on your computer
    if not os.path.exists(FILE_PATH):
        return []
    # Try opening and reading the JSON file
    try:
        with open(FILE_PATH,"r") as file:
            return json.load(file)
    except json.JSONDecodeError:
     # Returns empty list if file is empty 
        return []
    
def save_tasks(tasks):
    # Open tasks.json in write mode and save the Python list
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)
        

def add_tasks(description):
    tasks = load_tasks()
    
    if len(tasks) == 0:
        id = 1
    else:
        id = max(task["id"] for task in tasks) + 1
        
    
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    new_tasks = {
        "id": id,
        "description": description,
        "status": "in-progress",
        "created_At": time,
        "updated_At": time
    }
    
    tasks.append(new_tasks)
    # Save in Json file
    save_tasks(tasks)
    
    print(f"Task added completed with ID {id}")

def delete_task(id):
    tasks = load_tasks()
    
    update_tasks = [task for task in tasks if task["id"] != id]
    if len(tasks) == len(update_tasks):
        print(f"Error not found given ID {id}")
    else:
        for index, task in enumerate(update_tasks, start=1):
            task["id"] = index
        save_tasks(update_tasks)
        print(f"Successfully delete ID {id}")
        
def delete_all_tasks():
    save_tasks([])
    print("Successfully deleted all tasks")
    
def update(id, update_description):
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == id:
            task["description"] = update_description
            task["updated_At"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            save_tasks(tasks)
            print(f"Successfully updated id {id}")
            return
    print("Error not found given ID")
    
def update_status(id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            if task["status"] == "done":
                print(f"{id} is already done")
                return
            
            task["status"] = "done"
            task["updated_At"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            save_tasks(tasks)
            print(f"Successfully update status id {id}")
            return
    print("Error not found given ID")
    
def show_all_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found")
        return
    print(f"\n{'ID':<4} | Description | {'Status':<12} | {'Created At':<19} | {'Updated At':<19}")
    print("-" * 88)
    
    for task in tasks:
        
        # Clean up ISO timestamps for readable printing
        raw_created = task.get("created_At", "")
        formatted_created = raw_created.split(".")[0].replace("T", " ") if raw_created else "N/A"

        raw_updated = task.get("updated_At", "")
        formatted_updated = raw_updated.split(".")[0].replace("T", " ") if raw_updated else "N/A"

        print(f"{task['id']:<4} | {task['description']} | {task['status']:<12} | {formatted_created:<19} | {formatted_updated:<19}")
    print()
            
#sys.argv contains all command line input as a list
arguments = sys.argv[1:] #ignore the script name itself


if not arguments:
    print("Welcome Task Tracker (python)")
    print("Exmaple : python task_tracker.py add ______")
else:
    command = arguments[0]
    
    if command == "add":
        if len(arguments) > 1:
            task = arguments[1]
            add_tasks(task)
        else:
            print("Error : please provide task description")
            
    elif command == "list":
        print("Listing all task")
        
    elif command == "delete":
        if len(arguments) > 1 :
            try:
                id = int(arguments[1])
                delete_task(id)
            except ValueError:
                print("Error : Please provide ID")
        else:
            print("Error : Please provide correct ID to delete")
            
    elif command == "clear" or command == "delete-all-tasks":
        confirmation = input("Are you sure you want to delete all tasks? (y/n) : ")
        if confirmation.lower() == "y":
            delete_all_tasks()
        else:
            print("Cancelled deleting all tasks")
    
    elif command == "update":
        if len(arguments) > 2:
            try:
                id = int(arguments[1])
                update_description = arguments[2]
                update(id, update_description)
            except ValueError:
                print("Error : Please provide corrcet ID")
        else:
            print("Error : Please provide correct ID to update")
    elif command == "done":
        if len(arguments) > 1:
            try:
                id = int(arguments[1])
                update_status(id)
            except ValueError:
                print("Error : Please provide correct ID to update status")
        else:
            print("Error : Please provide correct ID to update status")
    elif command == "show-all-tasks":
        show_all_tasks()
    else:
        print("Something wrong Unknown", command)