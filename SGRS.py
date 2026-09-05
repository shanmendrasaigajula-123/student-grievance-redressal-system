grievances =[]
grievances_id = 1

def submit_grievance():
    global grievances_id
    name = input("Enter your name: ")
    category = input("Enter grievance category: ")
    description = input("Describe your grievance: ")

    grievance = {
        "id": grievances_id,
        "name": name,
        "category": category,
        "description": description,
        "status": "Pending",
        "Remarks": "Not Reviewed"
    }
    grievances.append(grievance)
    print(f"Grievance submitted successfully with ID: {grievances_id}\n")
    grievances_id +=1

def view_grievances():
    if not grievances:
        print("No grievances submitted yet.\n")
        return
    for g in grievances:
        print("\n---------------------------\n")
        print("ID         :", g["id"])
        print("Name       :", g["name"])
        print("Category   :", g["category"])
        print("Description:", g["description"])
        print("Status     :", g["status"])
        print("Remarks    :", g["Remarks"])
        print("\n---------------------------\n")

def admin_update():
    gid = int(input("Enter your grievance ID: "))
    
    for g in grievances:
        if g["id"]==gid:
            g["status"] = input("Enter new status (Resolved/Pending): ")
            if g["status"] == "Resolved":
                len(grievances)-1
            g["Remarks"] = input("Enter remarks: ")
            print("\nGrievance updated successfully.")
            return
        
    print("Grievance ID not found.\n")

def student_menu():
    while True:
        print("\n----- Student Menu -----")
        print("1. Submit Grievance")
        print("2. View Grievances")
        print("3. Exit")

        choice = input("enter your choice: ")
        if choice == "1":
            submit_grievance()
        elif choice == "2":
            view_grievances()
        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.\n")

def admin_menu():
    password = input("Enter admin password: ")
    if password != "admin123":
        return
    while True:
        print("Total grievances submitted:", len(grievances))
        print("\n----- Admin Menu -----")
        print("1.view all grievances")
        print("2.update grievance status")
        print("3.exit")

        choice = input("enter your choice: ")
        if choice == "1":
            view_grievances()
        elif choice == "2":
            admin_update()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.\n")

def main():
    while True:
        print("\n----- Grievance Reddressal System -----")
        print("1. Student")
        print("2. Admin")
        print("3. Exit ")

        choice = input("enter your choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            admin_menu()
        elif choice == "3":
            print("Thank you for using the SGRS. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()