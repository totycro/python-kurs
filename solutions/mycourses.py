courses_2021 = [
    {
        "lecturer": "B",
        "name": "Python",
        "grade": 2,
    },
    {
        "lecturer": "A",
        "name": "Holzverarbeitung 1",
    },
    {
        "lecturer": "A",
        "name": "Holzverarbeitung 2",
    },
]

def course_names(courses):
    return sorted([course['name'] for course in courses])


def lecturers(courses):
    lecturers = []
    for course in courses:
        if course['lecturer'] not in lecturers:
            lecturers.append(course['lecturer'])
    return lecturers


def lecturers_advanced(courses):
    return set(course['lecturer'] for course in courses)


def ungraded_courses(courses):
    return [
        course
        for course in courses
        if 'grade' not in course
    ]


def average_grade(courses):
    grades = [
        course['grade']
        for course in courses
        if 'grade' in course
    ]
    return sum(grades) / len(grades)


def courses_with_good_grades(courses, up_to=3):
    return [
        course
        for course in courses
        if course.get('grade', 100) < up_to
    ]



# Kurs hinzufügen:
# courses.append(course)


def add_grade(courses, course_name, grade):
    for course in courses:
        if course['name'] == course_name:
            course['grade'] = grade


