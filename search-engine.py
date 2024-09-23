import requests
from bs4 import BeautifulSoup
import random

# List of websites to search
websites = [
    "https://youtube.com",
    "https://instagram.com",
    "https://hianime.to/"
]

# Function to fetch and parse a web page
def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        return None

# Function to perform a random search
def random_search():
    url = random.choice(websites)
    soup = fetch_page(url)
    if soup:
        # Extract all text from the page
        text = soup.get_text()
        # Split text into words
        words = text.split()
        # Choose a random word
        random_word = random.choice(words)
        print(f"Random word from {url}: {random_word}")
    else:
        print(f"Failed to fetch {url}")

# Perform a random search
random_search()
