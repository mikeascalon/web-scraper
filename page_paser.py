import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    # Send an HTTP GET request to the provided URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all instances of the phrase "citation needed"
        citations_needed_count = len(soup.find_all(string="citation needed"))

        return citations_needed_count
    else:
        # Handle the case where the request was not successful
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        return None

def get_citations_needed_report(url):
    # Send an HTTP GET request to the provided URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all instances of the phrase "citation needed"
        citations = soup.find_all(string="citation needed")

        # Create a list to store the paragraphs containing "citation needed"
        citation_paragraphs = []

        # Iterate through each "citation needed" and find its parent element
        for citation in citations:
            parent_paragraph = citation.find_parent('p')

            if parent_paragraph:
                # Extract the text of the parent paragraph
                parent_text = parent_paragraph.get_text(strip=True)

                # Append the parent paragraph text to the list
                citation_paragraphs.append(parent_text)

        # Create a formatted report by joining the paragraphs
        report = "\n\n".join(citation_paragraphs)

        return report
    else:
        # Handle the case where the request was not successful
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        return None
