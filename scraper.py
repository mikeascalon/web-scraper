from page_paser import get_citations_needed_count, get_citations_needed_report

url = "https://en.wikipedia.org/wiki/Washington_(state)"  # Replace with the URL you want to scrape

# Get the number of citations needed
citations_count = get_citations_needed_count(url)
print(f"Number of citations needed: {citations_count}")

# Get the citations report
citations_report = get_citations_needed_report(url)
print("Citations Needed Report:")
print(citations_report)