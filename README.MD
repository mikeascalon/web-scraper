
# LAB - Class 17

## Project: Web Scraping

**Author:** Michelangelo Ascalon

### Overview
This project is focused on web scraping, specifically designed to extract citation-needed information from Wikipedia pages. It utilizes Python along with libraries such as Requests and BeautifulSoup to parse HTML and retrieve data.

### Setup

#### Dependencies
- Make sure Python is installed on your machine.
- Install necessary Python packages from `requirements.txt` using the command:
  ```bash
  pip install -r requirements.txt
  ```

### How to Run the Application

1. Clone the repository to your local machine.
2. Navigate to the directory containing `scraper.py`.
3. Run the script using Python:
   ```bash
   python scraper.py
   ```

### How to Use

- Modify the `url` variable in `scraper.py` to the Wikipedia page you wish to scrape.
- The script will output the number of citations needed and a detailed report of each section requiring citations.

### Features

- **Citation Count**: Retrieves the total number of citations needed for a given Wikipedia page.
- **Citation Report**: Provides detailed information on which sections or paragraphs of the page need citations.



