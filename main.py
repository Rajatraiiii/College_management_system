import json
import sys
from faculty import faculty_menu
from Course import course_menu
from Student import student_menu
from Fees import fees_menu

FILE = "data/students.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_menu():
    print("\n===== COLLEGE MANAGEMENT SYSTEM =====")
    print("1. Student Management")
    print("2. Faculty Management")
    print("3. Course Management")
    print("4. Fees & Reports")
    print("5. Exit")

def run(choice):
    if choice == 1:
        print("Running Student Module...")
        student_menu()
    elif choice == 2:
        print("Running Faculty Module...")
        faculty_menu()
    elif choice == 3:
        print("Running Course Module...")
        course_menu()
    elif choice == 4:
        print("Running Fees Module...")
        fees_menu()
    elif choice == 5:
        print("Thank You!")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    show_menu()

    # ✅ Jenkins-friendly input
    if len(sys.argv) > 1:
        choice = int(sys.argv[1])
    else:
        choice = 1  # default

    run(choice)
