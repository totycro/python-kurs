

courses_and_details = {"name" : [], "lecturer" : [], "grade" : []}

def add_coursedetails (name, lecturer, grade = 0):
    for i in courses_and_details:
        if i == "name":
            courses_and_details[i].append (name)
        elif i == "lecturer":
            courses_and_details[i].append (lecturer)
        elif i == "grade":
            courses_and_details[i].append (grade)
        
    return courses_and_details
    
def delete_coursedetails (dic, course):
    names = dic ["name"]
    lecturers = dic ["lecturer"]
    grades = dic ["grade"]
    for i in names:
        index = names.index (i)
        if i == course:
            names.remove(i)
            lecturers.pop(index)
            grades.pop(index)
    courses_and_details = {"name" : names, "lecturer": lecturers, "grade" : grades}
    return courses_and_details
    
def sort_alphabetically (dic, parameter):
    coursenamelist = dic[parameter]
    coursenamelist.sort()
    return coursenamelist
    
def list_of_all (dic, parameter):
    all_lecturers = dic [parameter]
    the_lecturers = []
    while len(all_lecturers) > 0:
        for i in all_lecturers:
            if i not in the_lecturers:
                the_lecturers.append(i)
                all_lecturers.remove(i)
            else:
                all_lecturers.remove (i)
    return the_lecturers
    
def courses_without (dic, without, output):
    grades = dic [without]
    coursenames = dic [output]
    indexlist = []
    coursenames_without_grades = []
    for i in grades:
        if i == 0:
            indexlist.append(grades.index(i))
    for y in indexlist:
        coursenames_without_grades.append(coursenames[y])
    return coursenames_without_grades
    
def count_grades (dic, num1, num2 = -1, num3 = -2):
    coursenames = dic["name"]
    grades = dic ["grade"]
    indexlist = []
    counted_grades = []
    for i in grades:
        if i == num1 or i == num2 or i == num3:
            indexlist.append(grades.index(i))
    for y in indexlist:
        counted_grades.append (coursenames[y])
    return counted_grades
    
def add_grade (dic, coursename, grade):
    coursenames = dic ["name"]
    lecturers = dic ["lecturer"]
    index = 0
    for i in coursenames:
        if i == coursename:
            index += coursename.index(i)
    delete_coursedetails (dic, coursename)
    add_coursedetails (coursename, lecturers[index], grade)
    return courses_and_details
    

add_coursedetails ("mathe", "Fritz", 5)
add_coursedetails ("biologie", "Karl", 1)
add_coursedetails ("bodenkunde", "Hansjörg", 2)
add_coursedetails ("sportkunde", "Franz", 2)
add_coursedetails ("statistik", "Sabrina", 4)
add_coursedetails ("raumplanung", "Julia", 3)
add_coursedetails ("ethik", "Klaus")
add_coursedetails (lecturer = "Hans", grade = 3, name = "hydrobiology")
add_coursedetails ("betriebswirtschaft", "Julia", 2)

print (courses_and_details)
print (sort_alphabetically(courses_and_details, "name"))
print (list_of_all(courses_and_details, "lecturer"))
print (courses_without(courses_and_details, without = "grade", output = "name"))
print (count_grades (courses_and_details, 1, 2, 3))
print (delete_coursedetails (courses_and_details, "biologie"))
print (add_grade (courses_and_details, "mathe", 3))




