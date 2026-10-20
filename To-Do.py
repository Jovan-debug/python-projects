
import json
class Task:
    def __init__(self,title:str,Completed:bool = False):
        self.title=title
        self.Completed=Completed

    def mark_done (self):
        self.Completed=True

    def to_dict(self):
        return {"title":self.title,"Status":self.Completed}
    @classmethod
    def from_dict(cls ,data:dict):
        return cls(title=data["title"],Completed=data["Status"])

          
class Todo_list:
    def __init__(self,filename:str ="task.json"):
        self.filename=filename
        self.tasks: list[Task]=[]
        self.load_task()


    def view_list(self):
        if not self.tasks:
            print("No task found")

        for i,task in enumerate (self.tasks):
            status="[x]" if task.Completed else "[ ]"
            print(f"{i+1}.{status} {task.title} ")

    def add_task(self,title):
        self.tasks.append(Task(title=title))
        print("Task added")
        self.save_task()

    def mark_task_done(self,index:int):
        realindex=index-1

        if 0<=realindex<len(self.tasks):
            self.tasks[realindex].mark_done()
            self.save_task()
            print("task mark as done")
        else:print("invalid task number")


    def save_task(self):

        try:
            with open(self.filename,"w") as file:
                data=[task.to_dict() for task in self.tasks]
                json.dump(data,file,indent=4)
        except TypeError as e:
            print("error ")

    def load_task(self):
        try:
            with open(self.filename,"r") as file:
                content=json.load(file)
            self.tasks=[Task.from_dict(item) for item in content]
        except FileNotFoundError:
            print("file not found")
            self.tasks=[]


def main():
    todo=Todo_list()

    while True:
        print("\n1. View List")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("q. Quit")

        choice=input("Enter your choice:").strip().lower()

        if choice=="1":
            todo.view_list()
        elif choice=="2":
            title=input("Enter the task description:").strip()
            todo.add_task(title=title)
            
        elif choice=="3":
            todo.view_list()
            num=input("Enter the task number to mark as done")
            if num.isdigit():
                todo.mark_task_done(int(num))
            else:print("enter a valid number")

        elif choice=="q":
            print("Thanks Good Bye")
            break
        else:print("enter a valid choice")

if __name__=="__main__":
    main()