# Class Attendance Management System
# Language: Python

students = ["Padmaveer", "Yashasvi", "Sanika", "Rutuja", "Karan"]
attendance = {}

def mark_attendance():
    print("\n--- Mark Attendance ---")
    for student in students:
        status = input(f"Is {student} present? (P/A): ").upper()
        if status == "P":
            attendance[student] = "Present"
        else:
            attendance[student] = "Absent"
    print("Attendance marked successfully.")

def view_attendance():
    print("\n--- Attendance Record ---")
    if not attendance:
        print("No attendance marked yet.")
    else:
        for student, status in attendance.items():
            print(f"{student} : {status}")

def main_menu():
    while True:
        print("\n===== CLASS ATTENDANCE SYSTEM =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Thank you! Exiting system.")
            break
        else:
            print("Invalid choice. Try again.")

main_menu()
