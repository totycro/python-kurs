import sqlite3
import requests
from bs4 import BeautifulSoup


def retrieve_current_forecast():
    page = requests.get("https://wetter.orf.at/wien/prognose")
    soup = BeautifulSoup(page.content, "html.parser")

    story_text = soup.find(id="ss-storyText")

    first_paragraph = story_text.find("p")
    text_of_first_paragraph = first_paragraph.text

    first_headline = story_text.find("h2")
    text_of_first_headline = first_headline.text

    return {
        "headline": text_of_first_headline,
        "text": text_of_first_paragraph,
    }


def save_to_database(forecast):
    connection = sqlite3.connect("forecast.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO forecasts(headline, text) VALUES (?, ?)",
        forecast["headline"],
        forecast["text"],
    )


if __name__ == "__main__":
    forecast = retrieve_current_forecast()
    save_to_database(forecast)
