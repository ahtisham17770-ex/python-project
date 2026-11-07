import pytest

from project import (
    assessment,
    calculate_mean,
    passed_students,
    find_topper,
    load_student_data,
)


# Sample student records used in different tests
def sample_students():
    return [
        {"name": "Ali", "marks": 80.0, "attendance": 90.0},
        {"name": "Sara", "marks": 45.0, "attendance": 55.0},
        {"name": "Ahmed", "marks": 60.0, "attendance": 70.0},
    ]


# Check whether the average marks are calculated correctly
def test_calculate_mean():
    assert calculate_mean(sample_students()) == pytest.approx(61.6667, rel=1e-3)


# Check whether the student with the highest marks is identified
def test_find_topper():
    assert find_topper(sample_students())["name"] == "Ali"


# Check whether the number of passed students is correct
def test_passed_students():
    assert passed_students(sample_students()) == 2


# Check whether students receive the correct assessment
def test_assessment():
    students = sample_students()

    assert assessment(students[0]) == "Doing well!"
    assert assessment(students[1]) == "Needs Attention!"
    assert assessment(students[2]) == "Needs Improvement!"


# Check whether student records are loaded correctly from a CSV file
def test_load_student_data(tmp_path):
    csv_file = tmp_path / "students.csv"

    csv_file.write_text("name,marks,attendance\nAli,80,90\nSara,45,55\n",encoding="utf-8")

    students = load_student_data(csv_file)

    assert len(students) == 2
    assert students[0]["name"] == "Ali"
    assert students[1]["marks"] == 45.0


# Check whether invalid marks are rejected
def test_load_student_data_invalid_marks(tmp_path):
    csv_file = tmp_path / "students.csv"

    csv_file.write_text("name,marks,attendance\nAli,150,90\n",encoding="utf-8")

    with pytest.raises(ValueError):
        load_student_data(csv_file)


# Check whether invalid attendance is rejected
def test_load_student_data_invalid_attendance(tmp_path):
    csv_file = tmp_path / "students.csv"

    csv_file.write_text("name,marks,attendance\nAli,80,120\n",encoding="utf-8")

    with pytest.raises(ValueError):
        load_student_data(csv_file)