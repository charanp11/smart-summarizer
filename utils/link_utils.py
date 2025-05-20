import requests
from bs4 import BeautifulSoup

def extract_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        if not paragraphs:
            return "⚠️ Could not extract readable content from the provided link."
        return ' '.join([p.get_text().strip() for p in paragraphs])
    except Exception as e:
        return f"⚠️ Failed to extract content from URL: {str(e)}"
