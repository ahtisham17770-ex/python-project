# Student Result Analyzer

### CS50P Final Project

## About the Project

Student Result Analyzer is a Python command-line application that I built as my final project for CS50's Introduction to Programming with Python.

The main idea behind this project is to make student result analysis easier. Instead of manually calculating averages, counting passed students, and checking individual performance, the program handles these tasks using student data stored in a CSV file.

It reads the records, validates the data, performs calculations, and generates a report showing the overall class performance and individual student assessments.

I also used the Rich library to make the terminal output cleaner and easier to read.

## Features

- **CSV File Handling:** Reads student records from a CSV file.
- **Data Validation:** Checks student names, marks, attendance, and required CSV columns.
- **Class Average:** Calculates the average marks of all students.
- **Topper Identification:** Finds the student with the highest marks.
- **Passed Students:** Counts students who scored at least 50 marks.
- **Student Assessment:** Evaluates students based on their marks and attendance.
- **Formatted Reports:** Uses Rich to display results in colorful tables and panels.
- **Command-Line Interface:** Allows users to provide a CSV filename through the terminal.
- **Unit Testing:** Uses pytest to test the main functions.

## Project Structure

```text
student-result-analyzer/
│
├── project.py
├── test_project.py
├── students.csv
├── requirements.txt
└── README.md
```

## Technologies and Libraries

- **Python 3:** Main programming language.
- **CSV:** For reading student records.
- **Argparse:** For handling command-line arguments.
- **Statistics:** For calculating average marks.
- **Rich:** For displaying formatted tables and reports in the terminal.
- **Pytest:** For testing the program.

## Installation

First, clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project folder:

```bash
cd student-result-analyzer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Run the program using:

```bash
python project.py students.csv
```

You can replace `students.csv` with the path to another CSV file containing student records.

## CSV File Format

The program expects a CSV file with three columns:

| Column | Description |
| `name` | Student's name |
| `marks` | Student's marks (0–100) |
| `attendance` | Attendance percentage (0–100) |

Example:

```csv
name,marks,attendance
Ali,85,90
Sara,45,55
Ahmed,70,80
Usman,92,95
```

## Student Assessment

The program checks each student's marks and attendance and provides a basic assessment.

| Condition | Assessment |

| Marks ≤ 50 and attendance < 60% | Needs Attention! |
| Marks ≤ 70 and attendance < 75% | Needs Improvement! |
| Otherwise | Doing well! |

A student needs at least 50 marks to pass.

## Terminal Output

I used the Rich library to improve how the results are displayed in the terminal.

Instead of showing everything as plain text, the program uses:

- Tables to display individual student results.
- Panels to show the overall class summary.
- Colors and formatting to make important information easier to identify.

The report includes the total number of students, passed students, class average, topper, and individual assessments.

## Running Tests

I included a separate test file to check whether the main functions are working correctly.

To run the tests:

```bash
pytest -v
```

The tests cover calculations, topper identification, passed students, student assessments, and CSV data loading.

## What I Learned

Working on this project helped me understand how different Python concepts can be combined to build a practical application.

During development, I got more experience with:

- Reading and processing CSV files.
- Writing reusable functions.
- Working with lists and dictionaries.
- Handling invalid data and exceptions.
- Using command-line arguments.
- Displaying formatted terminal output with Rich.
- Writing automated tests with pytest.

## Author

Created as my final project for **CS50's Introduction to Programming with Python (CS50P)**.