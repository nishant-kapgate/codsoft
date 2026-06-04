import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json") 
PRIORITIES = {"1": " High", "2": " Medium", "3": " Low"}
STATUSES = {"pending": " Pending", "in-progress": " In-Progress", "done": " Done"}
def load_tasks(): 
    if os.path.exists(DATA_FILE):
        try: 
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []  
def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)
def clear_screen(): 
    os.system("cls" if os.name == "nt" else "clear") 
def print_header():
    clear_screen()
    print("\n")
    print("                TO-DO LIST                       ") 
    print()
def print_separator():
    print("  ──────────────────────────────────────────────────────") 
def print_menu():
    print("                     MAIN MENU                        ")
    print("    [1]    Add a New Task                           ")
    print("    [2]    View All Tasks                           ")
    print("    [3]    Update a Task                            ")
    print("    [4]    Change Task Status                       ")
    print("    [5]    Delete a Task                            ") 
    print("    [6]    Search Tasks                             ")
    print("    [7]    View Summary / Statistics                ")
    print("    [8]    Exit                                     ")
    print()
def get_priority_label(priority):
    return PRIORITIES.get(str(priority), " Low") 
def get_status_label(status):
    return STATUSES.get(status, "⏳ Pending")
def display_task(task, index):
    priority = get_priority_label(task.get("priority", "3"))
    status = get_status_label(task.get("status", "pending"))
    category = task.get("category", "General")
    created = task.get("created", "N/A")
    print(f"    Task #{index + 1} ")
    print(f"      Title    : {task['title']}")
    print(f"      Details  : {task.get('description', 'No description')}")
    print(f"       Category : {category}")
    print(f"      Priority : {priority}")
    print(f"      Status   : {status}")
    print(f"      Created  : {created}")
def add_task(tasks):
    print_header()
    print("    ADD A NEW TASK \n")
    title = input("  Enter task title: ").strip()
    if not title:
        print("\n   Task title cannot be empty!") 
        input("\n  Press Enter to continue...")
        return
    description = input("  Enter description (optional): ").strip()
    category = input("  Enter category (e.g., Work, Personal, Study) [General]: ").strip()
    if not category: 
        category = "General"
    print("\n  Set Priority:")
    print("    [1]  High")
    print("    [2]  Medium")
    print("    [3]  Low")
    priority = input("  Choose (1/2/3) [3]: ").strip()
    if priority not in ("1", "2", "3"):
        priority = "3"
    task = {
        "title": title,
        "description": description if description else "No description",
        "category": category,
        "priority": priority,
        "status": "pending",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    } 
    tasks.append(task)
    save_tasks(tasks)
    print(f"\n    Task '{title}' added successfully!") 
    input("\n  Press Enter to continue...")
 
def view_tasks(tasks):
    print_header()
    print("    ALL TASKS \n")

    if not tasks:
        print("    No tasks found. Start by adding a new task!\n")
        input("  Press Enter to continue...")
        return
    print("  Filter by: [A]ll  [P]ending  [I]n-Progress  [D]one  [H]igh Priority")
    filter_choice = input("  Choose filter [A]: ").strip().lower()
    filtered = tasks 
    if filter_choice == "p": 
        filtered = [t for t in tasks if t.get("status") == "pending"] 
    elif filter_choice == "i":
        filtered = [t for t in tasks if t.get("status") == "in-progress"]
    elif filter_choice == "d":
        filtered = [t for t in tasks if t.get("status") == "done"]
    elif filter_choice == "h": 
        filtered = [t for t in tasks if str(t.get("priority")) == "1"] 
    if not filtered:
        print("\n   No tasks match this filter.\n") 
    else:  
        print(f"\n  Showing {len(filtered)} task(s):\n")
        for i, task in enumerate(filtered):
            original_index = tasks.index(task) 
            display_task(task, original_index)
            print()
    input("  Press Enter to continue...") 

def update_task(tasks): 
    print_header()
    print("     UPDATE A TASK \n")
    if not tasks: 
        print("    No tasks to update.\n")
        input("  Press Enter to continue...")
        return 
    for i, task in enumerate(tasks):
        print(f"  [{i + 1}] {get_status_label(task.get('status','pending'))}  {task['title']}") 
    print()
    try:  
        choice = int(input("  Enter task number to update: ")) - 1 
        if choice < 0 or choice >= len(tasks):
            raise ValueError
    except ValueError: 
        print("\n   Invalid selection!")
        input("\n  Press Enter to continue...")
        return
    task = tasks[choice]
    print(f"\n  Current Title: {task['title']}")
    new_title = input("  New title (press Enter to keep current): ").strip()
    if new_title: 
        task["title"] = new_title
    print(f"  Current Description: {task.get('description', 'No description')}")
    new_desc = input("  New description (press Enter to keep current): ").strip()
    if new_desc:
        task["description"] = new_desc
    print(f"  Current Category: {task.get('category', 'General')}")
    new_cat = input("  New category (press Enter to keep current): ").strip() 
    if new_cat:
        task["category"] = new_cat

    print(f"  Current Priority: {get_priority_label(task.get('priority', '3'))}")  
    print("    [1]  High   [2]  Medium   [3]  Low") 
    new_pri = input("  New priority (press Enter to keep current): ").strip()  
    if new_pri in ("1", "2", "3"):
        task["priority"] = new_pri

    save_tasks(tasks) 
    print(f"\n    Task updated successfully!")
    input("\n  Press Enter to continue...") 

def change_status(tasks):
    print_header() 
    print("   CHANGE TASK STATUS \n")
    if not tasks:
        print("    No tasks available.\n")
        input("  Press Enter to continue...")
        return
    for i, task in enumerate(tasks):
        print(f"  [{i + 1}] {get_status_label(task.get('status','pending'))}  {task['title']}") 
    print()
    try: 
        choice = int(input("  Enter task number: ")) - 1
        if choice < 0 or choice >= len(tasks):
            raise ValueError
    except ValueError:
        print("\n    Invalid selection!")
        input("\n  Press Enter to continue...")
        return
    task = tasks[choice]
    print(f"\n  Current status: {get_status_label(task.get('status', 'pending'))}")
    print("\n  Set new status:")
    print("    [1]  Pending")
    print("    [2]  In-Progress")
    print("    [3]  Done") 
    status_map = {"1": "pending", "2": "in-progress", "3": "done"}
    new_status = input("  Choose (1/2/3): ").strip()

    if new_status in status_map:
        task["status"] = status_map[new_status]
        save_tasks(tasks)
        print(f"\n    Status updated to {get_status_label(task['status'])}!")
    else: 
        print("\n    Invalid choice. No changes made.")
    input("\n  Press Enter to continue")

def delete_task(tasks):
    print_header() 
    print("     DELETE A TASK \n") 
    if not tasks:
        print("    No tasks to delete.\n") 
        input("  Press Enter to continue...") 
        return
    for i, task in enumerate(tasks):
        print(f"  [{i + 1}] {task['title']}  ({get_status_label(task.get('status','pending'))})")
    print() 
    try:
        choice = int(input("  Enter task number to delete: ")) - 1
        if choice < 0 or choice >= len(tasks): 
            raise ValueError
    except ValueError:
        print("\n    Invalid selection!")
        input("\n  Press Enter to continue...")
        return
    task = tasks[choice]
    confirm = input(f"    Delete '{task['title']}'? (y/n): ").strip().lower()
    if confirm == "y": 
        tasks.pop(choice) 
        save_tasks(tasks)
        print(f"\n    Task deleted successfully!") 
    else:
        print("\n    Deletion cancelled.")
    input("\n  Press Enter to continue...")

def search_tasks(tasks):
    print_header()
    print("     SEARCH TASKS \n")
    if not tasks: 
        print("    No tasks to search.\n")
        input("  Press Enter to continue...")   
        return
    keyword = input("  Enter search keyword: ").strip().lower()
    if not keyword:
        print("\n    Please enter a keyword to search.") 
        input("\n  Press Enter to continue...")
        return
    results = [
        (i, t) for i, t in enumerate(tasks)
        if keyword in t["title"].lower()
        or keyword in t.get("description", "").lower() 
        or keyword in t.get("category", "").lower()
    ]
    if results: 
        print(f"\n  Found {len(results)} result(s):\n") 
        for idx, task in results: 
            display_task(task, idx)
            print() 
    else:
        print(f"\n    No tasks found matching '{keyword}'.")
    input("\n  Press Enter to continue...")

def view_summary(tasks):
    print_header()
    print("     TASK SUMMARY \n")
    total = len(tasks)
    if total == 0: 
        print("    No tasks yet. Add some tasks to see statistics!\n")
        input("  Press Enter to continue...")
        return 
    pending = sum(1 for t in tasks if t.get("status") == "pending")
    in_progress = sum(1 for t in tasks if t.get("status") == "in-progress")
    done = sum(1 for t in tasks if t.get("status") == "done")
    high = sum(1 for t in tasks if str(t.get("priority")) == "1") 
    medium = sum(1 for t in tasks if str(t.get("priority")) == "2")
    low = sum(1 for t in tasks if str(t.get("priority")) == "3")
    completion = (done / total * 100) if total > 0 else 0
    bar_filled = int(completion / 5)
    bar_empty = 20 - bar_filled
    progress_bar = "█" * bar_filled + "░" * bar_empty
    print(f"  Total Tasks: {total}") 
    print_separator()
    print(f"   Status Breakdown:")
    print(f"      Pending      : {pending}") 
    print(f"      In-Progress  : {in_progress}")
    print(f"      Done         : {done}")
    print_separator()
    print(f"   Priority Breakdown:") 
    print(f"      High         : {high}")
    print(f"      Medium       : {medium}") 
    print(f"      Low          : {low}")
    print_separator()
    print(f"   Completion: [{progress_bar}] {completion:.1f}%")
    print() 
    categories = {}
    for t in tasks: 
        cat = t.get("category", "General")
        categories[cat] = categories.get(cat, 0) + 1
    if categories:
        print(f"    Categories:")
        for cat, count in sorted(categories.items()): 
            print(f"     • {cat}: {count} task(s)")
        print()
    input("  Press enter to continue...")
 
def main():
    tasks = load_tasks()
    while True:
        print_header()
        print_menu()
        choice = input("   Enter your choice (1-8): ").strip()
        if choice == "1":
            add_task(tasks) 
        elif choice == "2":
            view_tasks(tasks) 
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            change_status(tasks) 
        elif choice == "5": 
            delete_task(tasks)
        elif choice == "6":
            search_tasks(tasks)  
        elif choice == "7": 
            view_summary(tasks) 
        elif choice == "8": 
            print_header()
            print("    Thank you for using the To-Do List Manager!")  
            print("    Your tasks are saved in: tasks.json")
            break
        else:  
            print("\n    Invalid choice! Please select 1-8.")  
            input("\n  Press Enter to continue...") 
if __name__ == "__main__":
    main()  

    