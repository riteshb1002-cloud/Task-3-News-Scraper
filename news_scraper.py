import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://www.bbc.com/news"

# User-Agent
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    # Send GET request
    response = requests.get(url, headers=headers, timeout=10)

    # Check if request was successful
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all h2 elements
    headlines = soup.find_all("h2")

    # Store unique headlines
    unique_headlines = []

    for headline in headlines:
        title = headline.get_text(strip=True)

        if title and title not in unique_headlines:
            unique_headlines.append(title)

    # Save headlines to a text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for number, title in enumerate(unique_headlines, start=1):
            file.write(f"{number}. {title}\n")

    print("Headlines successfully scraped!")
    print("Total headlines found:", len(unique_headlines))
    print("Headlines saved to headlines.txt")

except requests.exceptions.RequestException as error:
    print("Error while accessing the website:")
    print(error)

except Exception as error:
    print("An unexpected error occurred:")
    print(error)