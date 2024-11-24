# README

# Indian Acts and Sections Scraper

This Python script scrapes Indian acts and sections from the [India Code](https://www.indiacode.nic.in/) website and structures the data into a JSON file. The scraper automates the extraction of acts, their sections, and section paragraphs, organizing them in a structured format.

## Features

- Extracts acts and sections from the India Code website.
- Collects detailed paragraphs for each section.
- Stores the scraped data in a JSON file for further use.
- Automatically navigates through pages and handles pagination.

## Requirements

- **Python 3.7+**
- **Selenium WebDriver**
- **Google Chrome** and **ChromeDriver**

## Installation

1. Clone this repository:

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have ChromeDriver installed and available in your PATH. You can download ChromeDriver from [here](https://chromedriver.chromium.org/downloads).

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. The script will navigate the India Code website, extract acts and sections, and save the data to a JSON file named `all_acts_sections.json`.

3. After completion, you can find the generated JSON file in the project directory.

## JSON Structure

The output JSON file is structured as follows:
```json
[
    {
        "act": "Act Name",
        "sections": [
            {
                "Section": "Section Name",
                "Paragraph": "Detailed content of the section"
            }
        ]
    }
]
```

## Notes

- Ensure a stable internet connection while running the script.
- The script may take time depending on the number of acts and sections being processed.
- For optimal performance, ensure the India Code website is accessible and responsive.

## Disclaimer

This project is intended for educational and research purposes only. Ensure compliance with all relevant terms and conditions of the India Code website before using this scraper.
