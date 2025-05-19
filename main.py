# Small simple ToDo App

class Task:
    id = 0
    def __init__(self, task):
        self.task = task
    def __str__(self):
        return f"{self.id}\n{self.task}"
        
def printMenu():
    print("""1. Load Tasks
2. Add Task
3. Finish Task
4. Save Tasks to file""")

def loadTasks():
    pass

def addTask():
    pass

def finTask():
    pass

def saveTask():
    pass

def main():
    tasks = {}
    print("Hello to my little ToDo App")
    while True:
        printMenu()
        choice = input("Enter a Menu choice (1-4)")
        try:
            choice = int(choice)
        except ValueError as e:
            print(f"error, Input not a Number:{e}")
            continue
        print(choice)
        match choice:
            case 1:
                loadTasks()
                continue
            case 2:
                addTask()
                continue
            case 3:
                finTask()
                continue
            case 4:
                saveTask()
                continue
            case 5:
                break        
    

if __name__ == "__main__":
    main()
