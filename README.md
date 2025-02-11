# Depth-Crawler

**Depth-Crawler** is a web scraper built using Python that recursively extracts links from a starting URL up to a specified depth. The crawler uses libraries such as BeautifulSoup and Requests to parse HTML, follow links, and capture useful data from web pages. This project is designed to help with web scraping and exploring the structure of websites.

## Features

- **Recursive Link Crawling:** 
  - The scraper follows links starting from the provided URL and goes deeper up to the specified depth.
  
- **Form Handling:** 
  - Automatically detects forms on web pages and handles `GET` and `POST` requests for form submission.

- **Link Extraction:** 
  - Extracts and follows valid HTTP/HTTPS links from the web pages to crawl deeper.
  
- **Response Data Collection:** 
  - Collects response headers, form data, and other attributes for each page crawled.
  
- **Data Output:** 
  - Saves the crawled data (including responses and headers) in a structured JSON format for easy analysis.

## Tech Stack

- **Programming Language:** Python
- **Libraries:**
  - `BeautifulSoup` (for parsing HTML)
  - `requests` (for making HTTP requests)
  - `re` (for regular expressions)
  - `urllib` (for URL handling)
  - `faker` (for generating fake data if needed)
  
- **Data Storage:** 
  - JSON format for storing scraped data.

## Installation

### Prerequisites

Make sure the following dependencies are installed:

- Python 3.x
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/shivishivendra123/Depth-Crawler.git
cd Depth-Crawler
```

Usage
To run the web crawler, execute the script with the desired starting URL and depth.

Example
```bash
python depth_crawler.py
```

This will start crawling from http://quotes.toscrape.com (default URL in the script) and follow links up to a depth of 2.

You can change the URL and depth in the extract function inside the script:

```bash
extract('http://quotes.toscrape.com', 2)
```

Output
The crawler saves the collected data in a data.txt file in JSON format. The output will include details such as response headers, content, HTTP methods, and form data for each page crawled.

Example of output in data.txt:

{
  "http://quotes.toscrape.com": {
    "data": [
      {
        "response": {...},
        "content": "content",
        "method": "GET",
        "attr": "a",
        "depth": 0,
        "parent": "http://quotes.toscrape.com"
      }
    ]
  }
}

Contributing
Fork the repository.
Create your feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
