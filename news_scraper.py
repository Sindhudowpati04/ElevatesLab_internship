import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file="headlines.txt"):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = []
        for tag in soup.find_all(["h1", "h2", "h3"]):
            text = tag.get_text(strip=True)
            if text:
                headlines.append(text)

        with open(output_file, "w", encoding="utf-8") as f:
            for i, headline in enumerate(headlines, start=1):
                f.write(f"{i}. {headline}\n")

        print(f"✅ Scraping complete. {len(headlines)} headlines saved to {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    url = "https://www.bbc.com/news"
    scrape_headlines(url)
