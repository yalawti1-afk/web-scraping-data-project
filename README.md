\# Web Scraping and Data Analysis Project



\## Overview

A Python project that collects book information from Books to Scrape, cleans the data, performs statistical analysis, and generates visualizations.



\## Features

\- Web scraping using Requests and BeautifulSoup

\- Data cleaning and duplicate removal using Pandas

\- Price conversion and missing-value handling

\- Statistical analysis: mean, median, minimum, and maximum prices

\- Data visualization using Matplotlib

\- CSV reports and charts



\## Technologies

\- Python

\- Requests

\- BeautifulSoup

\- Pandas

\- Matplotlib



\## Project Outputs

\- `books.csv` — Raw scraped data

\- `books\_cleaned.csv` — Cleaned data

\- `analysis\_report.txt` — Statistical summary

\- `price\_distribution.png` — Price distribution chart

\- `top\_10\_expensive\_books.png` — Top 10 most expensive books



\## How to Run



Install the dependencies:



```bash

pip install requests beautifulsoup4 pandas matplotlib

```



Run the scraper:



```bash

python main.py

```



Clean and analyze the data:



```bash

python analyze\_data.py

```



Generate visualizations:



```bash

python visualize\_data.py

```



\## Data Source

\[Books to Scrape](https://books.toscrape.com/), a website designed for practicing web scraping.



\## Note

This is a learning and portfolio project. The analysis reflects the scraped sample and is not representative of all books or the broader book market.



