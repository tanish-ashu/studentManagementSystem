from student_module import add_student, view_student, update_student, delete_student
import datetime

def main():
    while True:
        print("\n Student Management System")
        print("1. Add student")
        print("2. View students")
        print("3. Update students")
        print("4. Delete students")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            first_name = input("first name: ")
            last_name = input("last name: ")
            date_of_birth = input ("Date of birth (yyyy-mm-dd:")
            address = input("Address: ")
            phone_number = input("phone number: ")
            email = input("Email: ")
            enrollment_date = datetime.date.today()
            
            add_student(first_name, last_name, date_of_birth, address, phone_number, email, enrollment_date)
            print("Student added Successfully.")
            
        elif choice == "2":
            view_student()
            
        elif choice == "3":
            student_id = int(input("Student ID to update: "))
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            date_of_birth = input("Date of Birth (YYYY-MM-DD): ")
            address = input("Address: ")
            phone_number = input("Phone Number: ")
            email = input("Email: ")
            enrollment_date = datetime.date.tody()
            
            update_student(student_id, first_name, last_name, date_of_birth, address, phone_number, enrollment_date)
            print("Student updated successfully.")
            
        elif choice == "4":
            student_id = int(input("Student ID to delete: "))
            delete_student(student_id)
            print("Student deleted sucessfully.")
        
        elif choice == "5":
            break 
        
        else:
            print("Invalid choice.")
            
if __name__ == "__main__":
    main()
            
