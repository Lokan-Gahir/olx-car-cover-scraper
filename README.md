# OLX Car Cover Scraper 🛒

This is a simple Python script that scrapes search results for **"car cover"** listings from [OLX India](https://www.olx.in/items/q-car-cover) and saves the titles to a text file.

## 📌 Features
- Sends a request to the OLX search page
- Parses static HTML content using `BeautifulSoup`
- Extracts listing titles (if available)
- Saves results to `olx_car_cover_results.txt`

> ⚠️ **Note**: OLX uses dynamic content loading via JavaScript. This script only captures data from the static HTML response. For full scraping, tools like **Selenium** or **Playwright** are more suitable.

## 🛠️ Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

Install dependencies:
```bash
pip install requests beautifulsoup4
