# SearchScoop-Brand Site Collector

# Brand Website Scraper

## Description

This web app allows users to input a list of brand names along with a keyword, and it automates the process of searching each brand name combined with the keyword on Google. The app retrieves the website link for each brand and presents the results in a table format. Users can also download the results as a CSV file.

![benchmark](https://github.com/MorshedulHoque/SearchScoop-Brand-site-collector/blob/main/images/Screenshot_1.png)

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

1. **Upload Brand Names:** Put the list of brand names.
   ![benchmark](https://github.com/MorshedulHoque/SearchScoop-Brand-site-collector/blob/main/images/Screenshot_2.png)
2. **Input Keyword:** Enter the keyword to refine the search.
   ![benchmark](https://github.com/MorshedulHoque/SearchScoop-Brand-site-collector/blob/main/images/Screenshot_3.png)
3. **Run Search:** The bot performs Google searches and extracts website links. We can observe that by the progress bar.
   ![benchmark](https://github.com/MorshedulHoque/SearchScoop-Brand-site-collector/blob/main/images/Screenshot_4.png)
4. **View Results:** The results are displayed in a table format on the web app.
   ![benchmark](https://github.com/MorshedulHoque/SearchScoop-Brand-site-collector/blob/main/images/Screenshot_5.png)
5. **Download CSV:** Download the results as a CSV file for further use.
   ![benchmark](https://github.com/MorshedulHoque/SearchScoop-Brand-site-collector/blob/main/images/Screenshot_5.png)

