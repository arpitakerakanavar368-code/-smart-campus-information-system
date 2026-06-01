import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

while True:
    print("\n===== SMART CAMPUS INFORMATION SYSTEM =====")
    print("1. Student Registration and Grade Evaluation")
    print("2. Course Enrollment Management")
    print("3. Student Record Data Management")
    print("4. Sorting and Searching Student IDs")
    print("5. Student Fee Calculation")
    print("6. File Handling for Student Records")
    print("7. Directory Scanning")
    print("8. Student Performance Analysis")
    print("9. Exit")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        student_name = input("Enter student name: ")
        score = float(input("Enter exam score (0-100): "))

        if score >= 90 and score <= 100:
            grade = "A"
            remark = "Excellent"
        elif score >= 75:
            grade = "B"
            remark = "Very Good"
        elif score >= 60:
            grade = "C"
            remark = "Good"
        elif score >= 40:
            grade = "D"
            remark = "Average"
        else:
            grade = "F"
            remark = "Needs Improvement"

        print("\n--- Student Report ---")
        print("Name:", student_name)
        print("Score:", score)
        print("Grade:", grade)
        print("Performance Remark:", remark)

    elif choice == 2:
        courses = []
        max_courses = 5

        print("\n=== Course Enrollment System ===")

        while True:
            if len(courses) >= max_courses:
                print("Maximum course limit reached!")
                break

            course_name = input("Enter course name (or 'done' to finish): ")

            if course_name.lower() == "done":
                break

            credits = input("Enter credit value: ")

            if not credits.isdigit():
                print("Invalid credit value! Skipping entry...")
                continue

            credits = int(credits)

            if credits <= 0:
                print("Credit must be positive! Skipping entry...")
                continue

            courses.append((course_name, credits))
            print(f"Course '{course_name}' with {credits} credits added.")

        print("\n--- Enrollment Report ---")
        for course, credit in courses:
            print("Course:", course, "Credits:", credit)

        print("Total courses enrolled:", len(courses))

    elif choice == 3:
        students = []
        students.append({"name": "Priya", "age": 20, "grades": [85, 90, 78]})
        students.append({"name": "Rahul", "age": 21, "grades": [72, 88, 91]})
        students.append({"name": "Anita", "age": 19, "grades": [95, 89, 92]})

        print("\n=== Student Records ===")
        for student in students:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Grades:", student["grades"])
            print("---------------------")

        event_A = {"Priya", "Rahul", "Anita", "Kiran"}
        event_B = {"Rahul", "Anita", "Sneha"}

        print("\n=== Event Participation Analysis ===")
        print("Common Participants:", event_A & event_B)
        print("All Participants:", event_A | event_B)
        print("Only Event A Participants:", event_A - event_B)

    elif choice == 4:
        student_ids = [105, 102, 110, 108, 101, 115]
        print("Original IDs:", student_ids)

        n = len(student_ids)
        for i in range(n):
            for j in range(0, n - i - 1):
                if student_ids[j] > student_ids[j + 1]:
                    student_ids[j], student_ids[j + 1] = student_ids[j + 1], student_ids[j]

        print("Sorted IDs:", student_ids)

        target = int(input("Enter Student ID to search: "))

        found_index = -1
        for i in range(len(student_ids)):
            if student_ids[i] == target:
                found_index = i
                break

        if found_index != -1:
            print("Linear Search: ID", target, "found at index", found_index)
        else:
            print("Linear Search: ID not found")

        low = 0
        high = len(student_ids) - 1
        found_index = -1

        while low <= high:
            mid = (low + high) // 2
            if student_ids[mid] == target:
                found_index = mid
                break
            elif student_ids[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if found_index != -1:
            print("Binary Search: ID", target, "found at index", found_index)
        else:
            print("Binary Search: ID not found")

    elif choice == 5:
        def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
            return tuition_fee + hostel_fee + transportation_fee

        tuition = int(input("Enter Tuition Fee: "))
        hostel = int(input("Enter Hostel Fee: "))
        transport = int(input("Enter Transportation Fee: "))

        print("Total Fee =", calculate_fee(tuition, hostel, transport))

    elif choice == 6:
        with open("student_records.txt", "w") as file:
            file.write("ID,Name,Marks\n")
            file.write("101,Arjun,85\n")
            file.write("102,Meera,92\n")
            file.write("103,Ravi,76\n")
            file.write("104,Anita,89\n")

        print("Student records written successfully.")

    elif choice == 7:
        class MissingFileOrFolderError(Exception):
            pass

        def scan_directory(path):
            try:
                if not os.path.exists(path):
                    raise FileNotFoundError(f"Invalid directory path: {path}")

                for root, dirs, files in os.walk(path):
                    print(root)

            except Exception as e:
                print("Error:", e)

        directory_path = input("Enter directory path to scan: ")
        scan_directory(directory_path)

    elif choice == 8:
        try:
            df = pd.read_csv("student_performance.csv")
            print(df.head())
        except Exception as e:
            print("Error:", e)

    elif choice == 9:
        print("Thank You")
        break

    else:
        print("Invalid Choice! Please enter 1 to 9.")
