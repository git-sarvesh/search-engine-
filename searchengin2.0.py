import requests
from bs4 import BeautifulSoup
import re

# Function to fetch and parse a web page
def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        return None

# Function to index words on a web page
def index_words(soup):
    index = {}
    words = re.findall(r'\w+', soup.get_text())
    for word in words:
        word = word.lower()
        if word in index:
            index[word] += 1
        else:
            index[word] = 1
    return index

# Function to remove common stop words
def remove_stop_words(index):
    stop_words = {'a', 'an', 'the', 'and', 'or', 'in', 'on', 'at'}
    for stop_word in stop_words:
        if stop_word in index:
            del index[stop_word]
    return index

# Function to search for a query in the indexed words
def search(query, index):
    query_words = re.findall(r'\w+', query.lower())
    results = {}
    for word in query_words:
        if word in index:
            results[word] = index[word]
    return results

# Function to perform a search on a given URL
def search_engine(url, query):
    soup = fetch_page(url)
    if soup is None:
        return None
    index = index_words(soup)
    index = remove_stop_words(index)
    results = search(query, index)
    return results

# to opean GitHub
url = "https://GitHub.com"
query = "GitHub"
results = search_engine(url, query)
print(f"Search results for '{query}' on {url}: {results}")
