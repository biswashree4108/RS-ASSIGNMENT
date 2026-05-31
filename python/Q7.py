students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = int(input("Enter marks: "))
    students[roll_no] = {
        "Name": name,
        "Marks": marks
    }
print("\nStudent Records")
for roll_no, details in students.items():
    print("Roll No:", roll_no)
    print("Name:", details["Name"])
    print("Marks:", details["Marks"])
    print()