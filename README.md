# B2B Market Intelligence: Competitor Price & Sentiment Monitor

## Problem Statement

In the B2B market research space, businesses constantly need insights about their competitors — especially around pricing, product availability, and positioning. Manually tracking competitor websites is time-consuming, inconsistent, and prone to human error.

This project automates that process by collecting, cleaning, and presenting competitor data in a structured and usable format.

---

## Solution Overview

This project is an end-to-end data pipeline that:

- Scrapes product data from a public website
- Cleans and standardizes raw data
- Stores it in a structured database
- Adds a sentiment analysis layer
- Presents insights through a dynamic dashboard

The goal was to build something practical that a business user can actually interact with.

---

## Tech Stack

- Python  
- BeautifulSoup (Web Scraping)  
- Pandas (Data Cleaning & Processing)  
- SQLite (Database)  
- Streamlit (Dashboard/UI)  
- TextBlob (Sentiment Analysis)  

---

## Pipeline Workflow

### 1. Data Scraping
- Extracts product title, price, and availability
- Handles pagination automatically
- Includes error handling for failed requests
- Safely manages missing fields

---

### 2. Data Cleaning
- Removes unwanted symbols from price using regex
- Converts price into numeric format
- Standardizes availability values
- Handles inconsistencies and missing data

---

### 3. AI Layer (Bonus)
- Uses TextBlob to generate sentiment scores from product titles
- Helps simulate competitor branding analysis

---

### 4. Data Storage
- Stores cleaned data in SQLite (`b2b_data.db`)
- No external database setup required
- Table: `competitor_prices`

---

### 5. Dashboard (User Interface)
A Streamlit dashboard provides an interactive way to view insights:

- Price distribution (bar chart)
- Inventory/availability insights
- Full product dataset

---

## Business Value

- Automates competitor data tracking  
- Reduces manual effort and errors  
- Provides quick insights into pricing and availability  
- Supports data-driven decision-making  

---

## Automation

The pipeline is designed to support automation and can be scheduled to run at regular intervals.
For example, using a cron job:
0 0 * * * python main.py
This ensures the data stays updated without manual intervention.

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

### Step 2: Run the pipeline (scraping + cleaning + storage)
python main.py

### Step 3: Launch the dashboard
streamlit run app.py
