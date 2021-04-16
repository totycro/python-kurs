import math
import pandas as pd
import matplotlib.pyplot as plt


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

    df['Raum'] = exam_rooms

GRADES_MAIL = """n789: 4
e234: 1
m567: 5
f345: 4
a456: 3
"""
def add_grades(df, grades_mail):
    # 2)
    lines = grades_mail.splitlines()
    lines_pairs = [line.split(":") for line in lines]
    grades_dict = {
        matr_nr: int(grade)
        for matr_nr, grade in lines_pairs
    }
    import math
    df['Note'] = [
        grades_dict.get(matr_nr, math.nan)
        for matr_nr in df['Matr.Nr.']
    ]


def analyse_grades(df):
    # Alle Räume:
    rooms = df['Raum'].unique()

    # Variante 1: value_counts(0
    for room in rooms:
        # df filtern nach Einträgen in diesem Raum
        entries_room = df[df['Raum'] == room]

        # value_counts von Note: Werteverteilung
        vc = entries_room['Note'].value_counts()

        # Check ob 1 vorkommt
        if 1 in vc.index:
            count_grade_1 = vc.loc[1]
        else:
            count_grade_1 = 0

        print("Anzahl 1 in ", room, ":", count_grade_1)

    # Variante 2: Pandas filter kombinieren (auch in 2 Schritten möglich)
    for room in rooms:
        in_room_and_grade_1 = df[ (df['Raum'] == room) & (df['Note'] == 1) ]
        print("Anzahl 1 in ", room, ":", in_room_and_grade_1['Note'].count())


def main():
    df = pd.read_excel("exams.xlsx")
    print_df(df, "Daten initial")

    assign_exam_room(df)
    print_df(df, "Mit exam room")

    add_grades(df=df, grades_mail=GRADES_MAIL)
    print_df(df, "Mit grades")

    analyse_grades(df)

    # 4)
    df.hist(
        column="Note",
        # by="Raum",  # Gruppierung nach Räumen mit dieser Zeile
        bins=[1,2,3,4,5,6],
        sharey=True,
    )
    plt.show()



main()
