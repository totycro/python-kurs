"""
1) Die durchschnittliche Studiendauer ist 7 Jahre für Leute die nicht an der PH sind. Wann werden diese durchschnittlich fertig?
2) Wie viele dieser nicht-PH-Studierenden waren die ersten 500 Matrikulierten im Jahr und studieren an der Boku?
"""

import statistics



students = ["h01534001", "a02239332"]
average_duration = 7

non_ph_students = [
    student_id
    for student_id in students
    if student_id[1] != "4"
]

average_expected_finish_years = statistics.mean(
    [
        int(student_id[2:3]) + average_duration
        for student_id in non_ph_students
    ]
)

first_100_of_boku = len(
    [
        student_id
        for student_id in non_ph_students
        if int(student_id[-3]) <= 5 and student_id[0] == 'h'
    ]
)



expected_finish_years = []
first_100_of_boku = 0

for student_id in students:

    if student_id[1] != "4":

        expected_finish_years.append(int(student_id[2:3]) + average_duration)

        if int(student_id[-3]) <= 5 and student_id[0] == 'h':
            first_100_of_boku = first_100_of_boku + 1

average_expected_finish_years = statistics.mean(expected_finish_years)
