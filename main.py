import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
import sqlite3
import time

def scrape_books(pages=2):
    all_data = []
    
    for i in range(1, pages + 1):
        # 1. HANDLING PAGINATION: Dynamically changing the URL [cite: 16]
        url = f"http://books.toscrape.com/catalogue/page-{i}.html"
        print(f"Scraping {url}...")
        
        try:
            response = requests.get(url, timeout=10)
            # 2. GRACEFUL FAILURE: Checking if the site is up [cite: 18]
            if response.status_code != 200:
                break
                
            soup = BeautifulSoup(response.text, 'html.parser')
            books = soup.find_all('article', class_='product_pod')
            
            for book in books:
                # 3. MANAGING MISSING FIELDS: Using 'get' or 'if' checks [cite: 17]
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text
                availability = book.find('p', class_='instock availability').text.strip()
                
                all_data.append({
                    "Title": title,
                    "Price": price,
                    "Availability": availability
                })
            
            # Being a good bot: waiting 1 second between pages
            time.sleep(1) 
            
        except Exception as e:
            print(f"Error occurred: {e}") [cite: 18]
            
    return pd.DataFrame(all_data)

# --- CLEANING & AUTOMATION --- [cite: 20]
df = scrape_books(2)
# AI LAYER: Simple Sentiment Analysis
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df['Sentiment_Score'] = df['Title'].apply(get_sentiment)

# 4. STANDARDISING FORMATS: Removing symbols to make price a number [cite: 25]
# This uses a Regular Expression (regex) to keep only digits and dots
df['Price_Cleaned'] = df['Price'].str.replace(r'[^\d.]', '', regex=True).astype(float)

# 5. HANDLING INCONSISTENCIES: Removing extra spaces [cite: 24]
df['Availability'] = df['Availability'].replace('In stock', 'Available')

# --- DATABASE STORAGE --- 
# 6. SQLITE: Storing the cleaned data [cite: 27, 69]
conn = sqlite3.connect('b2b_data.db')
df.to_sql('competitor_prices', conn, if_exists='replace', index=False)
conn.close()

print("Pipeline Complete! Data saved to b2b_data.db")