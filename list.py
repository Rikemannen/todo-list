import argparse
import json
import os
from rapidfuzz import process, fuzz

# check if the file we save to exists
def check_file():
    if not os.path.exists("todo_list.json"):
        with open("todo_list.json", "w") as file:
            json.dump([], file)

# define the command line arguments
# (using argparse)
parser = argparse.ArgumentParser(
    prog="ToDo List",
    description="A simple cli todo list application",
)

parser.add_argument(
    "-a",
    "--add",
    type=str,
    help="Add a new task to the todo list",
)

parser.add_argument(
    "-r",
    "--remove",
    type=str,
    help="Remove a task from the todo list",
)

parser.add_argument(
    "-l",
    "--list",
    action="store_true",
    help="List all tasks in the todo list",
)

parser.add_argument(
    "-c",
    "--clear",
    action="store_true",
    help="Clear all tasks in the todo list",
)

# helper functions
def add_task(task):
    with open("todo_list.json", "r") as file:
        todo_list = json.load(file)
    base_task = task
    suffix = 1
    while task in todo_list:
        task = f"{base_task} ({suffix})"
        suffix += 1
    todo_list.append(task)
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)

def remove_task(task):
    with open("todo_list.json", "r") as file:
        todo_list = json.load(file)
    try:
        todo_list.pop(int(task))
    except (ValueError, IndexError):
        match = process.extractOne(task, todo_list, scorer=fuzz.partial_ratio, score_cutoff=50)
        if match:
            todo_list.remove(match[0])
        else:
            print(f"Task \"{task}\" not found.")
            return
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)

def list_tasks():
    with open("todo_list.json", "r") as file:
        todo_list = json.load(file)
    return todo_list

def clear_tasks():
    with open("todo_list.json", "w") as file:
        json.dump([], file)
    print("All tasks cleared.")

# main function
def main():
    check_file()
    args = parser.parse_args()

    if args.add:
        print(f"Adding task: {args.add}")
        add_task(args.add)
    elif args.remove is not None:
        print(f"Removing task: {args.remove}")
        remove_task(args.remove+1 if args.remove.isdigit() else args.remove)
    elif args.list:
        print("Listing all tasks")
        tasks = list_tasks()
        for i, task in enumerate(tasks):
            print(f"{i+1}: {task}")
    elif args.clear:
        print("Clearing all tasks")
        clear_tasks()
    else:
        parser.print_help()

# run
if __name__ == "__main__":
    main()