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

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT NAME, BEZIRK FROM bruecken ORDER BY BEZIRK;")
    db_result = cursor.fetchall()

    pprint.pprint(db_result)

    # Auch list-comprehension möglich
    formatted_result = []
    for name, bezirk in db_result:
        formatted_result.append({"name": name, "bezirk": bezirk})

    return formatted_result


if __name__ == "__main__":
    app.run(debug=True)
