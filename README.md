"# SearchScoop-Brand-site-collector" 

# Brand Website Scraper

## Description

This web app allows users to input a list of brand names along with a keyword, and it automates the process of searching each brand name combined with the keyword on Google. The app retrieves the website link for each brand and presents the results in a table format. Users can also download the results as a CSV file.

## Features

- **Bulk Brand Name Input:** Upload a list of brand names in bulk.
- **Keyword Integration:** Input a keyword to refine the search (e.g., "clothing brand").
- **Automated Google Search:** The bot uses BeautifulSoup to perform Google searches for each brand name combined with the keyword.
- **Website Link Extraction:** Retrieves the website link for each search result.
- **Tabular Display:** Displays the results in a table format on the web app.
- **CSV Export:** Allows users to download the results as a CSV file.

## Technologies Used

- **Flask:** For creating the web application.
- **BeautifulSoup:** For web scraping and extracting website links from Google search results.
- **Pandas:** For handling data and generating the CSV file.

## Usage

1. **Upload Brand Names:** Upload a CSV file containing a list of brand names.
2. **Input Keyword:** Enter the keyword to refine the search.
3. **Run Search:** The bot performs Google searches and extracts website links.
4. **View Results:** The results are displayed in a table format on the web app.
5. **Download CSV:** Download the results as a CSV file for further use.

