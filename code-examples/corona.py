from urllib.request import urlopen, Request
import json
import matplotlib.pyplot as plt


def fetch_data():
    return json.loads(
        urlopen(
            Request(
                "https://corona.lmao.ninja/countries",
                headers={"User-Agent": "Mozilla/5.0"},
            )
        ).read()
    )


country_cases = fetch_data()
# country_cases is sorted list of dicts with country case data
top10 = country_cases[:10]
plt.bar(
    x=[country_data["country"] for country_data in top10],
    height=[country_data["cases"] for country_data in top10],
)
plt.show()
