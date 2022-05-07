# LinkedIn Profile Scraper

A Python-based web scraping tool that extracts professional information from LinkedIn profiles using Selenium and Chrome WebDriver.

## Features

-   Automated LinkedIn profile data extraction
-   Secure login handling with user credentials
-   Batch processing of multiple profiles from a single URL
-   Data export to CSV format
-   Collects comprehensive profile information including:
    -   Education history
    -   Employment details
    -   Professional skills
    -   Contact information (emails)

## Prerequisites

-   Python 3.x
-   Chrome browser
-   Chrome WebDriver
-   Selenium
-   Valid LinkedIn account

## Installation

1. Clone the repository:

```bash
git clone https://github.com/aryanbk/linkedin-scrapper.git
cd linkedin-scraper
```

2. Install required packages:

```bash
pip install selenium pandas
```

3. Download ChromeDriver that matches your Chrome browser version from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

## Usage

1. Configure your LinkedIn credentials in `config.txt`:

```txt
LINKEDIN_USERNAME = "your_email@example.com"
LINKEDIN_PASSWORD = "your_password"
```

2. Run the scraper:

```bash
python search_scraper.py --url "https://www.linkedin.com/company/example/people/"
```

## Output

The script generates a CSV file containing the following information for each profile:

-   Full Name
-   Education History
-   Employment History
-   Skills
-   Email Address (if available)
