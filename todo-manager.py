import json
import os
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed
        }

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**task) for task in data]

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()
        print("Naloga dodana.")

    def list_tasks(self):
        if not self.tasks:
            print("Ni nalog.")
            return

        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task.completed else "✗"
            print(f"{i}. [{status}] {task.title} (rok: {task.due_date})")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
            print("Naloga označena kot končana.")
        else:
            print("Neveljaven indeks.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Izbrisana naloga: {removed.title}")
        else:
            print("Neveljaven indeks.")

def main():
    manager = TaskManager()

    while True:
        print("\n--- TO-DO MANAGER ---")
        print("1. Dodaj nalogo")
        print("2. Prikaži naloge")
        print("3. Označi nalogo kot končano")
        print("4. Izbriši nalogo")
        print("5. Izhod")

        choice = input("Izberi možnost: ")

        if choice == "1":
            title = input("Naslov: ")
            description = input("Opis: ")
            due_date = input("Rok (YYYY-MM-DD): ")
            manager.add_task(title, description, due_date)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            manager.list_tasks()
            index = int(input("Številka naloge: ")) - 1
            manager.complete_task(index)

        elif choice == "4":
            manager.list_tasks()
            index = int(input("Številka naloge: ")) - 1
            manager.delete_task(index)

        elif choice == "5":
            print("Izhod...")
            break

        else:
            print("Neveljavna izbira.")

if __name__ == "__main__":
    main()