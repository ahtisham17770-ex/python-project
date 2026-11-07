import csv
from statistics import mean
import argparse

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Read student records from a CSV file and validate the data
def load_student_data(file):

    with open(file, "r", newline="", encoding="utf-8") as data:
        reader = csv.DictReader(data)
        fields = {"name", "marks", "attendance"}
        students = []

        if not fields.issubset(reader.fieldnames or []):
            raise ValueError("Required columns: name, marks, attendance")
        for rows in reader:
            try:
                name = (rows.get("name") or "").strip()
                if not name:
                    raise ValueError("Student name is required")
                student = {
                    "name": name,
                    "marks": float(rows["marks"]),
                    "attendance": float(rows["attendance"])
                }

            except (ValueError, TypeError) as error:
                raise ValueError("Invalid student data in CSV file") from error

            if not 0 <= student["marks"] <= 100:
                raise ValueError("Marks must be between 0 and 100")

            if not 0 <= student["attendance"] <= 100:
                raise ValueError("Attendance must be between 0 and 100")

            students.append(student)

    return students

# Calculate the average marks of students
def calculate_mean(student):

    if not student:
        raise ValueError("No student records available")

    return mean(students["marks"] for students in student)


# Find the student with the highest marks
def find_topper(student):

    if not student:
        raise ValueError("No student records available")

    topper = max(student, key=lambda students: students["marks"])

    return topper


# Calculate the total number of passed students
def passed_students(student):

    passing_marks = 50
    return sum(students["marks"] >= passing_marks for students in student)


# Provide an assessment based on marks and attendance
def assessment(student):

    if student["marks"] <= 50 and student["attendance"] < 60:
        return "Needs Attention!"

    elif student["marks"] <= 70 and student["attendance"] < 75:
        return "Needs Improvement!"

    else:
        return "Doing well!"


# Display the final student report using Rich
def report(students):
    if not students:
        console.print("[bold yellow]No student records found.[/]")
        return
    average = calculate_mean(students)
    topper = find_topper(students)
    passed = passed_students(students)
    total = len(students)

    # Display overall class summary
    summary = (
        f"[bold cyan]Total Students: {total}[/]\n"
        f"[bold green]Passed Students: {passed}[/]\n"
        f"[bold yellow]Class Average: {average:.2f}[/]\n"
        f"[bold blue]Class Topper: {topper['name']}[/]"
    )

    console.print(
        Panel(
            summary,
            title="Student Result Summary",
            border_style="blue"
        )
    )
    # Create a table for individual student results
    table = Table(
        title="Detailed Student Assessment",
        show_header=True,
        border_style="blue"
    )

    table.add_column("Student Name", justify="center", style="cyan")
    table.add_column("Marks", justify="center", style="green")
    table.add_column("Attendance", justify="center", style="yellow")
    table.add_column("Assessment", justify="center", style="blue")

    for student in students:

        table.add_row(
            student["name"],
            str(student["marks"]),
            f"{student['attendance']}%",
            assessment(student)
        )

    console.print(table)

# Main function: get the CSV filename from the command line
def main():

    parser = argparse.ArgumentParser(
        description="Student Result Analyzer from a CSV file"
    )

    parser.add_argument("file", help="Path to the student CSV file")
    args = parser.parse_args()

    try:
        students = load_student_data(args.file)
        report(students)

    except (FileNotFoundError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
