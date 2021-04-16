import pandas as pd


def print_df(df, title):
    print("=" * 40)
    print(title)
    print("=" * 40)
    print(df)
    print()


def assign_exam_room(df):
    # 1)
    # Hier Variante mit list comprehension
    # Auch möglich: Liste mittels append() aufbauen
    # Auch möglich: .apply() von pandas
    def room_for_matr_nr(matr_nr):
        if int(matr_nr[1:]) % 2 == 0:
            return "A"
        else:
            return "B"

    exam_rooms = [room_for_matr_nr(matr_nr) for matr_nr in df['Matr.Nr.']]

    df['exam_room'] = exam_rooms

GRADES_MAIL = """n789: 4
e234: 1
m567: 5
"""
def add_grades(df, grades_mail):
    # 2)
    lines = grades_mail.splitlines()
    lines_pairs = [line.split(":") for line in lines]
    grades_dict = {
        matr_nr: int(grade)
        for matr_nr, grade in lines_pairs
    }
    df['grades'] = [
        grades_dict.get(matr_nr, "")
        for matr_nr in df['Matr.Nr.']
    ]


def main():
    df = pd.read_excel("exams.xlsx")
    print_df(df, "Daten initial")

    assign_exam_room(df)
    print_df(df, "Mit exam room")

    add_grades(df=df, grades_mail=GRADES_MAIL)
    print_df(df, "Mit grades")


main()
