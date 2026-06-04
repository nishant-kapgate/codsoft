> CODESOFT Internship Projects
A collection of Python projects built during the **CodSoft Internship Program**.
--

> Projects Overview
| # | Project | Description | Run Command |
-------------------------------------------
  1 - To-Do List (#-1-to-do-list-manager) | Task manager with priorities, statuses & stats | `python todo.py` |
  3 - Password Generator (#-3-password-generator) | Customizable random password generator | `python Pass.py` |
  5 - Contact Book (#-5-contact-book) | Contact manager with colored terminal UI | `python contact.py` |

--
## 1. To-Do List Manager
Path: `1todo_list/todo.py`

A full-featured command-line task manager with filtering, search, and visual statistics.
> Features

 Add Tasks * — Title, description, category & priority (High / Medium / Low)
 View & Filter * — Filter by status (Pending, In-Progress, Done) or high priority
 Update / Delete * — Edit task fields or remove tasks with confirmation
 Search * — Keyword search across title, description & category
 Summary Dashboard * — Visual progress bar, status/priority breakdown, category stats

>  Menu
```
[1] Add a New Task        [5] Delete a Task
[2] View All Tasks        [6] Search Tasks
[3] Update a Task         [7] View Summary / Statistics
[4] Change Task Status    [8] Exit
```

> Storage
Tasks are persisted in `tasks.json` (auto-created on first use).

---
## 3. Password Generator
Path: `3password_gener/Pass.py`
A simple and effective random password generator with full control over character types.

> Features
* Custom Length * — Choose any password length (1+)
* Character Control * — Toggle uppercase, lowercase, digits & symbols independently
* Regenerate * — Generate multiple passwords in one session
* Validation * — Handles invalid inputs gracefully

> Usage Example
```
===== Password Generator =====
Enter password length: 10
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include symbols? (y/n): y

Your generated password: asaDF6@h#K
Password length: 10
```
---
##  5. Contact Book

Path: `5contact_book/contact.py`
A colorful terminal-based contact manager with ANSI-styled UI, table displays, and input validation.

> Features
* Add / View / Search / Update / Delete * contacts
* Validation * — Phone format (7–15 digits) and email format checking
* Table Display * — Aligned columns with box-drawing characters (┌─┬─┐ │ └─┴─┘)
* Color UI * — Cyan headers, green success (✔), red errors (✘), yellow warnings (⚠)

> Menu
```
[1] Add Contact       [4] Update Contact
[2] View All Contacts [5] Delete Contact
[3] Search Contact    [6] Exit
```

> Storage
Contacts are persisted in `contacts.json` (auto-created on first use).

---
##  Tech Stack

-**Language:** Python 3
-**Storage:** JSON files
-**Dependencies:** None — all projects use the standard library only

##  Project Structure

```
CODESOFT/
├── README.md
├── 1todo_list/
│   └── todo.py
├── 3password_gener/
│   └── Pass.py
└── 5contact_book/
    └── contact.py
```
## How to Run the Projects

Clone the repository-
git clone https://github.com/modx99/CoDESoFT.git

Navigate to the project folder-
cd CODSOFT

Run any project >
**Example:**
python todo.py