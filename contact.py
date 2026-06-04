import json
import os
import re
import sys
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.json")
class Color:
    HEADER    = "\033[95m"
    BLUE      = "\033[94m"
    CYAN      = "\033[96m"
    GREEN     = "\033[92m"
    YELLOW    = "\033[93m"
    RED       = "\033[91m"
    BOLD      = "\033[1m"
    UNDERLINE = "\033[4m"
    DIM       = "\033[2m"
    RESET     = "\033[0m"
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def pause():
    input(f"\n{Color.DIM}  Press Enter to continue...{Color.RESET}")
def print_header(title: str):
    width = 60
    print(f"\n{Color.CYAN}{Color.BOLD}  ╔{'═' * (width - 2)}╗")
    print(f"  ║{title:^{width - 2}}║")
    print(f"  ╚{'═' * (width - 2)}╝{Color.RESET}\n")
def print_success(message: str):
    print(f"  {Color.GREEN}✔ {message}{Color.RESET}")
def print_error(message: str):
    print(f"  {Color.RED}✘ {message}{Color.RESET}")
def print_warning(message: str):
    print(f"  {Color.YELLOW}⚠ {message}{Color.RESET}")
def print_info(message: str):
    print(f"  {Color.BLUE}ℹ {message}{Color.RESET}")
def validate_phone(phone: str) -> bool:
    return bool(re.match(r'^[\d\s\+\-\(\)]{7,15}$', phone.strip()))
def validate_email(email: str) -> bool: 
    if not email.strip():
        return True  # Email is optional
    return bool(re.match(r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$', email.strip()))
def load_contacts() -> list:
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []
def save_contacts(contacts: list):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print_error(f"Failed to save contacts: {e}")
def display_contact_table(contacts: list):
    if not contacts:
        print_warning("No contacts to display.")
        return
    w_no    = 4
    w_name  = 22
    w_phone = 16
    w_email = 28
    w_addr  = 22
    separator = f"  ├{'─' * w_no}┼{'─' * w_name}┼{'─' * w_phone}┼{'─' * w_email}┼{'─' * w_addr}┤"
    top_line  = f"  ┌{'─' * w_no}┬{'─' * w_name}┬{'─' * w_phone}┬{'─' * w_email}┬{'─' * w_addr}┐"
    bot_line  = f"  └{'─' * w_no}┴{'─' * w_name}┴{'─' * w_phone}┴{'─' * w_email}┴{'─' * w_addr}┘"
    def trunc(text: str, width: int) -> str:
        s = str(text)
        limit = width - 2
        if len(s) <= limit:
            return s
        chars: list[str] = []
        for i in range(limit - 1):
            chars.append(s[i])
        return "".join(chars) + "..."
    print(f"{Color.CYAN}{top_line}")
    print(f"  │{'No':^{w_no}}│{'Name':^{w_name}}│{'Phone':^{w_phone}}│{'Email':^{w_email}}│{'Address':^{w_addr}}│")
    print(separator + Color.RESET)
    for i, c in enumerate(contacts, 1):
        name  = trunc(c.get("name", "N/A"), w_name)
        phone = trunc(c.get("phone", "N/A"), w_phone)
        email = trunc(c.get("email", "—"), w_email)
        addr  = trunc(c.get("address", "—"), w_addr)
        row_color = Color.DIM if i % 2 == 0 else ""
        print(f"{row_color}  │{i:^{w_no}}│ {name:<{w_name - 1}}│ {phone:<{w_phone - 1}}│ {email:<{w_email - 1}}│ {addr:<{w_addr - 1}}│{Color.RESET}")
    print(f"{Color.CYAN}{bot_line}{Color.RESET}")
    print(f"\n  {Color.DIM}Total: {len(contacts)} contact(s){Color.RESET}")


def display_single_contact(contact: dict, index: int | None = None):
    prefix = f"  [{index}] " if index is not None else "  "
    print(f"{Color.BOLD}{prefix}📇 {contact.get('name', 'N/A')}{Color.RESET}")
    print(f"       Phone   : {Color.GREEN}{contact.get('phone', 'N/A')}{Color.RESET}")
    print(f"       Email   : {Color.BLUE}{contact.get('email', '—') or '—'}{Color.RESET}")
    print(f"       Address : {Color.YELLOW}{contact.get('address', '—') or '—'}{Color.RESET}")
    print(f"      {'─' * 40}")

def add_contact(contacts: list):
    print_header("  ADD NEW CONTACT")

    name = input(f"  {Color.BOLD}Name{Color.RESET} (required): ").strip()
    if not name:
        print_error("Name cannot be empty. Contact not added.")
        return

    while True:
        phone = input(f"  {Color.BOLD}Phone{Color.RESET} (required): ").strip()
        if not phone:
            print_error("Phone number is required.")
            continue
        if not validate_phone(phone):
            print_error("Invalid phone number. Use 7-15 digits (may include +, -, spaces).")
            continue
        break

    while True:
        email = input(f"  {Color.BOLD}Email{Color.RESET} (optional): ").strip()
        if not validate_email(email):
            print_error("Invalid email format. Try again or leave blank.")
            continue
        break

    address = input(f"  {Color.BOLD}Address{Color.RESET} (optional): ").strip()
    contact = {
        "name": name,
        "phone": phone,
        "email": email if email else "",
        "address": address if address else "",
    }
    contacts.append(contact)
    save_contacts(contacts)
    print()
    print_success(f"Contact '{name}' added successfully!")
    display_single_contact(contact)
def view_contacts(contacts: list): 
    print_header("  ALL CONTACTS") 
    display_contact_table(contacts) 
def search_contacts(contacts: list):
    print_header("  SEARCH CONTACTS")

    if not contacts:
        print_warning("Contact book is empty. Nothing to search.")
        return
    query = input(f"  Enter name or phone to search: ").strip().lower()
    if not query: 
        print_error("Search query cannot be empty.")
        return 
    results = [
        c for c in contacts 
        if query in c.get("name", "").lower() or query in c.get("phone", "")
    ]
    if results:
        print(f"\n  {Color.GREEN}Found {len(results)} result(s):{Color.RESET}\n")
        for i, c in enumerate(results, 1): 
            display_single_contact(c, i)
    else:
        print_warning(f"No contacts found matching '{query}'.")

def update_contact(contacts: list):
    print_header("    UPDATE CONTACT")

    if not contacts:
        print_warning("Contact book is empty. Nothing to update.") 
        return 
    display_contact_table(contacts)
    try:
        idx = int(input(f"\n  Enter contact number to update (1-{len(contacts)}): ")) - 1
        if idx < 0 or idx >= len(contacts):
            print_error("Invalid contact number.")
            return
    except ValueError:
        print_error("Please enter a valid number.")
        return
    contact = contacts[idx] 
    print(f"\n  {Color.BOLD}Editing: {contact['name']}{Color.RESET}")
    print(f"  {Color.DIM}(Leave blank to keep current value){Color.RESET}\n") 
    new_name = input(f"  Name [{contact['name']}]: ").strip()
    if new_name: 
        contact["name"] = new_name
    while True:
        new_phone = input(f"  Phone [{contact['phone']}]: ").strip() 
        if not new_phone:
            break
        if validate_phone(new_phone): 
            contact["phone"] = new_phone
            break
        print_error("Invalid phone number format.")
    while True:
        new_email = input(f"  Email [{contact.get('email', '—')}]: ").strip()
        if not new_email:
            break
        if validate_email(new_email):
            contact["email"] = new_email 
            break
        print_error("Invalid email format.")
    new_address = input(f"  Address [{contact.get('address', '—')}]: ").strip()
    if new_address:
        contact["address"] = new_address
    save_contacts(contacts)
    print()
    print_success(f"Contact '{contact['name']}' updated successfully!")
    display_single_contact(contact) 
def delete_contact(contacts: list): 
    print_header("   DELETE CONTACT") 

    if not contacts:
        print_warning("Contact book is empty. Nothing to delete.") 
    return
    display_contact_table(contacts)
    try:
        idx = int(input(f"\n  Enter contact number to delete (1-{len(contacts)}): ")) - 1
        if idx < 0 or idx >= len(contacts):
            print_error("Invalid contact number.")
            return
    except ValueError:
        print_error("Please enter a valid number.")
        return
    contact = contacts[idx] 
    confirm = input( 
        f"\n  {Color.RED}Are you sure you want to delete '{contact['name']}'? (y/n): {Color.RESET}" 
    ).strip().lower()
    if confirm == "y": 
        contacts.pop(idx) 
        save_contacts(contacts)
        print_success(f"Contact '{contact['name']}' deleted successfully!") 
    else: 
        print_info("Deletion cancelled.")
def show_menu():
    clear_screen()
    print(f"""
{Color.CYAN}{Color.BOLD}
                                                             
                 C O N T A C T   B O O K
                                                              
        {Color.GREEN}[1]{Color.CYAN}     Add Contact                                
        {Color.GREEN}[2]{Color.CYAN}     View All Contacts                         
        {Color.GREEN}[3]{Color.CYAN}     Search Contact                            
        {Color.GREEN}[4]{Color.CYAN}      Update Contact                            
        {Color.GREEN}[5]{Color.CYAN}      Delete Contact                            
        {Color.RED}[6]{Color.CYAN}     Exit                                      
{Color.RESET}""")
def main():
    contacts = load_contacts()
    while True:
        show_menu()
        print(f"  {Color.DIM}Contacts stored: {len(contacts)}{Color.RESET}\n")
        choice = input(f"  {Color.BOLD}Choose an option (1-6): {Color.RESET}").strip()
        if choice == "1":
            add_contact(contacts)
            pause()
        elif choice == "2":
            view_contacts(contacts)
            pause()
        elif choice == "3":
            search_contacts(contacts)
            pause()
        elif choice == "4":
            update_contact(contacts)
            pause()
        elif choice == "5":
            delete_contact(contacts)
            pause()
        elif choice == "6":
            clear_screen()
            print(f"""
{Color.CYAN}{Color.BOLD}
                                                              
                Thank you for using Contact Book             
                                                               
                   Bye & have a great time!                                                                   
{Color.RESET}""")
            sys.exit(0)
        else:
            print_error("Invalid option. Please choose 1-6.")
            pause()

if __name__ == "__main__":
    main()




