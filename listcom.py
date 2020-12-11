"""
1) Die durchschnittliche Studiendauer ist 7 Jahre für Leute die nicht an der PH sind. Wann werden diese durchschnittlich fertig?
2) Wie viele dieser nicht-PH-Studierenden waren die ersten 500 Matrikulierten im Jahr und studieren an der Boku?
"""

import statistics


students = ["h01812345", "h01600123", "z41774632"]
average_duration = 7
non_ph_students = [
    student_id
    for student_id in students
    if student_id[1] != "4"
]
expected_finish_years = [
    int(student_id[2:4]) + average_duration
    for student_id in non_ph_students
]
average_expected_finish_years = statistics.mean(expected_finish_years)

first_of_year_of_boku = len(
    [
        student_id
        for student_id in non_ph_students
        if int(student_id[-5:]) <= 500 and student_id[0] == 'h'
    ]
)

print(1)
print(average_expected_finish_years)
print(first_of_year_of_boku)


expected_finish_years = []
first_of_year_of_boku = 0

for student_id in students:

    if student_id[1] != "4":

        expected_finish_years.append(int(student_id[2:4]) + average_duration)

        if int(student_id[-5:]) <= 500 and student_id[0] == 'h':
            first_of_year_of_boku = first_of_year_of_boku + 1

average_expected_finish_years = statistics.mean(expected_finish_years)

print()
print(2)
print(average_expected_finish_years)
print(first_of_year_of_boku)


