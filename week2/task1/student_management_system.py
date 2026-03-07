import json

class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.id = student_id
        self.grade = grade

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Grade: {self.grade}"

class StudentManager:
    def __init__(self):
        self.students = []
        self.load_data()

    def add_student(self, name, student_id, grade):
        for s in self.students:
            if s.id == student_id:
                print("Error: ID already exist!")
                return
        new_student = Student(name, student_id, grade)
        self.students.append(new_student)
        self.save_data()
        print("Student added successfully!")

    def update_student(self, student_id):
        for s in self.students:
            if s.id == student_id:
                print(f"Old records: {s}")
                
                new_name = input("Enter new name (Keep empty if you not want to change): ")
                new_grade = input("Enter new grade (Keep empty if you not want to change): ")

                if new_name:
                    s.name = new_name
                if new_grade:
                    s.grade = new_grade
                
                self.save_data()
                print("Record updated successfully!")
                return
        
        print("Error: No student found with this id.")

    def list_students(self):
        if not self.students:
            print("Record is empty.")
            return
        
        print(f"{'ID':<10} {'Name':<20} {'Grade':<5}")
        print("-" * 35)
        
        for s in self.students:
            print(f"{s.id:<10} {s.name:<20} {s.grade:<5}")

    def delete_student(self, student_id):
        original_count = len(self.students)
        self.students = [s for s in self.students if s.id != student_id]
        
        if len(self.students) < original_count:
            self.save_data()
            print("Student deleted successfully!")
        else:
            print("Error: No student found with this id.")

    def save_data(self):
        data = [{"id": s.id, "name": s.name, "grade": s.grade} for s in self.students]
        with open("students.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open("students.json", "r") as f:
                data = json.load(f)
                self.students = [Student(d['name'], d['id'], d['grade']) for d in data]
        except FileNotFoundError:
            self.students = []

# 3. Main Program
manager = StudentManager()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. List Students")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Exit")
    
    choice = input("Please choose one option (1-5): ")

    if choice == "1":
        while True:
            name = input("Enter student name: ")
            if not name.isalpha():
                print("Error: Name should only have alphabets!")
                continue 
            if len(name)<3:
                print("Error: Invalid name!")
                continue
            break

        while True:
            student_id = input("Enter student id (only integer): ")
            if not student_id.isdigit():
                print("Error: Invalid id!")
                continue
            break
        while True:
            grade = input("Grade (A, B, C, F): ").upper()
            if grade not in ['A', 'B', 'C', 'D', 'F']:
                print("Error: Grade should be only A, B, C, D, or F!")
                continue
            break

        manager.add_student(name, student_id, grade)
    elif choice == "2":
            manager.list_students()
            
    elif choice == "3":
        i = input("Enter id for delete: ")
        manager.delete_student(i)
        
    elif choice == "4":
        i = input("Enter id for update: ")
        manager.update_student(i) 
        
    elif choice == "5":
        print("Good Bye!")
        break
    else:
        print("Invalid choice! Try again.")
