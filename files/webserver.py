from flask import Flask, render_template, jsonify
import pprint
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/statistik-daten")
def statistik_daten():

    formatted_result = fetch_data()

    return jsonify(formatted_result)


@app.route("/statistik-view")
def statistik_view():

    # TODO: filtern nach Bezirk mit GET-parameter: request.args.get("bezirk")

    formatted_result = fetch_data()

    return render_template("data.html", formatted_result=formatted_result)


def fetch_data():

    connection = sqlite3.connect("stud.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT Datum, Inland_Frauen, Inland_Maenner FROM Studierendenstatistik ORDER BY Datum;"
    )
    db_result = cursor.fetchall()

    pprint.pprint(db_result)

    # Auch list-comprehension möglich
    formatted_result = []
    for datum, inland_frauen, inland_maenner in db_result:
        formatted_result.append(
            {
                "datum": datum,
                "inland_frauen": inland_frauen,
                "inland_maenner": inland_maenner,
            }
        )

    return formatted_result


if __name__ == "__main__":
    app.run(debug=True)
