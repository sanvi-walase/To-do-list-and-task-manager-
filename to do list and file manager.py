# PROJECT: TO-DO LIST AND TASK MANAGER

# PART 1: CLASSES AND INHERITANCE

class Task:

    def __init__(self, task_id, title, description):
        self._task_id = task_id
        self.title = title
        self.description = description
        self.status = "Pending"

    def get_id(self):
        return self._task_id


class PriorityTask(Task):

    def __init__(self, task_id, title, description, priority):
        super().__init__(task_id, title, description)
        self.priority = priority

    def display(self):
        print("-" * 45)
        print("Task ID     :", self._task_id)
        print("Title       :", self.title)
        print("Description :", self.description)
        print("Priority    :", self.priority)
        print("Status      :", self.status)
        print("-" * 45)


# PART 2: TASK MANAGER CLASS

class TaskManager:

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def find_task(self, task_id):
        for task in self.tasks:
            if task.get_id() == task_id:
                return task
        return None

    def select_priority(self):

        print("\nSelect Task Priority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        while True:
            choice = input("Enter priority (1-3): ")

            if choice == "1":
                return "High"
            elif choice == "2":
                return "Medium"
            elif choice == "3":
                return "Low"
            else:
                print("Invalid choice! Try again.")


# PART 3: ADD AND VIEW TASKS

    def add_task(self):

        print("\n========== ADD NEW TASK ==========")

        title = input("Enter task title: ").strip()

        if not title:
            print("Task title cannot be empty!")
            return

        description = input("Enter task description: ").strip()
        priority = self.select_priority()

        task = PriorityTask(
            self.next_id,
            title,
            description,
            priority
        )

        self.tasks.append(task)
        self.next_id += 1

        print("\nTask added successfully!")

    def view_tasks(self):

        print("\n========== ALL TASKS ==========")

        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            task.display()


# PART 4: UPDATE AND COMPLETE TASKS

    def update_task(self):

        print("\n========== UPDATE TASK ==========")

        try:
            task_id = int(input("Enter Task ID: "))
        except ValueError:
            print("Please enter a valid Task ID.")
            return

        task = self.find_task(task_id)

        if task is None:
            print("Task not found!")
            return

        print("\nPress Enter to keep the existing value.")

        new_title = input("Enter new title: ").strip()

        if new_title:
            task.title = new_title

        new_description = input("Enter new description: ").strip()

        if new_description:
            task.description = new_description

        change_priority = input(
            "Change priority? (yes/no): "
        ).strip().lower()

        if change_priority == "yes":
            task.priority = self.select_priority()

        print("\nTask updated successfully!")

    def complete_task(self):

        print("\n========== COMPLETE TASK ==========")

        try:
            task_id = int(input("Enter Task ID: "))
        except ValueError:
            print("Please enter a valid Task ID.")
            return

        task = self.find_task(task_id)

        if task is None:
            print("Task not found!")
        else:
            task.status = "Completed"
            print("\nTask marked as completed!")


# PART 5: DELETE TASK

    def delete_task(self):

        print("\n========== DELETE TASK ==========")

        try:
            task_id = int(input("Enter Task ID: "))
        except ValueError:
            print("Please enter a valid Task ID.")
            return

        task = self.find_task(task_id)

        if task is None:
            print("Task not found!")
            return

        confirm = input(
            "Are you sure you want to delete this task? (yes/no): "
        ).strip().lower()

        if confirm == "yes":
            self.tasks.remove(task)
            print("\nTask deleted successfully!")
        else:
            print("\nDelete operation cancelled.")


# MAIN MENU

def main():

    manager = TaskManager()

    print("=" * 45)
    print("       TO-DO LIST AND TASK MANAGER")
    print("=" * 45)

    while True:

        print("\n============== MAIN MENU ==============")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            manager.add_task()

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.update_task()

        elif choice == "4":
            manager.complete_task()

        elif choice == "5":
            manager.delete_task()

        elif choice == "6":
            print("\nThank you for using To-Do List Manager!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter 1 to 6.")


# PROGRAM EXECUTION

if __name__ == "__main__":
    main()
