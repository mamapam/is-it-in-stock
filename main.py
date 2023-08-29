import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

scraping_url = os.getenv("SCRAPING_URL")
webhook_url = os.getenv("WEBHOOK_URL")

page = requests.get(scraping_url)
soup = BeautifulSoup(page.content, "lxml")

# --------- Set the element and the class to find on the page ---------

results = soup.find("button", {"class": "ProductForm__AddToCart"})

# ---------------------------------------------------------------------

# String version of the results found
data = str(results)

# Use the string of the results to find if item is available or not
if 'disabled="disabled"' in data:
    webhook_data = {"content": "Item IS NOT IN stock"}
    requests.post(webhook_url, webhook_data)
else:
    webhook_data = {"content": "Item IS IN stock"}
    requests.post(webhook_url, webhook_data)
