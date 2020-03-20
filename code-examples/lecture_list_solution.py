def sorted_courses(courses):
    return sorted([course['name'] for course in courses])


def sorted_courses_2(courses):
    names = []
    for course in courses:
        names.append(course['name'])
    names.sort()
    return names


def get_lecturers(courses):
#     set(course['lecturer'] for course in courses)
    lecturers = []
    for course in courses:
        lecturer = course['lecturer']
        if lecturer not in lecturers:
            lecturers.append(lecturer)
            
    return lecturers


def courses_without_grades(courses):
    return [course['name'] for course in courses if 'grade' not in course]


def courses_with_good_grades(courses):
    return [course['name'] for course in courses if course.get('grade') in [1,2,3] ]


def add_course(courses, new_course):
    courses.append(new_course)
    
    
def add_course_2(courses, new_course):
    return courses + [new_course]

    
def add_grade_for_course(courses, name, grade):
    for course in courses:
        if course['name'] == name:
            course['grade'] = grade
                

def main():
    courses = [
        {
            "name": "Mathe",
            "lecturer": "X",
            "grade": 2,
        },
        {
            "name": "Mathe 2",
            "lecturer": "X",
        },
        {
            "name": "Holzkunde",
            "lecturer": "Y",
            "grade": 4,
        },
    ]
    courses_collegue = [
        {
            "name": "Mathe",
            "lecturer": "X",
            "grade": 1,
        },
        {
            "name": "Holzkunde",
            "lecturer": "Y",
            "grade": 4,
        },
    ]
    add_grade_for_course(courses, name="Mathe 2", grade=1)
    # to add grade:
    # courses[1]['grade'] = 2
    #   OR
    # mathe2 = courses[1]
    # mathe2['grade'] = 3
    print(courses_with_good_grades(courses))
    return courses
#     print("meine:")
#     print(sorted_courses_2(courses))
#     print("kollege:")
#     print(sorted_courses_2(courses_collegue))
    
    
# courses = main()

prices = {
    'apple': 1,
    'pear': 4,
}

mathe = {"name": "Mathe"}


def add_participant(course, name):
    course.setdefault('participants', []).append(name)
    
print(mathe)
add_participant(mathe, name="Bernhard")
print(mathe)
add_participant(mathe, name="Alex")
print(mathe)