# Amazon Price Analyzer

A Python-based web scraping and data analytics project that collects laptop product data from Amazon India, cleans and analyzes the data, and generates insights through visualizations.

## Features

* Scrapes product information from Amazon India
* Extracts:

  * Product Title
  * Product Price
  * Product Rating
* Stores raw data in CSV format
* Cleans and preprocesses scraped data
* Performs basic exploratory data analysis (EDA)
* Visualizes price trends and product comparisons
* Modular project structure for future ML and dashboard integration

## Project Structure

```text
Amazon-Price-Analyzer/
│
├── data/
│   ├── raw/
│   │   └── amazon_products.csv
│   │
│   └── processed/
│       └── clean_products.csv
│
├── scraper/
│   └── amazon_scraper.py
│
├── analysis/
│   ├── analyze.py
│   └── visualize.py
│
├── requirements.txt
│
└── README.md
```

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* Pandas
* Matplotlib
* lxml

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Amazon-Price-Analyzer
```

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Scrape Amazon Products

```bash
python scraper/amazon_scraper.py
```

This will create:

```text
data/raw/amazon_products.csv
```

### Step 2: Clean and Analyze Data

```bash
python analysis/analyze.py
```

This generates:

```text
data/processed/clean_products.csv
```

and displays:

* Dataset statistics
* Average price
* Highest priced product
* Lowest priced product

### Step 3: Visualize Data

```bash
python analysis/visualize.py
```

This displays charts for:

* Top expensive laptops
* Price comparisons
* Additional visual insights

## Sample Output

| Title                    | Price  | Rating |
| ------------------------ | ------ | ------ |
| Apple MacBook Pro M5 Max | 429900 | 4.3    |
| Lenovo Yoga Slim 7 Aura  | 110990 | 4.2    |
| Acer Aspire One          | 35990  | 3.2    |

## Future Enhancements

* Streamlit Dashboard
* Product Recommendation System
* Price Trend Tracking
* Multi-site Scraping (Amazon, Flipkart, Croma)
* PostgreSQL Integration
* Automated Daily Scraping
* Machine Learning-based Product Recommendations

## Learning Outcomes

This project demonstrates:

* Web Scraping
* Data Collection
* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* Python Project Structuring

## Disclaimer

This project is intended for educational and research purposes only. Users should comply with Amazon's Terms of Service and applicable laws when collecting data from websites.

## Author

Swati Keshri

Data Science | Machine Learning | AI Projects
