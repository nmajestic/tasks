from task import Task

def mainloop():

    continue_tasks = True
    tasks = []

    while continue_tasks:

        print("Option [a] to add a task")
        print("Option [d] to delete a task")
        print("Option [l] to list tasks")
        print("Option [q] to quit")
        option_selected = input("Select an option: ")

        match option_selected:
            case "a":
                task_name = input("Type the name of the task: ")
                task_description = input("Type the description of the task: ")
                task = Task(task_name, task_description)
                tasks.append(task)
            case "d":
                task_name = input("Type the name of the task to delete: ")
                for task in tasks:
                    if task.name == task_name:
                        tasks.remove(task)
                pass
            case "l":
                for task in tasks:
                    print(f"Task: {task.name} --------- Description: {task.description}")
            case "q":
                exit()

def greeting():
    print("Welcome to Tasks!")
    print("Version: 0.0.1")

def main():
    greeting()
    greeting_prompt = input("Type 'continue' to start or 'exit' to exit: ")
    if greeting_prompt == "continue":
        mainloop()
    if greeting_prompt == "exit":
        exit()

if __name__ == "__main__":
    main()