import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://www.olx.in/items/q-car-cover"

# Set headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Send request
response = requests.get(url, headers=headers)

# Check for successful response
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    # OLX now uses dynamic rendering; scraping is limited to what's visible in static HTML
    for item in soup.find_all('li'):
        title_tag = item.find('h6')
        if title_tag:
            title = title_tag.get_text(strip=True)
            results.append(title)

    # Write results to file
    with open("olx_car_cover_results.txt", "w", encoding='utf-8') as file:
        for index, title in enumerate(results, start=1):
            file.write(f"{index}. {title}\n")

    print("Search results saved to 'olx_car_cover_results.txt'.")
else:
    print(f"Failed to fetch page: {response.status_code}")
